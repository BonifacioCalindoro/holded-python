"""
Asynchronous client for the Holded API.
"""
import json
import logging
import asyncio
from typing import Any, Dict, List, Optional, Type, TypeVar, Union
from urllib.parse import urljoin

import aiohttp
from aiohttp import ClientError, ClientTimeout
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
from .resources.async_accounting import AsyncAccountingResource
from .resources.async_contacts import AsyncContactsResource
from .resources.async_crm import AsyncCRMResource
from .resources.async_documents import AsyncDocumentsResource
from .resources.async_employees import AsyncEmployeesResource
from .resources.async_expense_accounts import AsyncExpenseAccountsResource
from .resources.async_numbering_series import AsyncNumberingSeriesResource
from .resources.async_products import AsyncProductsResource
from .resources.async_projects import AsyncProjectsResource
from .resources.async_remittances import AsyncRemittancesResource
from .resources.async_sales_channels import AsyncSalesChannelsResource
from .resources.async_treasury import AsyncTreasuryResource
from .resources.async_warehouse import AsyncWarehouseResource

logger = logging.getLogger(__name__)

T = TypeVar("T")


class AsyncHoldedClient:
    """
    Asynchronous client for the Holded API.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.holded.com/api/",
        api_version: str = "v1",
        timeout: int = 30,
        max_retries: int = 3,
        retry_delay: int = 1,
    ):
        """
        Initialize the asynchronous Holded API client.

        Args:
            api_key: Your Holded API key
            base_url: The base URL for the Holded API
            api_version: The API version to use
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
            retry_delay: Delay between retries in seconds
        """
        self.api_key = api_key
        self.base_url = base_url
        self.api_version = api_version
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.session = None
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Key": self.api_key,
        }

        # Initialize resources
        self.contacts = AsyncContactsResource(self)
        self.documents = AsyncDocumentsResource(self)
        self.products = AsyncProductsResource(self)
        self.warehouse = AsyncWarehouseResource(self)
        self.treasury = AsyncTreasuryResource(self)
        self.accounting = AsyncAccountingResource(self)
        self.employees = AsyncEmployeesResource(self)
        self.projects = AsyncProjectsResource(self)
        self.crm = AsyncCRMResource(self)
        self.sales_channels = AsyncSalesChannelsResource(self)
        self.numbering_series = AsyncNumberingSeriesResource(self)
        self.expense_accounts = AsyncExpenseAccountsResource(self)
        self.remittances = AsyncRemittancesResource(self)

    async def _get_session(self) -> aiohttp.ClientSession:
        """
        Get or create an aiohttp ClientSession.

        Returns:
            An aiohttp ClientSession
        """
        if self.session is None or self.session.closed:
            timeout = ClientTimeout(total=self.timeout)
            self.session = aiohttp.ClientSession(
                headers=self.headers,
                timeout=timeout,
            )
        return self.session

    def _build_url(self, path: str) -> str:
        """
        Build the URL for the API request.

        Args:
            path: The API path (e.g., 'invoicing/documents')

        Returns:
            The full URL.
        """
        values = path.split("/")
        service = values[0]
        endpoint = values[1]
        extra = values[2:]
        return urljoin(self.base_url, service + "/" + self.api_version + "/" + endpoint + "/" + "/".join(extra))

    def _serialize_data(self, data: Union[Dict[str, Any], BaseModel]) -> Dict[str, Any]:
        """
        Serialize data for a request.

        Args:
            data: The data to serialize.

        Returns:
            The serialized data.
        """
        if isinstance(data, BaseModel):
            return data.model_dump(exclude_none=True)
        return data

    async def _handle_response(
        self, response: aiohttp.ClientResponse, response_model: Optional[Type[T]] = None
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """
        Handle the API response and raise appropriate exceptions.

        Args:
            response: The aiohttp ClientResponse object
            response_model: Optional Pydantic model to deserialize to

        Returns:
            The parsed JSON response

        Raises:
            HoldedAuthError: When authentication fails
            HoldedNotFoundError: When a resource is not found
            HoldedValidationError: When there's a validation error
            HoldedRateLimitError: When the rate limit is exceeded
            HoldedServerError: When there's a server error
            HoldedAPIError: For other API errors
        """
        status_code = response.status
        content_type = response.headers.get("Content-Type", "")

        try:
            if "application/json" in content_type:
                data = await response.json()
            else:
                text = await response.text()
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    data = {"message": text}
        except Exception as e:
            raise HoldedAPIError(f"Failed to parse response: {str(e)}", status_code=status_code)

        if status_code >= 400:
            error_message = data.get("message", str(data))
            if status_code == 401:
                raise HoldedAuthError(error_message, status_code=status_code, error_data=data)
            elif status_code == 404:
                raise HoldedNotFoundError(error_message, status_code=status_code, error_data=data)
            elif status_code == 422:
                raise HoldedValidationError(error_message, status_code=status_code, error_data=data)
            elif status_code == 429:
                raise HoldedRateLimitError(error_message, status_code=status_code, error_data=data)
            elif status_code >= 500:
                raise HoldedServerError(error_message, status_code=status_code, error_data=data)
            else:
                raise HoldedAPIError(error_message, status_code=status_code, error_data=data)

        if response_model is not None:
            return response_model.model_validate(data)
        return data

    async def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Union[Dict[str, Any], BaseModel]] = None,
        response_model: Optional[Type[T]] = None,
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """
        Make an asynchronous request to the Holded API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            path: API path (e.g., 'invoicing/documents')
            params: Optional query parameters
            data: Optional request body data
            response_model: Optional Pydantic model to deserialize to

        Returns:
            The parsed JSON response

        Raises:
            HoldedTimeoutError: When the request times out
            HoldedConnectionError: When there's a connection error
            Various HoldedAPIError subclasses for API errors
        """
        url = self._build_url(path)
        session = await self._get_session()
        
        if data is not None:
            data = self._serialize_data(data)

        for attempt in range(self.max_retries):
            try:
                async with session.request(
                    method=method,
                    url=url,
                    params=params,
                    json=data,
                    ssl=True,
                ) as response:
                    return await self._handle_response(response, response_model)
            except (HoldedRateLimitError, HoldedServerError) as e:
                if attempt < self.max_retries - 1:
                    wait_time = self.retry_delay * (2 ** attempt)
                    logger.warning(
                        f"Request failed with {e.__class__.__name__}. "
                        f"Retrying in {wait_time} seconds..."
                    )
                    await asyncio.sleep(wait_time)
                else:
                    raise
            except aiohttp.ClientConnectorError as e:
                raise HoldedConnectionError(f"Connection error: {str(e)}")
            except asyncio.TimeoutError:
                raise HoldedTimeoutError("Request timed out")
            except HoldedError:
                raise
            except Exception as e:
                raise HoldedError(f"Unexpected error: {str(e)}")

    async def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        response_model: Optional[Type[T]] = None,
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """
        Make an asynchronous GET request to the Holded API.

        Args:
            path: API path (e.g., 'invoicing/documents')
            params: Optional query parameters
            response_model: Optional Pydantic model to deserialize to

        Returns:
            The parsed JSON response
        """
        return await self.request("GET", path, params=params, response_model=response_model)

    async def post(
        self,
        path: str,
        data: Optional[Union[Dict[str, Any], BaseModel]] = None,
        params: Optional[Dict[str, Any]] = None,
        response_model: Optional[Type[T]] = None,
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """
        Make an asynchronous POST request to the Holded API.

        Args:
            path: API path (e.g., 'invoicing/documents')
            data: Request body data
            params: Optional query parameters
            response_model: Optional Pydantic model to deserialize to

        Returns:
            The parsed JSON response
        """
        return await self.request("POST", path, params=params, data=data, response_model=response_model)

    async def put(
        self,
        path: str,
        data: Optional[Union[Dict[str, Any], BaseModel]] = None,
        params: Optional[Dict[str, Any]] = None,
        response_model: Optional[Type[T]] = None,
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """
        Make an asynchronous PUT request to the Holded API.

        Args:
            path: API path (e.g., 'invoicing/documents')
            data: Request body data
            params: Optional query parameters
            response_model: Optional Pydantic model to deserialize to

        Returns:
            The parsed JSON response
        """
        return await self.request("PUT", path, params=params, data=data, response_model=response_model)

    async def delete(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        response_model: Optional[Type[T]] = None,
    ) -> Union[Dict[str, Any], List[Dict[str, Any]], T]:
        """
        Make an asynchronous DELETE request to the Holded API.

        Args:
            path: API path (e.g., 'invoicing/documents')
            params: Optional query parameters
            response_model: Optional Pydantic model to deserialize to

        Returns:
            The parsed JSON response
        """
        return await self.request("DELETE", path, params=params, response_model=response_model)

    async def close(self) -> None:
        """
        Close the aiohttp session.
        """
        if self.session and not self.session.closed:
            await self.session.close() 