#!/usr/bin/env python
"""
Example script demonstrating how to use the Holded API wrapper for products and inventory management.
"""
import os
import asyncio
from pprint import pprint

from holded.client import HoldedClient
from holded.async_client import AsyncHoldedClient
from holded.models.products import (
    ProductCreate, ProductUpdate, ProductVariant, ProductListParams,
    ProductCategoryCreate
)
from holded.models.warehouse import (
    WarehouseCreate, WarehouseStockUpdate, WarehouseStockMovementCreate
)
from holded.exceptions import HoldedError


def sync_example():
    """Example using the synchronous client."""
    # Get API key from environment variable
    api_key = os.environ.get("HOLDED_API_KEY")
    if not api_key:
        print("Please set the HOLDED_API_KEY environment variable.")
        return

    # Initialize the client
    client = HoldedClient(api_key=api_key)

    try:
        # Create a product category
        print("\n=== Creating a product category ===")
        category_data = ProductCategoryCreate(
            name="Example Category"
        )
        category = client.products.create_category(category_data)
        print(f"Created category: {category.get('name')} with ID: {category.get('id')}")

        # Create a product with variants
        print("\n=== Creating a product with variants ===")
        product_data = ProductCreate(
            name="Example Product",
            description="This is an example product with variants",
            reference="PROD-EXAMPLE-001",
            price=99.99,
            tax=21.0,
            category_id=category.get('id'),
            variants=[
                ProductVariant(
                    name="Small",
                    price=89.99,
                    sku="PROD-EXAMPLE-001-S"
                ),
                ProductVariant(
                    name="Medium",
                    price=99.99,
                    sku="PROD-EXAMPLE-001-M"
                ),
                ProductVariant(
                    name="Large",
                    price=109.99,
                    sku="PROD-EXAMPLE-001-L"
                )
            ]
        )
        product = client.products.create(product_data)
        print(f"Created product: {product.get('name')} with ID: {product.get('id')}")

        # Get the product details
        print("\n=== Getting product details ===")
        product_details = client.products.get(product.get('id'))
        print(f"Product details:")
        pprint(product_details)

        # List products with filtering
        print("\n=== Listing products ===")
        params = ProductListParams(
            page=1,
            limit=5,
            category_id=category.get('id')
        )
        products = client.products.list(params)
        print(f"Found {len(products.items)} products in the category:")
        for prod in products.items:
            print(f"- {prod.name} (ID: {prod.id}, Price: {prod.price})")

        # Create a warehouse
        print("\n=== Creating a warehouse ===")
        warehouse_data = WarehouseCreate(
            name="Example Warehouse",
            address="123 Example Street",
            city="Example City",
            postal_code="12345",
            country="Example Country"
        )
        warehouse = client.warehouse.create(warehouse_data)
        print(f"Created warehouse: {warehouse.get('name')} with ID: {warehouse.get('id')}")

        # Update product stock
        print("\n=== Updating product stock ===")
        stock_data = WarehouseStockUpdate(
            product_id=product.get('id'),
            warehouse_id=warehouse.get('id'),
            quantity=100,
            notes="Initial stock"
        )
        stock_result = client.warehouse.update_stock(stock_data)
        print(f"Updated stock: {stock_result}")

        # Create a stock movement
        print("\n=== Creating a stock movement ===")
        movement_data = WarehouseStockMovementCreate(
            product_id=product.get('id'),
            warehouse_id=warehouse.get('id'),
            quantity=10,
            type="out",
            date="2023-01-01T00:00:00Z",
            notes="Example stock movement"
        )
        movement = client.warehouse.create_stock_movement(movement_data)
        print(f"Created stock movement with ID: {movement.get('id')}")

        # List stock for the product
        print("\n=== Listing product stock ===")
        stock = client.warehouse.list_stock(product_id=product.get('id'))
        print(f"Product stock:")
        pprint(stock)

        # Update the product
        print("\n=== Updating product ===")
        update_data = ProductUpdate(
            name="Updated Example Product",
            description="This is an updated example product"
        )
        updated_product = client.products.update(product.get('id'), update_data)
        print(f"Updated product: {updated_product.get('name')}")

        # Clean up - delete the product, category, and warehouse
        print("\n=== Cleaning up ===")
        client.products.delete(product.get('id'))
        print(f"Deleted product")
        client.products.delete_category(category.get('id'))
        print(f"Deleted category")
        client.warehouse.delete(warehouse.get('id'))
        print(f"Deleted warehouse")

    except HoldedError as e:
        print(f"Error: {e.message}")
        if hasattr(e, 'error_data') and e.error_data:
            print(f"Error data: {e.error_data}")
    finally:
        client.close()


async def async_example():
    """Example using the asynchronous client."""
    # Get API key from environment variable
    api_key = os.environ.get("HOLDED_API_KEY")
    if not api_key:
        print("Please set the HOLDED_API_KEY environment variable.")
        return

    # Initialize the client
    client = AsyncHoldedClient(api_key=api_key)

    try:
        # Create a product category
        print("\n=== Creating a product category (async) ===")
        category_data = ProductCategoryCreate(
            name="Async Example Category"
        )
        category = await client.products.create_category(category_data)
        print(f"Created category: {category.get('name')} with ID: {category.get('id')}")

        # Create a product
        print("\n=== Creating a product (async) ===")
        product_data = ProductCreate(
            name="Async Example Product",
            description="This is an async example product",
            reference="ASYNC-PROD-001",
            price=79.99,
            tax=21.0,
            category_id=category.get('id')
        )
        product = await client.products.create(product_data)
        print(f"Created product: {product.get('name')} with ID: {product.get('id')}")

        # Get the product details
        print("\n=== Getting product details (async) ===")
        product_details = await client.products.get(product.get('id'))
        print(f"Product details:")
        pprint(product_details)

        # Clean up - delete the product and category
        print("\n=== Cleaning up (async) ===")
        await client.products.delete(product.get('id'))
        print(f"Deleted product")
        await client.products.delete_category(category.get('id'))
        print(f"Deleted category")

    except HoldedError as e:
        print(f"Error: {e.message}")
        if hasattr(e, 'error_data') and e.error_data:
            print(f"Error data: {e.error_data}")
    finally:
        await client.close()


if __name__ == "__main__":
    print("Running synchronous example...")
    sync_example()
    
    print("\nRunning asynchronous example...")
    asyncio.run(async_example()) 