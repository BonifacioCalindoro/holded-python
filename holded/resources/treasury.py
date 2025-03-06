"""
Treasury resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import BaseResource


class TreasuryResource(BaseResource):
    """
    Resource for interacting with the Treasury API.
    """

    def list_accounts(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all treasury accounts.

        Args:
            params: Optional query parameters.

        Returns:
            A list of treasury accounts.
        """
        result = self.client.get("treasury/accounts", params=params)
        return result

    def create_account(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury account.

        Args:
            data: Treasury account data.

        Returns:
            The created treasury account.
        """
        result = self.client.post("treasury/accounts", data=data)
        return result

    def get_account(self, account_id: str) -> Dict[str, Any]:
        """
        Get a specific treasury account.

        Args:
            account_id: The treasury account ID.

        Returns:
            The treasury account.
        """
        result = self.client.get(f"treasury/accounts/{account_id}")
        return result

    def update_account(self, account_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury account.

        Args:
            account_id: The treasury account ID.
            data: Updated treasury account data.

        Returns:
            The updated treasury account.
        """
        result = self.client.put(f"treasury/accounts/{account_id}", data=data)
        return result

    def delete_account(self, account_id: str) -> Dict[str, Any]:
        """
        Delete a treasury account.

        Args:
            account_id: The treasury account ID.

        Returns:
            A confirmation message.
        """
        result = self.client.delete(f"treasury/accounts/{account_id}")
        return result

    def list_transactions(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all treasury transactions.

        Args:
            params: Optional query parameters.

        Returns:
            A list of treasury transactions.
        """
        result = self.client.get("treasury/transactions", params=params)
        return result

    def create_transaction(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury transaction.

        Args:
            data: Treasury transaction data.

        Returns:
            The created treasury transaction.
        """
        result = self.client.post("treasury/transactions", data=data)
        return result

    def get_transaction(self, transaction_id: str) -> Dict[str, Any]:
        """
        Get a specific treasury transaction.

        Args:
            transaction_id: The treasury transaction ID.

        Returns:
            The treasury transaction.
        """
        result = self.client.get(f"treasury/transactions/{transaction_id}")
        return result

    def update_transaction(self, transaction_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury transaction.

        Args:
            transaction_id: The treasury transaction ID.
            data: Updated treasury transaction data.

        Returns:
            The updated treasury transaction.
        """
        result = self.client.put(f"treasury/transactions/{transaction_id}", data=data)
        return result

    def delete_transaction(self, transaction_id: str) -> Dict[str, Any]:
        """
        Delete a treasury transaction.

        Args:
            transaction_id: The treasury transaction ID.

        Returns:
            A confirmation message.
        """
        result = self.client.delete(f"treasury/transactions/{transaction_id}")
        return result

    def reconcile_transaction(self, transaction_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reconcile a treasury transaction.

        Args:
            transaction_id: The treasury transaction ID.
            data: Reconciliation data.

        Returns:
            The reconciled treasury transaction.
        """
        result = self.client.post(f"treasury/transactions/{transaction_id}/reconcile", data=data)
        return result

    def list_categories(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all treasury categories.

        Args:
            params: Optional query parameters.

        Returns:
            A list of treasury categories.
        """
        result = self.client.get("treasury/categories", params=params)
        return result

    def create_category(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury category.

        Args:
            data: Treasury category data.

        Returns:
            The created treasury category.
        """
        result = self.client.post("treasury/categories", data=data)
        return result

    def update_category(self, category_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury category.

        Args:
            category_id: The treasury category ID.
            data: Updated treasury category data.

        Returns:
            The updated treasury category.
        """
        result = self.client.put(f"treasury/categories/{category_id}", data=data)
        return result

    def delete_category(self, category_id: str) -> Dict[str, Any]:
        """
        Delete a treasury category.

        Args:
            category_id: The treasury category ID.

        Returns:
            A confirmation message.
        """
        result = self.client.delete(f"treasury/categories/{category_id}")
        return result