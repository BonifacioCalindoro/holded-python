"""
Asynchronous treasury resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import AsyncBaseResource


class AsyncTreasuryResource(AsyncBaseResource):
    """
    Resource for interacting with the Treasury API asynchronously.
    """

    def __init__(self, client):
        """Initialize the treasury resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "treasury"

    async def list_accounts(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all treasury accounts asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of treasury accounts.
        """
        result = await self.client.get(f"{self.base_path}/accounts", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_account(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury account asynchronously.

        Args:
            data: Treasury account data.

        Returns:
            The created treasury account.
        """
        result = await self.client.post(f"{self.base_path}/accounts", data=data)
        return cast(Dict[str, Any], result)

    async def get_account(self, account_id: str) -> Dict[str, Any]:
        """
        Get a specific treasury account asynchronously.

        Args:
            account_id: The treasury account ID.

        Returns:
            The treasury account.
        """
        result = await self.client.get(f"{self.base_path}/accounts/{account_id}")
        return cast(Dict[str, Any], result)

    async def update_account(self, account_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury account asynchronously.

        Args:
            account_id: The treasury account ID.
            data: Updated treasury account data.

        Returns:
            The updated treasury account.
        """
        result = await self.client.put(f"{self.base_path}/accounts/{account_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_account(self, account_id: str) -> Dict[str, Any]:
        """
        Delete a treasury account asynchronously.

        Args:
            account_id: The treasury account ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"{self.base_path}/accounts/{account_id}")
        return cast(Dict[str, Any], result)

    async def list_transactions(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all treasury transactions asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of treasury transactions.
        """
        result = await self.client.get(f"{self.base_path}/transactions", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_transaction(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury transaction asynchronously.

        Args:
            data: Treasury transaction data.

        Returns:
            The created treasury transaction.
        """
        result = await self.client.post(f"{self.base_path}/transactions", data=data)
        return cast(Dict[str, Any], result)

    async def get_transaction(self, transaction_id: str) -> Dict[str, Any]:
        """
        Get a specific treasury transaction asynchronously.

        Args:
            transaction_id: The treasury transaction ID.

        Returns:
            The treasury transaction.
        """
        result = await self.client.get(f"{self.base_path}/transactions/{transaction_id}")
        return cast(Dict[str, Any], result)

    async def update_transaction(self, transaction_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury transaction asynchronously.

        Args:
            transaction_id: The treasury transaction ID.
            data: Updated treasury transaction data.

        Returns:
            The updated treasury transaction.
        """
        result = await self.client.put(f"{self.base_path}/transactions/{transaction_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_transaction(self, transaction_id: str) -> Dict[str, Any]:
        """
        Delete a treasury transaction asynchronously.

        Args:
            transaction_id: The treasury transaction ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"{self.base_path}/transactions/{transaction_id}")
        return cast(Dict[str, Any], result)

    async def reconcile_transaction(self, transaction_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reconcile a treasury transaction asynchronously.

        Args:
            transaction_id: The treasury transaction ID.
            data: Reconciliation data.

        Returns:
            The reconciled treasury transaction.
        """
        result = await self.client.post(f"{self.base_path}/transactions/{transaction_id}/reconcile", data=data)
        return cast(Dict[str, Any], result)

    async def list_categories(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all treasury categories asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of treasury categories.
        """
        result = await self.client.get(f"{self.base_path}/categories", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_category(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury category asynchronously.

        Args:
            data: Treasury category data.

        Returns:
            The created treasury category.
        """
        result = await self.client.post(f"{self.base_path}/categories", data=data)
        return cast(Dict[str, Any], result)

    async def update_category(self, category_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury category asynchronously.

        Args:
            category_id: The treasury category ID.
            data: Updated treasury category data.

        Returns:
            The updated treasury category.
        """
        result = await self.client.put(f"{self.base_path}/categories/{category_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_category(self, category_id: str) -> Dict[str, Any]:
        """
        Delete a treasury category asynchronously.

        Args:
            category_id: The treasury category ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"{self.base_path}/categories/{category_id}")
        return cast(Dict[str, Any], result)