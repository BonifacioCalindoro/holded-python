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
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of treasury accounts
        """
        result = self.client.get("treasury", "accounts", params=params)
        return cast(List[Dict[str, Any]], result)

    def create_account(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury account.

        Args:
            data: Account data

        Returns:
            The created treasury account
        """
        result = self.client.post("treasury", "accounts", data)
        return cast(Dict[str, Any], result)

    def get_account(self, account_id: str) -> Dict[str, Any]:
        """
        Get a specific treasury account.

        Args:
            account_id: The account ID

        Returns:
            The treasury account details
        """
        result = self.client.get("treasury", "accounts", account_id)
        return cast(Dict[str, Any], result)

    def update_account(self, account_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury account.

        Args:
            account_id: The account ID
            data: Updated account data

        Returns:
            The updated treasury account
        """
        result = self.client.put("treasury", "accounts", account_id, data)
        return cast(Dict[str, Any], result)

    def delete_account(self, account_id: str) -> Dict[str, Any]:
        """
        Delete a treasury account.

        Args:
            account_id: The account ID

        Returns:
            The deletion response
        """
        result = self.client.delete("treasury", "accounts", account_id)
        return cast(Dict[str, Any], result)

    def list_transactions(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all treasury transactions.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of treasury transactions
        """
        result = self.client.get("treasury", "transactions", params=params)
        return cast(List[Dict[str, Any]], result)

    def create_transaction(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury transaction.

        Args:
            data: Transaction data

        Returns:
            The created treasury transaction
        """
        result = self.client.post("treasury", "transactions", data)
        return cast(Dict[str, Any], result)

    def get_transaction(self, transaction_id: str) -> Dict[str, Any]:
        """
        Get a specific treasury transaction.

        Args:
            transaction_id: The transaction ID

        Returns:
            The treasury transaction details
        """
        result = self.client.get("treasury", "transactions", transaction_id)
        return cast(Dict[str, Any], result)

    def update_transaction(self, transaction_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury transaction.

        Args:
            transaction_id: The transaction ID
            data: Updated transaction data

        Returns:
            The updated treasury transaction
        """
        result = self.client.put("treasury", "transactions", transaction_id, data)
        return cast(Dict[str, Any], result)

    def delete_transaction(self, transaction_id: str) -> Dict[str, Any]:
        """
        Delete a treasury transaction.

        Args:
            transaction_id: The transaction ID

        Returns:
            The deletion response
        """
        result = self.client.delete("treasury", "transactions", transaction_id)
        return cast(Dict[str, Any], result)

    def list_account_transactions(self, account_id: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all transactions for a specific treasury account.

        Args:
            account_id: The account ID
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of transactions for the account
        """
        result = self.client.get("treasury", f"accounts/{account_id}/transactions", params=params)
        return cast(List[Dict[str, Any]], result)

    def create_account_transaction(self, account_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new transaction for a specific treasury account.

        Args:
            account_id: The account ID
            data: Transaction data

        Returns:
            The created transaction
        """
        result = self.client.post("treasury", f"accounts/{account_id}/transactions", data)
        return cast(Dict[str, Any], result)

    def reconcile_transaction(self, transaction_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reconcile a treasury transaction.

        Args:
            transaction_id: The transaction ID
            data: Reconciliation data

        Returns:
            The reconciled transaction
        """
        result = self.client.put("treasury", f"transactions/{transaction_id}/reconcile", data)
        return cast(Dict[str, Any], result)

    def list_categories(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all treasury categories.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of treasury categories
        """
        result = self.client.get("treasury", "categories", params=params)
        return cast(List[Dict[str, Any]], result)

    def create_category(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new treasury category.

        Args:
            data: Category data

        Returns:
            The created treasury category
        """
        result = self.client.post("treasury", "categories", data)
        return cast(Dict[str, Any], result)

    def update_category(self, category_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a treasury category.

        Args:
            category_id: The category ID
            data: Updated category data

        Returns:
            The updated treasury category
        """
        result = self.client.put("treasury", "categories", category_id, data)
        return cast(Dict[str, Any], result)

    def delete_category(self, category_id: str) -> Dict[str, Any]:
        """
        Delete a treasury category.

        Args:
            category_id: The category ID

        Returns:
            The deletion response
        """
        result = self.client.delete("treasury", "categories", category_id)
        return cast(Dict[str, Any], result)