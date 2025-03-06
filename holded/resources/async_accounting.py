"""
Asynchronous accounting resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, Union

from ..models.accounting import (
    AccountCreate, AccountUpdate, AccountListParams,
    AccountResponse, AccountListResponse, JournalEntryCreate,
    JournalEntryListParams, JournalEntryResponse, JournalEntryListResponse
)


class AsyncAccountingResource:
    """Resource for interacting with the Accounting API asynchronously."""

    def __init__(self, client):
        """Initialize the accounting resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "/accounting"

    async def list_entries(self, params: Optional[Union[Dict[str, Any], JournalEntryListParams]] = None) -> JournalEntryListResponse:
        """List all accounting entries asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit, from, to)

        Returns:
            A list of accounting entries
        """
        return await self.client.get(f"{self.base_path}/entry", params=params)

    async def create_entry(self, data: Union[Dict[str, Any], JournalEntryCreate]) -> JournalEntryResponse:
        """Create a new accounting entry asynchronously.

        Args:
            data: Entry data including at least 2 entry lines

        Returns:
            The created entry
        """
        return await self.client.post(f"{self.base_path}/entry", data=data)

    async def get_entry(self, entry_id: str) -> JournalEntryResponse:
        """Get a specific accounting entry asynchronously.

        Args:
            entry_id: The entry ID

        Returns:
            The entry details
        """
        return await self.client.get(f"{self.base_path}/entry/{entry_id}")

    async def list_accounts(self, params: Optional[Union[Dict[str, Any], AccountListParams]] = None) -> AccountListResponse:
        """List all accounting accounts asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of accounting accounts
        """
        return await self.client.get(f"{self.base_path}/account", params=params)

    async def create_account(self, data: Union[Dict[str, Any], AccountCreate]) -> AccountResponse:
        """Create a new accounting account asynchronously.

        Args:
            data: Account data

        Returns:
            The created account
        """
        return await self.client.post(f"{self.base_path}/account", data=data)

    async def get_account(self, account_id: str) -> AccountResponse:
        """Get a specific accounting account asynchronously.

        Args:
            account_id: The account ID

        Returns:
            The account details
        """
        return await self.client.get(f"{self.base_path}/account/{account_id}")

    async def update_account(self, account_id: str, data: Union[Dict[str, Any], AccountUpdate]) -> AccountResponse:
        """Update an accounting account asynchronously.

        Args:
            account_id: The account ID
            data: Updated account data

        Returns:
            The updated account
        """
        return await self.client.put(f"{self.base_path}/account/{account_id}", data=data)

    async def delete_account(self, account_id: str) -> Dict[str, Any]:
        """Delete an accounting account asynchronously.

        Args:
            account_id: The account ID

        Returns:
            A confirmation message
        """
        return await self.client.delete(f"{self.base_path}/account/{account_id}") 