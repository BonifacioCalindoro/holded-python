"""
Models for the Products API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from enum import Enum

from pydantic import Field, field_validator

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class ProductType(str, Enum):
    """Product type enum."""
    PRODUCT = "product"
    SERVICE = "service"
    SUBSCRIPTION = "subscription"
    BUNDLE = "bundle"


class ProductStatus(str, Enum):
    """Product status enum."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    DISCONTINUED = "discontinued"


class StockManagement(str, Enum):
    """Stock management type enum."""
    SIMPLE = "simple"
    VARIANTS = "variants"
    NONE = "none"


class ProductImage(BaseModel):
    """Product image model."""
    
    id: Optional[str] = Field(default=None, description="Image ID")
    url: str = Field(..., description="Image URL")
    is_primary: Optional[bool] = Field(default=False, description="Whether this is the primary image")
    position: Optional[int] = Field(default=0, description="Image position in the gallery")
    alt_text: Optional[str] = Field(default=None, description="Alternative text for the image")


class ProductVariantAttribute(BaseModel):
    """Product variant attribute model."""
    
    name: str = Field(..., description="Attribute name (e.g., 'Color', 'Size')")
    value: str = Field(..., description="Attribute value (e.g., 'Red', 'XL')")


class ProductVariant(BaseModel):
    """Product variant model."""
    
    id: Optional[str] = Field(default=None, description="Variant ID")
    name: str = Field(..., description="Variant name")
    sku: Optional[str] = Field(default=None, description="Stock Keeping Unit")
    barcode: Optional[str] = Field(default=None, description="Barcode (EAN, UPC, etc.)")
    price: Optional[float] = Field(default=None, description="Variant price")
    cost: Optional[float] = Field(default=None, description="Variant cost")
    stock: Optional[int] = Field(default=None, description="Variant stock quantity")
    min_stock: Optional[int] = Field(default=None, description="Minimum stock level")
    weight: Optional[float] = Field(default=None, description="Weight in kg")
    dimensions: Optional[Dict[str, float]] = Field(default=None, description="Dimensions (length, width, height)")
    attributes: Optional[List[ProductVariantAttribute]] = Field(default=None, description="Variant attributes")
    images: Optional[List[ProductImage]] = Field(default=None, description="Variant images")
    is_default: Optional[bool] = Field(default=False, description="Whether this is the default variant")


class ProductTax(BaseModel):
    """Product tax model."""
    
    id: Optional[str] = Field(default=None, description="Tax ID")
    name: Optional[str] = Field(default=None, description="Tax name")
    rate: float = Field(..., description="Tax rate percentage")


class ProductSupplier(BaseModel):
    """Product supplier model."""
    
    id: str = Field(..., description="Supplier ID (contact ID)")
    name: Optional[str] = Field(default=None, description="Supplier name")
    reference: Optional[str] = Field(default=None, description="Supplier's reference for this product")
    cost: Optional[float] = Field(default=None, description="Cost from this supplier")
    is_preferred: Optional[bool] = Field(default=False, description="Whether this is the preferred supplier")
    lead_time: Optional[int] = Field(default=None, description="Lead time in days")
    min_order_quantity: Optional[int] = Field(default=None, description="Minimum order quantity")


class ProductWarehouse(BaseModel):
    """Product warehouse stock model."""
    
    warehouse_id: str = Field(..., description="Warehouse ID")
    warehouse_name: Optional[str] = Field(default=None, description="Warehouse name")
    stock: int = Field(..., description="Stock quantity in this warehouse")
    min_stock: Optional[int] = Field(default=None, description="Minimum stock level for this warehouse")
    location: Optional[str] = Field(default=None, description="Location within the warehouse")


