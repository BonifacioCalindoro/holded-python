"""
Asynchronous treasury resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import AsyncBaseResource


class AsyncTreasuryResource(AsyncBaseResource):
    """
    Resource for interacting with the Treasury API asynchronously.
    """

    async def list_accounts(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all treasury accounts asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of treasury accounts
        """
        result = await self.client.get("treasury", "accounts", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_account(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury account asynchronously.

        Args:
            data: Account data

        Returns:
            The created treasury account
        """
        result = await self.client.post("treasury", "accounts", data)
        return cast(Dict[str, Any], result)

    async def get_account(self, account_id: str) -> Dict[str, Any]:
        """
        Get a specific treasury account asynchronously.

        Args:
            account_id: The account ID

        Returns:
            The treasury account details
        """
        result = await self.client.get("treasury", "accounts", account_id)
        return cast(Dict[str, Any], result)

    async def update_account(self, account_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury account asynchronously.

        Args:
            account_id: The account ID
            data: Updated account data

        Returns:
            The updated treasury account
        """
        result = await self.client.put("treasury", "accounts", account_id, data)
        return cast(Dict[str, Any], result)

    async def delete_account(self, account_id: str) -> Dict[str, Any]:
        """
        Delete a treasury account asynchronously.

        Args:
            account_id: The account ID

        Returns:
            The deletion response
        """
        result = await self.client.delete("treasury", "accounts", account_id)
        return cast(Dict[str, Any], result)

    async def list_transactions(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all treasury transactions asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of treasury transactions
        """
        result = await self.client.get("treasury", "transactions", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_transaction(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury transaction asynchronously.

        Args:
            data: Transaction data

        Returns:
            The created treasury transaction
        """
        result = await self.client.post("treasury", "transactions", data)
        return cast(Dict[str, Any], result)

    async def get_transaction(self, transaction_id: str) -> Dict[str, Any]:
        """
        Get a specific treasury transaction asynchronously.

        Args:
            transaction_id: The transaction ID

        Returns:
            The treasury transaction details
        """
        result = await self.client.get("treasury", "transactions", transaction_id)
        return cast(Dict[str, Any], result)

    async def update_transaction(self, transaction_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury transaction asynchronously.

        Args:
            transaction_id: The transaction ID
            data: Updated transaction data

        Returns:
            The updated treasury transaction
        """
        result = await self.client.put("treasury", "transactions", transaction_id, data)
        return cast(Dict[str, Any], result)

    async def delete_transaction(self, transaction_id: str) -> Dict[str, Any]:
        """
        Delete a treasury transaction asynchronously.

        Args:
            transaction_id: The transaction ID

        Returns:
            The deletion response
        """
        result = await self.client.delete("treasury", "transactions", transaction_id)
        return cast(Dict[str, Any], result)

    async def list_account_transactions(self, account_id: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all transactions for a specific treasury account asynchronously.

        Args:
            account_id: The account ID
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of transactions for the account
        """
        result = await self.client.get("treasury", f"accounts/{account_id}/transactions", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_account_transaction(self, account_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new transaction for a specific treasury account asynchronously.

        Args:
            account_id: The account ID
            data: Transaction data

        Returns:
            The created transaction
        """
        result = await self.client.post("treasury", f"accounts/{account_id}/transactions", data)
        return cast(Dict[str, Any], result)

    async def reconcile_transaction(self, transaction_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reconcile a treasury transaction asynchronously.

        Args:
            transaction_id: The transaction ID
            data: Reconciliation data

        Returns:
            The reconciled transaction
        """
        result = await self.client.put("treasury", f"transactions/{transaction_id}/reconcile", data)
        return cast(Dict[str, Any], result)

    async def list_categories(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all treasury categories asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of treasury categories
        """
        result = await self.client.get("treasury", "categories", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_category(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury category asynchronously.

        Args:
            data: Category data

        Returns:
            The created treasury category
        """
        result = await self.client.post("treasury", "categories", data)
        return cast(Dict[str, Any], result)

    async def update_category(self, category_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury category asynchronously.

        Args:
            category_id: The category ID
            data: Updated category data

        Returns:
            The updated treasury category
        """
        result = await self.client.put("treasury", "categories", category_id, data)
        return cast(Dict[str, Any], result)

    async def delete_category(self, category_id: str) -> Dict[str, Any]:
        """
        Delete a treasury category asynchronously.

        Args:
            category_id: The category ID

        Returns:
            The deletion response
        """
        result = await self.client.delete("treasury", "categories", category_id)
        return cast(Dict[str, Any], result)