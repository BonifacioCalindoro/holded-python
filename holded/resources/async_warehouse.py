"""
Asynchronous warehouse resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import AsyncBaseResource


class AsyncWarehouseResource(AsyncBaseResource):
    """
    Resource for interacting with the Warehouse API asynchronously.
    """

    def __init__(self, client):
        """Initialize the warehouse resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "warehouse"

    async def list_warehouses(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all warehouses asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of warehouses.
        """
        result = await self.client.get(f"{self.base_path}/warehouses", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_warehouse(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new warehouse asynchronously.

        Args:
            data: Warehouse data.

        Returns:
            The created warehouse.
        """
        result = await self.client.post(f"{self.base_path}/warehouses", data=data)
        return cast(Dict[str, Any], result)

    async def get_warehouse(self, warehouse_id: str) -> Dict[str, Any]:
        """
        Get a specific warehouse asynchronously.

        Args:
            warehouse_id: The warehouse ID.

        Returns:
            The warehouse.
        """
        result = await self.client.get(f"{self.base_path}/warehouses/{warehouse_id}")
        return cast(Dict[str, Any], result)

    async def update_warehouse(self, warehouse_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a warehouse asynchronously.

        Args:
            warehouse_id: The warehouse ID.
            data: Updated warehouse data.

        Returns:
            The updated warehouse.
        """
        result = await self.client.put(f"{self.base_path}/warehouses/{warehouse_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_warehouse(self, warehouse_id: str) -> Dict[str, Any]:
        """
        Delete a warehouse asynchronously.

        Args:
            warehouse_id: The warehouse ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"{self.base_path}/warehouses/{warehouse_id}")
        return cast(Dict[str, Any], result)

    async def list_stock_adjustments(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all stock adjustments asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of stock adjustments.
        """
        result = await self.client.get(f"{self.base_path}/stockAdjustments", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_stock_adjustment(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new stock adjustment asynchronously.

        Args:
            data: Stock adjustment data.

        Returns:
            The created stock adjustment.
        """
        result = await self.client.post(f"{self.base_path}/stockAdjustments", data=data)
        return cast(Dict[str, Any], result)

    async def get_stock_adjustment(self, adjustment_id: str) -> Dict[str, Any]:
        """
        Get a specific stock adjustment asynchronously.

        Args:
            adjustment_id: The stock adjustment ID.

        Returns:
            The stock adjustment.
        """
        result = await self.client.get(f"{self.base_path}/stockAdjustments/{adjustment_id}")
        return cast(Dict[str, Any], result)

    async def update_stock_adjustment(self, adjustment_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a stock adjustment asynchronously.

        Args:
            adjustment_id: The stock adjustment ID.
            data: Updated stock adjustment data.

        Returns:
            The updated stock adjustment.
        """
        result = await self.client.put(f"{self.base_path}/stockAdjustments/{adjustment_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_stock_adjustment(self, adjustment_id: str) -> Dict[str, Any]:
        """
        Delete a stock adjustment asynchronously.

        Args:
            adjustment_id: The stock adjustment ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"{self.base_path}/stockAdjustments/{adjustment_id}")
        return cast(Dict[str, Any], result)

    async def list_stock_transfers(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all stock transfers asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of stock transfers.
        """
        result = await self.client.get("warehouse/stockTransfers", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_stock_transfer(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new stock transfer asynchronously.

        Args:
            data: Stock transfer data.

        Returns:
            The created stock transfer.
        """
        result = await self.client.post("warehouse/stockTransfers", data=data)
        return cast(Dict[str, Any], result)

    async def get_stock_transfer(self, transfer_id: str) -> Dict[str, Any]:
        """
        Get a specific stock transfer asynchronously.

        Args:
            transfer_id: The stock transfer ID.

        Returns:
            The stock transfer.
        """
        result = await self.client.get(f"warehouse/stockTransfers/{transfer_id}")
        return cast(Dict[str, Any], result)

    async def update_stock_transfer(self, transfer_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a stock transfer asynchronously.

        Args:
            transfer_id: The stock transfer ID.
            data: Updated stock transfer data.

        Returns:
            The updated stock transfer.
        """
        result = await self.client.put(f"warehouse/stockTransfers/{transfer_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_stock_transfer(self, transfer_id: str) -> Dict[str, Any]:
        """
        Delete a stock transfer asynchronously.

        Args:
            transfer_id: The stock transfer ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"warehouse/stockTransfers/{transfer_id}")
        return cast(Dict[str, Any], result)

    async def get_product_stock(self, product_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Get stock information for a specific product asynchronously.

        Args:
            product_id: The product ID
            params: Optional query parameters

        Returns:
            The product stock information
        """
        result = await self.client.get("warehouse", f"products/{product_id}/stock", params=params)
        return cast(Dict[str, Any], result)

    async def update_product_stock(self, product_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update stock information for a specific product asynchronously.

        Args:
            product_id: The product ID
            data: Updated stock information

        Returns:
            The updated product stock information
        """
        result = await self.client.put("warehouse", f"products/{product_id}/stock", data)
        return cast(Dict[str, Any], result) 