class ProductCreate(BaseModel):
    """Model for creating a product."""
    
    name: str = Field(..., description="Product name")
    description: Optional[str] = Field(default=None, description="Product description")
    reference: Optional[str] = Field(default=None, description="Product reference")
    sku: Optional[str] = Field(default=None, description="Stock Keeping Unit")
    barcode: Optional[str] = Field(default=None, description="Barcode (EAN, UPC, etc.)")
    price: Optional[float] = Field(default=None, description="Product price")
    cost: Optional[float] = Field(default=None, description="Product cost")
    tax: Optional[Union[float, ProductTax]] = Field(default=None, description="Product tax percentage or tax object")
    type: Optional[ProductType] = Field(default=ProductType.PRODUCT, description="Product type")
    status: Optional[ProductStatus] = Field(default=ProductStatus.ACTIVE, description="Product status")
    category_id: Optional[str] = Field(default=None, description="Category ID")
    stock_management: Optional[StockManagement] = Field(default=StockManagement.SIMPLE, description="Stock management type")
    stock: Optional[int] = Field(default=None, description="Stock quantity (for simple stock management)")
    min_stock: Optional[int] = Field(default=None, description="Minimum stock level")
    variants: Optional[List[ProductVariant]] = Field(default=None, description="Product variants")
    images: Optional[List[ProductImage]] = Field(default=None, description="Product images")
    suppliers: Optional[List[ProductSupplier]] = Field(default=None, description="Product suppliers")
    warehouses: Optional[List[ProductWarehouse]] = Field(default=None, description="Product warehouse stock")
    weight: Optional[float] = Field(default=None, description="Weight in kg")
    dimensions: Optional[Dict[str, float]] = Field(default=None, description="Dimensions (length, width, height)")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    tags: Optional[List[str]] = Field(default=None, description="Product tags")
    brand: Optional[str] = Field(default=None, description="Product brand")
    manufacturer: Optional[str] = Field(default=None, description="Product manufacturer")
    is_sellable: Optional[bool] = Field(default=True, description="Whether the product can be sold")
    is_purchasable: Optional[bool] = Field(default=True, description="Whether the product can be purchased")
    sales_account_id: Optional[str] = Field(default=None, description="Sales account ID")
    purchase_account_id: Optional[str] = Field(default=None, description="Purchase account ID")
    
    @field_validator('variants')
    def validate_variants(cls, v, values):
        """Validate variants based on stock management type."""
        if v and 'stock_management' in values.data and values.data['stock_management'] != StockManagement.VARIANTS:
            raise ValueError("Variants can only be defined when stock_management is 'variants'")
        return v


class ProductUpdate(BaseModel):
    """Model for updating a product."""
    
    name: Optional[str] = Field(default=None, description="Product name")
    description: Optional[str] = Field(default=None, description="Product description")
    reference: Optional[str] = Field(default=None, description="Product reference")
    sku: Optional[str] = Field(default=None, description="Stock Keeping Unit")
    barcode: Optional[str] = Field(default=None, description="Barcode (EAN, UPC, etc.)")
    price: Optional[float] = Field(default=None, description="Product price")
    cost: Optional[float] = Field(default=None, description="Product cost")
    tax: Optional[Union[float, ProductTax]] = Field(default=None, description="Product tax percentage or tax object")
    type: Optional[ProductType] = Field(default=None, description="Product type")
    status: Optional[ProductStatus] = Field(default=None, description="Product status")
    category_id: Optional[str] = Field(default=None, description="Category ID")
    stock_management: Optional[StockManagement] = Field(default=None, description="Stock management type")
    stock: Optional[int] = Field(default=None, description="Stock quantity (for simple stock management)")
    min_stock: Optional[int] = Field(default=None, description="Minimum stock level")
    variants: Optional[List[ProductVariant]] = Field(default=None, description="Product variants")
    images: Optional[List[ProductImage]] = Field(default=None, description="Product images")
    suppliers: Optional[List[ProductSupplier]] = Field(default=None, description="Product suppliers")
    warehouses: Optional[List[ProductWarehouse]] = Field(default=None, description="Product warehouse stock")
    weight: Optional[float] = Field(default=None, description="Weight in kg")
    dimensions: Optional[Dict[str, float]] = Field(default=None, description="Dimensions (length, width, height)")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    tags: Optional[List[str]] = Field(default=None, description="Product tags")
    brand: Optional[str] = Field(default=None, description="Product brand")
    manufacturer: Optional[str] = Field(default=None, description="Product manufacturer")
    is_sellable: Optional[bool] = Field(default=None, description="Whether the product can be sold")
    is_purchasable: Optional[bool] = Field(default=None, description="Whether the product can be purchased")
    sales_account_id: Optional[str] = Field(default=None, description="Sales account ID")
    purchase_account_id: Optional[str] = Field(default=None, description="Purchase account ID")


