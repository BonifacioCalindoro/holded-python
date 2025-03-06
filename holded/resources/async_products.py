"""
Asynchronous products resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import AsyncBaseResource


class AsyncProductsResource(AsyncBaseResource):
    """
    Resource for interacting with the Products API asynchronously.
    """

    async def list(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all products asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of products
        """
        result = await self.client.get("invoicing", "products", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new product asynchronously.

        Args:
            data: Product data

        Returns:
            The created product
        """
        result = await self.client.post("invoicing", "products", data)
        return cast(Dict[str, Any], result)

    async def get(self, product_id: str) -> Dict[str, Any]:
        """
        Get a specific product asynchronously.

        Args:
            product_id: The product ID

        Returns:
            The product details
        """
        result = await self.client.get("invoicing", "products", product_id)
        return cast(Dict[str, Any], result)

    async def update(self, product_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a product asynchronously.

        Args:
            product_id: The product ID
            data: Updated product data

        Returns:
            The updated product
        """
        result = await self.client.put("invoicing", "products", product_id, data)
        return cast(Dict[str, Any], result)

    async def delete(self, product_id: str) -> Dict[str, Any]:
        """
        Delete a product asynchronously.

        Args:
            product_id: The product ID

        Returns:
            The deletion response
        """
        result = await self.client.delete("invoicing", "products", product_id)
        return cast(Dict[str, Any], result)

    async def list_categories(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all product categories asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of product categories
        """
        result = await self.client.get("invoicing", "products/categories", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_category(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new product category asynchronously.

        Args:
            data: Category data

        Returns:
            The created category
        """
        result = await self.client.post("invoicing", "products/categories", data)
        return cast(Dict[str, Any], result)

    async def update_category(self, category_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a product category asynchronously.

        Args:
            category_id: The category ID
            data: Updated category data

        Returns:
            The updated category
        """
        result = await self.client.put("invoicing", "products/categories", category_id, data)
        return cast(Dict[str, Any], result)

    async def delete_category(self, category_id: str) -> Dict[str, Any]:
        """
        Delete a product category asynchronously.

        Args:
            category_id: The category ID

        Returns:
            The deletion response
        """
        result = await self.client.delete("invoicing", "products/categories", category_id)
        return cast(Dict[str, Any], result)

    async def list_variants(self, product_id: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all variants for a specific product asynchronously.

        Args:
            product_id: The product ID
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of product variants
        """
        result = await self.client.get("invoicing", f"products/{product_id}/variants", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_variant(self, product_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new variant for a specific product asynchronously.

        Args:
            product_id: The product ID
            data: Variant data

        Returns:
            The created variant
        """
        result = await self.client.post("invoicing", f"products/{product_id}/variants", data)
        return cast(Dict[str, Any], result)

    async def update_variant(self, product_id: str, variant_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a variant for a specific product asynchronously.

        Args:
            product_id: The product ID
            variant_id: The variant ID
            data: Updated variant data

        Returns:
            The updated variant
        """
        result = await self.client.put("invoicing", f"products/{product_id}/variants", variant_id, data)
        return cast(Dict[str, Any], result)

    async def delete_variant(self, product_id: str, variant_id: str) -> Dict[str, Any]:
        """
        Delete a variant for a specific product asynchronously.

        Args:
            product_id: The product ID
            variant_id: The variant ID

        Returns:
            The deletion response
        """
        result = await self.client.delete("invoicing", f"products/{product_id}/variants", variant_id)
        return cast(Dict[str, Any], result)