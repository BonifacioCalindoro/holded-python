"""
Accounting resource for the Holded API.
"""
from typing import Any, Dict, Optional, Union

from ..models.accounting import (
     AccountCreate, AccountUpdate, AccountListParams,
    AccountResponse, AccountListResponse, JournalEntryCreate,
    JournalEntryListParams, JournalEntryResponse, JournalEntryListResponse
)


class AccountingResource:
    """Resource for interacting with the Accounting API."""

    def __init__(self, client):
        """Initialize the accounting resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "/accounting"

    def list_entries(self, params: Optional[Union[Dict[str, Any], JournalEntryListParams]] = None) -> JournalEntryListResponse:
        """List all accounting entries.

        Args:
            params: Optional query parameters (e.g., page, limit, from, to)

        Returns:
            A list of accounting entries
        """
        return self.client.get(f"{self.base_path}/entry", params=params)

    def create_entry(self, data: Union[Dict[str, Any], JournalEntryCreate]) -> JournalEntryResponse:
        """Create a new accounting entry.

        Args:
            data: Entry data including at least 2 entry lines

        Returns:
            The created entry
        """
        return self.client.post(f"{self.base_path}/entry", data=data)

    def get_entry(self, entry_id: str) -> JournalEntryResponse:
        """Get a specific accounting entry.

        Args:
            entry_id: The entry ID

        Returns:
            The entry details
        """
        return self.client.get(f"{self.base_path}/entry/{entry_id}")

    def list_accounts(self, params: Optional[Union[Dict[str, Any], AccountListParams]] = None) -> AccountListResponse:
        """List all accounting accounts.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of accounting accounts
        """
        return self.client.get(f"{self.base_path}/account", params=params)

    def create_account(self, data: Union[Dict[str, Any], AccountCreate]) -> AccountResponse:
        """Create a new accounting account.

        Args:
            data: Account data

        Returns:
            The created account
        """
        return self.client.post(f"{self.base_path}/account", data=data)

    def get_account(self, account_id: str) -> AccountResponse:
        """Get a specific accounting account.

        Args:
            account_id: The account ID

        Returns:
            The account details
        """
        return self.client.get(f"{self.base_path}/account/{account_id}")

    def update_account(self, account_id: str, data: Union[Dict[str, Any], AccountUpdate]) -> AccountResponse:
        """Update an accounting account.

        Args:
            account_id: The account ID
            data: Updated account data

        Returns:
            The updated account
        """
        return self.client.put(f"{self.base_path}/account/{account_id}", data=data)

    def delete_account(self, account_id: str) -> Dict[str, Any]:
        """Delete an accounting account.

        Args:
            account_id: The account ID

        Returns:
            A confirmation message
        """
        return self.client.delete(f"{self.base_path}/account/{account_id}") 