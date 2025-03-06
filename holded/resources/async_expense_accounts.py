"""
Asynchronous resource for interacting with the Expense Accounts API.
"""
from typing import Any, Dict, List, Optional, Union

from ..models.expense_accounts import (
    ExpenseAccountCreate, ExpenseAccountUpdate, ExpenseAccountListParams,
    ExpenseAccountResponse, ExpenseAccountListResponse
)


class AsyncExpenseAccountsResource:
    """Resource for interacting with the Expense Accounts API asynchronously."""

    def __init__(self, client):
        """Initialize the expense accounts resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "/expenseAccounts"

    async def list(self, params: Optional[Union[Dict[str, Any], ExpenseAccountListParams]] = None) -> ExpenseAccountListResponse:
        """List all expense accounts asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of expense accounts
        """
        return await self.client.get(self.base_path, params=params)

    async def create(self, data: Union[Dict[str, Any], ExpenseAccountCreate]) -> ExpenseAccountResponse:
        """Create a new expense account asynchronously.

        Args:
            data: Expense account data

        Returns:
            The created expense account
        """
        return await self.client.post(self.base_path, data=data)

    async def get(self, account_id: str) -> ExpenseAccountResponse:
        """Get a specific expense account asynchronously.

        Args:
            account_id: The expense account ID

        Returns:
            The expense account
        """
        return await self.client.get(f"{self.base_path}/{account_id}")

    async def update(self, account_id: str, data: Union[Dict[str, Any], ExpenseAccountUpdate]) -> ExpenseAccountResponse:
        """Update an expense account asynchronously.

        Args:
            account_id: The expense account ID
            data: Updated expense account data

        Returns:
            The updated expense account
        """
        return await self.client.put(f"{self.base_path}/{account_id}", data=data)

    async def delete(self, account_id: str) -> Dict[str, Any]:
        """Delete an expense account asynchronously.

        Args:
            account_id: The expense account ID

        Returns:
            A confirmation message
        """
        return await self.client.delete(f"{self.base_path}/{account_id}") 