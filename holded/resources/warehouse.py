"""
Warehouse resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import BaseResource


class WarehouseResource(BaseResource):
    """
    Resource for interacting with the Warehouse API.
    """

    def list_warehouses(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all warehouses.

        Args:
            params: Optional query parameters.

        Returns:
            A list of warehouses.
        """
        result = self.client.get("warehouse/warehouses", params=params)
        return result

    def create_warehouse(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new warehouse.

        Args:
            data: Warehouse data.

        Returns:
            The created warehouse.
        """
        result = self.client.post("warehouse/warehouses", data=data)
        return result

    def get_warehouse(self, warehouse_id: str) -> Dict[str, Any]:
        """
        Get a specific warehouse.

        Args:
            warehouse_id: The warehouse ID.

        Returns:
            The warehouse.
        """
        result = self.client.get(f"warehouse/warehouses/{warehouse_id}")
        return result

    def update_warehouse(self, warehouse_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a warehouse.

        Args:
            warehouse_id: The warehouse ID.
            data: Updated warehouse data.

        Returns:
            The updated warehouse.
        """
        result = self.client.put(f"warehouse/warehouses/{warehouse_id}", data=data)
        return result

    def delete_warehouse(self, warehouse_id: str) -> Dict[str, Any]:
        """
        Delete a warehouse.

        Args:
            warehouse_id: The warehouse ID.

        Returns:
            A confirmation message.
        """
        result = self.client.delete(f"warehouse/warehouses/{warehouse_id}")
        return result

    def list_stock_adjustments(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all stock adjustments.

        Args:
            params: Optional query parameters.

        Returns:
            A list of stock adjustments.
        """
        result = self.client.get("warehouse/stockAdjustments", params=params)
        return result

    def create_stock_adjustment(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new stock adjustment.

        Args:
            data: Stock adjustment data.

        Returns:
            The created stock adjustment.
        """
        result = self.client.post("warehouse/stockAdjustments", data=data)
        return result

    def get_stock_adjustment(self, adjustment_id: str) -> Dict[str, Any]:
        """
        Get a specific stock adjustment.

        Args:
            adjustment_id: The stock adjustment ID.

        Returns:
            The stock adjustment.
        """
        result = self.client.get(f"warehouse/stockAdjustments/{adjustment_id}")
        return result

    def update_stock_adjustment(self, adjustment_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a stock adjustment.

        Args:
            adjustment_id: The stock adjustment ID.
            data: Updated stock adjustment data.

        Returns:
            The updated stock adjustment.
        """
        result = self.client.put(f"warehouse/stockAdjustments/{adjustment_id}", data=data)
        return result

    def delete_stock_adjustment(self, adjustment_id: str) -> Dict[str, Any]:
        """
        Delete a stock adjustment.

        Args:
            adjustment_id: The stock adjustment ID.

        Returns:
            A confirmation message.
        """
        result = self.client.delete(f"warehouse/stockAdjustments/{adjustment_id}")
        return result

    def list_stock_transfers(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all stock transfers.

        Args:
            params: Optional query parameters.

        Returns:
            A list of stock transfers.
        """
        result = self.client.get("warehouse/stockTransfers", params=params)
        return result

    def create_stock_transfer(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new stock transfer.

        Args:
            data: Stock transfer data.

        Returns:
            The created stock transfer.
        """
        result = self.client.post("warehouse/stockTransfers", data=data)
        return result

    def get_stock_transfer(self, transfer_id: str) -> Dict[str, Any]:
        """
        Get a specific stock transfer.

        Args:
            transfer_id: The stock transfer ID.

        Returns:
            The stock transfer.
        """
        result = self.client.get(f"warehouse/stockTransfers/{transfer_id}")
        return result

    def update_stock_transfer(self, transfer_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a stock transfer.

        Args:
            transfer_id: The stock transfer ID.
            data: Updated stock transfer data.

        Returns:
            The updated stock transfer.
        """
        result = self.client.put(f"warehouse/stockTransfers/{transfer_id}", data=data)
        return result

    def delete_stock_transfer(self, transfer_id: str) -> Dict[str, Any]:
        """
        Delete a stock transfer.

        Args:
            transfer_id: The stock transfer ID.

        Returns:
            A confirmation message.
        """
        result = self.client.delete(f"warehouse/stockTransfers/{transfer_id}")
        return result

    def get_product_stock(self, product_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Get stock information for a specific product.

        Args:
            product_id: The product ID
            params: Optional query parameters

        Returns:
            The product stock information
        """
        result = self.client.get("warehouse", f"products/{product_id}/stock", params=params)
        return cast(Dict[str, Any], result)

    def update_product_stock(self, product_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update stock information for a specific product.

        Args:
            product_id: The product ID
            data: Updated stock information

        Returns:
            The updated product stock information
        """
        result = self.client.put("warehouse", f"products/{product_id}/stock", data)
        return cast(Dict[str, Any], result) 