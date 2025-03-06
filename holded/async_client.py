"""
Asynchronous client for the Holded API.
"""
import json
import logging
import asyncio
from typing import Any, Dict, Optional, TypeVar
from urllib.parse import urljoin

import aiohttp
from aiohttp import ClientError, ClientTimeout

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
        self.base_url = urljoin(base_url, api_version + "/")
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

    def _build_url(self, resource: str, endpoint: str, resource_id: Optional[str] = None) -> str:
        """
        Build the URL for the API request.

        Args:
            resource: The API resource (e.g., 'invoicing', 'accounting')
            endpoint: The endpoint (e.g., 'contacts', 'documents')
            resource_id: Optional resource ID for specific resource operations

        Returns:
            The complete URL for the API request
        """
        url = f"{self.base_url}/{resource}"
        if resource_id:
            url = f"{url}/{resource_id}"
        return url

    async def _handle_response(self, response: aiohttp.ClientResponse) -> Any:
        """
        Handle the API response and raise appropriate exceptions.

        Args:
            response: The aiohttp ClientResponse object

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
        try:
            if response.content_length and response.content_length > 0:
                response_json = await response.json()
            else:
                response_json = {}
        except json.JSONDecodeError:
            response_json = {}

        if 200 <= response.status < 300:
            return response_json

        error_message = response_json.get("message", "Unknown error")

        if response.status == 401:
            raise HoldedAuthError(response.status, response_json, error_message)
        elif response.status == 404:
            raise HoldedNotFoundError(response.status, response_json, error_message)
        elif response.status == 422:
            raise HoldedValidationError(response.status, response_json, error_message)
        elif response.status == 429:
            raise HoldedRateLimitError(response.status, response_json, error_message)
        elif 500 <= response.status < 600:
            raise HoldedServerError(response.status, response_json, error_message)
        else:
            raise HoldedAPIError(response.status, response_json, error_message)

    async def request(
        self,
        method: str,
        resource: str,
        endpoint: str,
        resource_id: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """
        Make an asynchronous request to the Holded API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            resource: API resource (e.g., 'invoicing', 'accounting')
            endpoint: API endpoint (e.g., 'contacts', 'documents')
            resource_id: Optional resource ID for specific resource operations
            params: Optional query parameters
            data: Optional request body data

        Returns:
            The parsed JSON response

        Raises:
            HoldedTimeoutError: When the request times out
            HoldedConnectionError: When there's a connection error
            Various HoldedAPIError subclasses for API errors
        """
        url = self._build_url(resource, endpoint, resource_id)
        session = await self._get_session()
        
        try:
            async with session.request(
                method=method,
                url=url,
                params=params,
                json=data,
                ssl=True,
            ) as response:
                return await self._handle_response(response)
        except aiohttp.ClientResponseError as e:
            raise HoldedAPIError(e.status, {}, str(e))
        except asyncio.TimeoutError:
            raise HoldedTimeoutError(f"Request timed out after {self.timeout} seconds")
        except ClientError as e:
            raise HoldedConnectionError(f"Connection error: {str(e)}")
        except Exception as e:
            if isinstance(e, HoldedError):
                raise
            raise HoldedError(message=f"Unexpected error: {str(e)}") from e

    async def get(
        self,
        resource: str,
        endpoint: str,
        resource_id: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """
        Make an asynchronous GET request to the Holded API.

        Args:
            resource: API resource (e.g., 'invoicing', 'accounting')
            endpoint: API endpoint (e.g., 'contacts', 'documents')
            resource_id: Optional resource ID for specific resource operations
            params: Optional query parameters

        Returns:
            The parsed JSON response
        """
        return await self.request("GET", resource, endpoint, resource_id, params)

    async def post(
        self,
        resource: str,
        endpoint: str,
        data: Dict[str, Any],
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """
        Make an asynchronous POST request to the Holded API.

        Args:
            resource: API resource (e.g., 'invoicing', 'accounting')
            endpoint: API endpoint (e.g., 'contacts', 'documents')
            data: Request body data
            params: Optional query parameters

        Returns:
            The parsed JSON response
        """
        return await self.request("POST", resource, endpoint, None, params, data)

    async def put(
        self,
        resource: str,
        endpoint: str,
        resource_id: str,
        data: Dict[str, Any],
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """
        Make an asynchronous PUT request to the Holded API.

        Args:
            resource: API resource (e.g., 'invoicing', 'accounting')
            endpoint: API endpoint (e.g., 'contacts', 'documents')
            resource_id: Resource ID for the specific resource
            data: Request body data
            params: Optional query parameters

        Returns:
            The parsed JSON response
        """
        return await self.request("PUT", resource, endpoint, resource_id, params, data)

    async def delete(
        self,
        resource: str,
        endpoint: str,
        resource_id: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """
        Make an asynchronous DELETE request to the Holded API.

        Args:
            resource: API resource (e.g., 'invoicing', 'accounting')
            endpoint: API endpoint (e.g., 'contacts', 'documents')
            resource_id: Resource ID for the specific resource
            params: Optional query parameters

        Returns:
            The parsed JSON response
        """
        return await self.request("DELETE", resource, endpoint, resource_id, params)

    async def close(self) -> None:
        """
        Close the aiohttp session.
        """
        if self.session and not self.session.closed:
            await self.session.close() 