class Product(BaseModel):
    """Product model."""
    
    id: str = Field(..., description="Product ID")
    name: str = Field(..., description="Product name")
    description: Optional[str] = Field(default=None, description="Product description")
    reference: Optional[str] = Field(default=None, description="Product reference")
    sku: Optional[str] = Field(default=None, description="Stock Keeping Unit")
    barcode: Optional[str] = Field(default=None, description="Barcode (EAN, UPC, etc.)")
    price: float = Field(..., description="Product price")
    cost: Optional[float] = Field(default=None, description="Product cost")
    tax: Union[float, ProductTax] = Field(..., description="Product tax percentage or tax object")
    type: ProductType = Field(..., description="Product type")
    status: ProductStatus = Field(..., description="Product status")
    category_id: Optional[str] = Field(default=None, description="Category ID")
    category_name: Optional[str] = Field(default=None, description="Category name")
    stock_management: StockManagement = Field(..., description="Stock management type")
    stock: Optional[int] = Field(default=None, description="Stock quantity (for simple stock management)")
    min_stock: Optional[int] = Field(default=None, description="Minimum stock level")
    variants: Optional[List[ProductVariant]] = Field(default=None, description="Product variants")
    images: Optional[List[ProductImage]] = Field(default=None, description="Product images")
    suppliers: Optional[List[ProductSupplier]] = Field(default=None, description="Product suppliers")
    warehouses: Optional[List[ProductWarehouse]] = Field(default=None, description="Product warehouse stock")
    weight: Optional[float] = Field(default=None, description="Weight in kg")
    dimensions: Optional[Dict[str, float]] = Field(default=None, description="Dimensions (length, width, height)")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    tags: Optional[List[str]] = Field(default=None, description="Product tags")
    brand: Optional[str] = Field(default=None, description="Product brand")
    manufacturer: Optional[str] = Field(default=None, description="Product manufacturer")
    is_sellable: bool = Field(..., description="Whether the product can be sold")
    is_purchasable: bool = Field(..., description="Whether the product can be purchased")
    sales_account_id: Optional[str] = Field(default=None, description="Sales account ID")
    purchase_account_id: Optional[str] = Field(default=None, description="Purchase account ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")
    sales_count: Optional[int] = Field(default=None, description="Number of sales")
    purchase_count: Optional[int] = Field(default=None, description="Number of purchases")


class ProductListParams(PaginationParams, DateRangeParams):
    """Parameters for listing products."""
    
    category_id: Optional[str] = Field(default=None, description="Filter by category ID")
    type: Optional[ProductType] = Field(default=None, description="Filter by product type")
    status: Optional[ProductStatus] = Field(default=None, description="Filter by product status")
    query: Optional[str] = Field(default=None, description="Search query")
    tags: Optional[List[str]] = Field(default=None, description="Filter by tags")
    min_price: Optional[float] = Field(default=None, description="Filter by minimum price")
    max_price: Optional[float] = Field(default=None, description="Filter by maximum price")
    min_stock: Optional[int] = Field(default=None, description="Filter by minimum stock")
    max_stock: Optional[int] = Field(default=None, description="Filter by maximum stock")
    is_sellable: Optional[bool] = Field(default=None, description="Filter by sellable status")
    is_purchasable: Optional[bool] = Field(default=None, description="Filter by purchasable status")
    has_variants: Optional[bool] = Field(default=None, description="Filter by whether the product has variants")
    supplier_id: Optional[str] = Field(default=None, description="Filter by supplier ID")
    warehouse_id: Optional[str] = Field(default=None, description="Filter by warehouse ID")


class ProductCategoryCreate(BaseModel):
    """Model for creating a product category."""
    
    name: str = Field(..., description="Category name")
    parent_id: Optional[str] = Field(default=None, description="Parent category ID")
    description: Optional[str] = Field(default=None, description="Category description")
    image_url: Optional[str] = Field(default=None, description="Category image URL")
    is_active: Optional[bool] = Field(default=True, description="Whether the category is active")


class ProductCategoryUpdate(BaseModel):
    """Model for updating a product category."""
    
    name: Optional[str] = Field(default=None, description="Category name")
    parent_id: Optional[str] = Field(default=None, description="Parent category ID")
    description: Optional[str] = Field(default=None, description="Category description")
    image_url: Optional[str] = Field(default=None, description="Category image URL")
    is_active: Optional[bool] = Field(default=None, description="Whether the category is active")


