"""
Resource for interacting with the Expense Accounts API.
"""
from typing import Any, Dict, Optional, Union

from ..models.expense_accounts import (
    ExpenseAccountCreate, ExpenseAccountUpdate, ExpenseAccountListParams,
    ExpenseAccountResponse, ExpenseAccountListResponse
)


class ExpenseAccountsResource:
    """Resource for interacting with the Expense Accounts API."""

    def __init__(self, client):
        """Initialize the expense accounts resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "/expenseAccounts"

    def list(self, params: Optional[Union[Dict[str, Any], ExpenseAccountListParams]] = None) -> ExpenseAccountListResponse:
        """List all expense accounts.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of expense accounts
        """
        return self.client.get(self.base_path, params=params)

    def create(self, data: Union[Dict[str, Any], ExpenseAccountCreate]) -> ExpenseAccountResponse:
        """Create a new expense account.

        Args:
            data: Expense account data

        Returns:
            The created expense account
        """
        return self.client.post(self.base_path, data=data)

    def get(self, account_id: str) -> ExpenseAccountResponse:
        """Get a specific expense account.

        Args:
            account_id: The expense account ID

        Returns:
            The expense account
        """
        return self.client.get(f"{self.base_path}/{account_id}")

    def update(self, account_id: str, data: Union[Dict[str, Any], ExpenseAccountUpdate]) -> ExpenseAccountResponse:
        """Update an expense account.

        Args:
            account_id: The expense account ID
            data: Updated expense account data

        Returns:
            The updated expense account
        """
        return self.client.put(f"{self.base_path}/{account_id}", data=data)

    def delete(self, account_id: str) -> Dict[str, Any]:
        """Delete an expense account.

        Args:
            account_id: The expense account ID

        Returns:
            A confirmation message
        """
        return self.client.delete(f"{self.base_path}/{account_id}") 