"""
Synchronous client for the Holded API.
"""
import json
import logging
import time
from typing import Any, Dict, List, Optional, Type, TypeVar, Union
from urllib.parse import urljoin

import requests
from pydantic import BaseModel

from .exceptions import (
    HoldedAPIError,
    HoldedAuthError,
    HoldedConnectionError,
    HoldedError,
    HoldedNotFoundError,
    HoldedRateLimitError,
    HoldedServerError,
    HoldedTimeoutError,
    HoldedValidationError,
)
from .resources.accounting import AccountingResource
from .resources.contacts import ContactsResource
from .resources.crm import CRMResource
from .resources.documents import DocumentsResource
from .resources.employees import EmployeesResource
from .resources.expense_accounts import ExpenseAccountsResource
from .resources.numbering_series import NumberingSeriesResource
from .resources.products import ProductsResource
from .resources.projects import ProjectsResource
from .resources.remittances import RemittancesResource
from .resources.sales_channels import SalesChannelsResource
from .resources.treasury import TreasuryResource
from .resources.warehouse import WarehouseResource

logger = logging.getLogger(__name__)

T = TypeVar("T")


class HoldedClient:
    """Client for the Holded API."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.holded.com/api/",
        api_version: str = "v1",
        timeout: int = 30,
        max_retries: int = 3,
        retry_delay: int = 1,
    ):
        """Initialize the Holded client.

        Args:
            api_key: Your Holded API key.
            base_url: The base URL for the Holded API.
            api_version: The API version to use.
            timeout: Request timeout in seconds.
            max_retries: Maximum number of retries for failed requests.
            retry_delay: Delay between retries in seconds.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.api_version = api_version
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Key": self.api_key,
            }
        )

        # Initialize resources
        self.contacts = ContactsResource(self)
        self.documents = DocumentsResource(self)
        self.products = ProductsResource(self)
        self.warehouse = WarehouseResource(self)
        self.treasury = TreasuryResource(self)
        self.accounting = AccountingResource(self)
        self.employees = EmployeesResource(self)
        self.projects = ProjectsResource(self)
        self.crm = CRMResource(self)
        self.sales_channels = SalesChannelsResource(self)
        self.numbering_series = NumberingSeriesResource(self)
        self.expense_accounts = ExpenseAccountsResource(self)
        self.remittances = RemittancesResource(self)

    def _build_url(self, path: str) -> str:
        """Build the URL for the API request.

        Args:
            path: The API path (e.g., 'invoicing/documents')

        Returns:
            The full URL.
        """
        values = path.split("/")
        service = values[0]
        endpoint = values[1]
        extra = values[2:]
        print(self.base_url  + service + "/" + self.api_version + "/" + endpoint + "/" + "/".join(extra))
        return urljoin(self.base_url, service + "/" + self.api_version + "/" + endpoint + "/" + "/".join(extra))

    def _serialize_data(self, data: Union[Dict[str, Any], BaseModel]) -> Dict[str, Any]:
        """Serialize data for a request.

        Args:
            data: The data to serialize.

        Returns:
            The serialized data.
        """
        if isinstance(data, BaseModel):
            return data.model_dump(exclude_none=True)
        return data

    def _deserialize_response(
        self, response: requests.Response, response_model: Optional[Type[T]] = None
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """Deserialize a response.

        Args:
            response: The response to deserialize.
            response_model: Optional Pydantic model to deserialize to.

        Returns:
            The deserialized response.
        """
        try:
            data = response.json()
        except ValueError:
            data = {"message": response.text}

        if response_model is not None:
            return response_model.model_validate(data)
        return data

    def _handle_response(
        self, response: requests.Response, response_model: Optional[Type[T]] = None
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """Handle a response from the API.

        Args:
            response: The response to handle.
            response_model: Optional Pydantic model to deserialize to.

        Returns:
            The response data.

        Raises:
            HoldedAuthError: If authentication fails.
            HoldedNotFoundError: If the resource is not found.
            HoldedValidationError: If the request is invalid.
            HoldedRateLimitError: If the rate limit is exceeded.
            HoldedServerError: If the server returns an error.
            HoldedAPIError: For other API errors.
        """
        try:
            response.raise_for_status()
            return self._deserialize_response(response, response_model)
        except requests.exceptions.HTTPError as e:
            error_data = {}
            try:
                error_data = response.json()
            except ValueError:
                error_data = {"message": response.text}

            status_code = response.status_code
            if status_code == 401:
                raise HoldedAuthError(
                    message="Authentication failed. Check your API key.",
                    status_code=status_code,
                    error_data=error_data,
                )
            elif status_code == 404:
                raise HoldedNotFoundError(
                    message="Resource not found.",
                    status_code=status_code,
                    error_data=error_data,
                )
            elif status_code == 422:
                raise HoldedValidationError(
                    message="Validation error.",
                    status_code=status_code,
                    error_data=error_data,
                )
            elif status_code == 429:
                raise HoldedRateLimitError(
                    message="Rate limit exceeded.",
                    status_code=status_code,
                    error_data=error_data,
                )
            elif status_code >= 500:
                raise HoldedServerError(
                    message="Server error.",
                    status_code=status_code,
                    error_data=error_data,
                )
            else:
                raise HoldedAPIError(
                    message=f"API error: {response.text}",
                    status_code=status_code,
                    error_data=error_data,
                )

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Union[Dict[str, Any], BaseModel]] = None,
        data: Optional[Union[Dict[str, Any], BaseModel]] = None,
        response_model: Optional[Type[T]] = None,
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """Make a request to the API.

        Args:
            method: The HTTP method to use.
            path: The API endpoint path.
            params: Optional query parameters.
            data: Optional request data.
            response_model: Optional Pydantic model to deserialize to.

        Returns:
            The response data.

        Raises:
            HoldedConnectionError: If the connection fails.
            HoldedTimeoutError: If the request times out.
            HoldedError: For other errors.
        """
        url = self._build_url(path)
        
        # Serialize params and data if they are Pydantic models
        if params is not None and isinstance(params, BaseModel):
            params = params.model_dump(exclude_none=True)
        
        if data is not None:
            data = self._serialize_data(data)
            data_str = json.dumps(data)
        else:
            data_str = None

        for attempt in range(self.max_retries):
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    params=params,
                    data=data_str,
                    timeout=self.timeout,
                )
                return self._handle_response(response, response_model)
            except (requests.exceptions.ConnectionError, requests.exceptions.SSLError) as e:
                if attempt == self.max_retries - 1:
                    raise HoldedConnectionError(
                        message=f"Connection error: {str(e)}"
                    ) from e
                time.sleep(self.retry_delay)
            except requests.exceptions.Timeout as e:
                if attempt == self.max_retries - 1:
                    raise HoldedTimeoutError(
                        message=f"Request timed out: {str(e)}"
                    ) from e
                time.sleep(self.retry_delay)
            except (HoldedRateLimitError, HoldedServerError) as e:
                if attempt == self.max_retries - 1:
                    raise
                time.sleep(self.retry_delay * (attempt + 1))
            except Exception as e:
                if isinstance(e, HoldedError):
                    raise
                raise HoldedError(message=f"Unexpected error: {str(e)}") from e

    def get(
        self,
        path: str,
        params: Optional[Union[Dict[str, Any], BaseModel]] = None,
        response_model: Optional[Type[T]] = None,
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """Make a GET request.

        Args:
            path: The API endpoint path.
            params: Optional query parameters.
            response_model: Optional Pydantic model to deserialize to.

        Returns:
            The response data.
        """
        return self._request("GET", path, params=params, response_model=response_model)

    def post(
        self,
        path: str,
        data: Optional[Union[Dict[str, Any], BaseModel]] = None,
        params: Optional[Union[Dict[str, Any], BaseModel]] = None,
        response_model: Optional[Type[T]] = None,
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """Make a POST request.

        Args:
            path: The API endpoint path.
            data: The request data.
            params: Optional query parameters.
            response_model: Optional Pydantic model to deserialize to.

        Returns:
            The response data.
        """
        return self._request("POST", path, params=params, data=data, response_model=response_model)

    def put(
        self,
        path: str,
        data: Optional[Union[Dict[str, Any], BaseModel]] = None,
        params: Optional[Union[Dict[str, Any], BaseModel]] = None,
        response_model: Optional[Type[T]] = None,
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """Make a PUT request.

        Args:
            path: The API endpoint path.
            data: The request data.
            params: Optional query parameters.
            response_model: Optional Pydantic model to deserialize to.

        Returns:
            The response data.
        """
        return self._request("PUT", path, params=params, data=data, response_model=response_model)

    def delete(
        self,
        path: str,
        params: Optional[Union[Dict[str, Any], BaseModel]] = None,
        response_model: Optional[Type[T]] = None,
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """Make a DELETE request.

        Args:
            path: The API endpoint path.
            params: Optional query parameters.
            response_model: Optional Pydantic model to deserialize to.

        Returns:
            The response data.
        """
        return self._request("DELETE", path, params=params, response_model=response_model)

    def close(self) -> None:
        """Close the client session."""
        self.session.close() 