class ProductCategory(BaseModel):
    """Product category model."""
    
    id: str = Field(..., description="Category ID")
    name: str = Field(..., description="Category name")
    parent_id: Optional[str] = Field(default=None, description="Parent category ID")
    parent_name: Optional[str] = Field(default=None, description="Parent category name")
    description: Optional[str] = Field(default=None, description="Category description")
    image_url: Optional[str] = Field(default=None, description="Category image URL")
    is_active: bool = Field(..., description="Whether the category is active")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")
    product_count: Optional[int] = Field(default=None, description="Number of products in this category")
    subcategories: Optional[List['ProductCategory']] = Field(default=None, description="Subcategories")


class ProductCategoryListParams(PaginationParams):
    """Parameters for listing product categories."""
    
    parent_id: Optional[str] = Field(default=None, description="Filter by parent category ID")
    is_active: Optional[bool] = Field(default=None, description="Filter by active status")
    query: Optional[str] = Field(default=None, description="Search query")
    include_subcategories: Optional[bool] = Field(default=False, description="Whether to include subcategories in the response")


class ProductStockAdjustment(BaseModel):
    """Model for adjusting product stock."""
    
    quantity: int = Field(..., description="Quantity to adjust (positive for increase, negative for decrease)")
    reason: Optional[str] = Field(default=None, description="Reason for the adjustment")
    warehouse_id: Optional[str] = Field(default=None, description="Warehouse ID")
    variant_id: Optional[str] = Field(default=None, description="Variant ID (for variant products)")
    date: Optional[datetime] = Field(default=None, description="Adjustment date")
    notes: Optional[str] = Field(default=None, description="Additional notes")


class ProductImageUpload(BaseModel):
    """Parameters for uploading a product image."""
    
    file: str = Field(..., description="Base64 encoded image content")
    is_primary: Optional[bool] = Field(default=False, description="Whether this is the primary image")
    position: Optional[int] = Field(default=0, description="Image position in the gallery")
    alt_text: Optional[str] = Field(default=None, description="Alternative text for the image")


class ProductImport(BaseModel):
    """Parameters for importing products."""
    
    file: str = Field(..., description="Base64 encoded CSV or Excel file content")
    file_type: str = Field(..., description="File type (csv, xlsx)")
    column_mapping: Dict[str, str] = Field(..., description="Mapping of file columns to product fields")
    skip_first_row: Optional[bool] = Field(default=True, description="Whether to skip the first row (header)")


# Response models
class ProductResponse(BaseResponse):
    """Response model for a single product."""
    
    product: Product = Field(..., description="Product data")


class ProductListResponse(BaseResponse):
    """Response model for a list of products."""
    
    items: List[Product] = Field(..., description="List of products")
    total: Optional[int] = Field(default=None, description="Total number of products")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class ProductCategoryResponse(BaseResponse):
    """Response model for a single product category."""
    
    category: ProductCategory = Field(..., description="Category data")


class ProductCategoryListResponse(BaseResponse):
    """Response model for a list of product categories."""
    
    items: List[ProductCategory] = Field(..., description="List of product categories")
    total: Optional[int] = Field(default=None, description="Total number of categories")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class ProductVariantResponse(BaseResponse):
    """Response model for a single product variant."""
    
    variant: ProductVariant = Field(..., description="Variant data")


class ProductVariantListResponse(BaseResponse):
    """Response model for a list of product variants."""
    
    items: List[ProductVariant] = Field(..., description="List of product variants")
    total: Optional[int] = Field(default=None, description="Total number of variants")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class ProductStockAdjustmentResponse(BaseResponse):
    """Response model for a stock adjustment."""
    
    previous_stock: int = Field(..., description="Previous stock quantity")
    new_stock: int = Field(..., description="New stock quantity")
    adjustment: int = Field(..., description="Adjustment amount")


class ProductImageResponse(BaseResponse):
    """Response model for a product image."""
    
    image: ProductImage = Field(..., description="Image data")


class ProductImageListResponse(BaseResponse):
    """Response model for a list of product images."""
    
    items: List[ProductImage] = Field(..., description="List of images")
    total: Optional[int] = Field(default=None, description="Total number of images")


class ProductImportResponse(BaseResponse):
    """Response model for importing products."""
    
    imported: int = Field(..., description="Number of products imported")
    errors: Optional[List[Dict[str, Any]]] = Field(default=None, description="Import errors")
    message: Optional[str] = Field(default=None, description="Response message") 