"""
Models for the Products API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams


class ProductVariant(BaseModel):
    """Product variant model."""
    
    id: Optional[str] = Field(default=None, description="Variant ID")
    name: str = Field(..., description="Variant name")
    sku: Optional[str] = Field(default=None, description="Stock Keeping Unit")
    price: Optional[float] = Field(default=None, description="Variant price")
    cost: Optional[float] = Field(default=None, description="Variant cost")
    stock: Optional[int] = Field(default=None, description="Variant stock quantity")


class ProductCreate(BaseModel):
    """Model for creating a product."""
    
    name: str = Field(..., description="Product name")
    description: Optional[str] = Field(default=None, description="Product description")
    reference: Optional[str] = Field(default=None, description="Product reference")
    price: Optional[float] = Field(default=None, description="Product price")
    cost: Optional[float] = Field(default=None, description="Product cost")
    tax: Optional[float] = Field(default=None, description="Product tax percentage")
    type: Optional[str] = Field(default=None, description="Product type")
    category_id: Optional[str] = Field(default=None, description="Category ID")
    variants: Optional[List[ProductVariant]] = Field(default=None, description="Product variants")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class ProductUpdate(BaseModel):
    """Model for updating a product."""
    
    name: Optional[str] = Field(default=None, description="Product name")
    description: Optional[str] = Field(default=None, description="Product description")
    reference: Optional[str] = Field(default=None, description="Product reference")
    price: Optional[float] = Field(default=None, description="Product price")
    cost: Optional[float] = Field(default=None, description="Product cost")
    tax: Optional[float] = Field(default=None, description="Product tax percentage")
    type: Optional[str] = Field(default=None, description="Product type")
    category_id: Optional[str] = Field(default=None, description="Category ID")
    variants: Optional[List[ProductVariant]] = Field(default=None, description="Product variants")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class Product(ProductCreate):
    """Product model."""
    
    id: str = Field(..., description="Product ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class ProductListParams(PaginationParams):
    """Parameters for listing products."""
    
    category_id: Optional[str] = Field(default=None, description="Filter by category ID")
    query: Optional[str] = Field(default=None, description="Search query")


class ProductCategoryCreate(BaseModel):
    """Model for creating a product category."""
    
    name: str = Field(..., description="Category name")
    parent_id: Optional[str] = Field(default=None, description="Parent category ID")


class ProductCategoryUpdate(BaseModel):
    """Model for updating a product category."""
    
    name: Optional[str] = Field(default=None, description="Category name")
    parent_id: Optional[str] = Field(default=None, description="Parent category ID")


class ProductCategory(ProductCategoryCreate):
    """Product category model."""
    
    id: str = Field(..., description="Category ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


# Response models
class ProductResponse(BaseResponse, Product):
    """Response model for a single product."""
    pass


class ProductListResponse(BaseResponse):
    """Response model for a list of products."""
    
    items: List[Product] = Field(..., description="List of products")
    total: Optional[int] = Field(default=None, description="Total number of products")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class ProductCategoryResponse(BaseResponse, ProductCategory):
    """Response model for a single product category."""
    pass


class ProductCategoryListResponse(BaseResponse):
    """Response model for a list of product categories."""
    
    items: List[ProductCategory] = Field(..., description="List of product categories")
    total: Optional[int] = Field(default=None, description="Total number of categories")


class ProductVariantResponse(BaseResponse, ProductVariant):
    """Response model for a single product variant."""
    pass


class ProductVariantListResponse(BaseResponse):
    """Response model for a list of product variants."""
    
    items: List[ProductVariant] = Field(..., description="List of product variants")
    total: Optional[int] = Field(default=None, description="Total number of variants") 