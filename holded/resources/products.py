"""
Products resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import BaseResource


class ProductsResource(BaseResource):
    """
    Resource for interacting with the Products API.
    """

    def list(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all products.

        Args:
            params: Optional query parameters.

        Returns:
            A list of products.
        """
        result = self.client.get("invoicing/products", params=params)
        return result

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new product.

        Args:
            data: Product data.

        Returns:
            The created product.
        """
        result = self.client.post("invoicing/products", data=data)
        return result

    def get(self, product_id: str) -> Dict[str, Any]:
        """
        Get a specific product.

        Args:
            product_id: The product ID.

        Returns:
            The product.
        """
        result = self.client.get(f"invoicing/products/{product_id}")
        return result

    def update(self, product_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a product.

        Args:
            product_id: The product ID.
            data: Updated product data.

        Returns:
            The updated product.
        """
        result = self.client.put(f"invoicing/products/{product_id}", data=data)
        return result

    def delete(self, product_id: str) -> Dict[str, Any]:
        """
        Delete a product.

        Args:
            product_id: The product ID.

        Returns:
            A confirmation message.
        """
        result = self.client.delete(f"invoicing/products/{product_id}")
        return result

    def list_categories(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all product categories.

        Args:
            params: Optional query parameters.

        Returns:
            A list of product categories.
        """
        result = self.client.get("invoicing/products/categories", params=params)
        return result

    def create_category(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new product category.

        Args:
            data: Category data.

        Returns:
            The created category.
        """
        result = self.client.post("invoicing/products/categories", data=data)
        return result

    def update_category(self, category_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a product category.

        Args:
            category_id: The category ID.
            data: Updated category data.

        Returns:
            The updated category.
        """
        result = self.client.put(f"invoicing/products/categories/{category_id}", data=data)
        return result

    def delete_category(self, category_id: str) -> Dict[str, Any]:
        """
        Delete a product category.

        Args:
            category_id: The category ID.

        Returns:
            A confirmation message.
        """
        result = self.client.delete(f"invoicing/products/categories/{category_id}")
        return result

    def list_variants(self, product_id: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all variants for a specific product.

        Args:
            product_id: The product ID
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of product variants
        """
        result = self.client.get("invoicing", f"products/{product_id}/variants", params=params)
        return cast(List[Dict[str, Any]], result)

    def create_variant(self, product_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new variant for a specific product.

        Args:
            product_id: The product ID
            data: Variant data

        Returns:
            The created variant
        """
        result = self.client.post("invoicing", f"products/{product_id}/variants", data)
        return cast(Dict[str, Any], result)

    def update_variant(self, product_id: str, variant_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a variant for a specific product.

        Args:
            product_id: The product ID
            variant_id: The variant ID
            data: Updated variant data

        Returns:
            The updated variant
        """
        result = self.client.put("invoicing", f"products/{product_id}/variants", variant_id, data)
        return cast(Dict[str, Any], result)

    def delete_variant(self, product_id: str, variant_id: str) -> Dict[str, Any]:
        """
        Delete a variant for a specific product.

        Args:
            product_id: The product ID
            variant_id: The variant ID

        Returns:
            The deletion response
        """
        result = self.client.delete("invoicing", f"products/{product_id}/variants", variant_id)
        return cast(Dict[str, Any], result)