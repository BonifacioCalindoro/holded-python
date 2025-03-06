"""
Models for the Warehouse API.
"""
from datetime import datetime
from typing import List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class WarehouseCreate(BaseModel):
    """Model for creating a warehouse."""
    
    name: str = Field(..., description="Warehouse name")
    address: Optional[str] = Field(default=None, description="Warehouse address")
    city: Optional[str] = Field(default=None, description="Warehouse city")
    postal_code: Optional[str] = Field(default=None, description="Warehouse postal code")
    province: Optional[str] = Field(default=None, description="Warehouse province or state")
    country: Optional[str] = Field(default=None, description="Warehouse country")
    notes: Optional[str] = Field(default=None, description="Warehouse notes")
    is_default: Optional[bool] = Field(default=None, description="Whether this is the default warehouse")


class WarehouseUpdate(BaseModel):
    """Model for updating a warehouse."""
    
    name: Optional[str] = Field(default=None, description="Warehouse name")
    address: Optional[str] = Field(default=None, description="Warehouse address")
    city: Optional[str] = Field(default=None, description="Warehouse city")
    postal_code: Optional[str] = Field(default=None, description="Warehouse postal code")
    province: Optional[str] = Field(default=None, description="Warehouse province or state")
    country: Optional[str] = Field(default=None, description="Warehouse country")
    notes: Optional[str] = Field(default=None, description="Warehouse notes")
    is_default: Optional[bool] = Field(default=None, description="Whether this is the default warehouse")


class Warehouse(WarehouseCreate):
    """Warehouse model."""
    
    id: str = Field(..., description="Warehouse ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class WarehouseListParams(PaginationParams):
    """Parameters for listing warehouses."""
    
    query: Optional[str] = Field(default=None, description="Search query")


class WarehouseStockItem(BaseModel):
    """Warehouse stock item model."""
    
    product_id: str = Field(..., description="Product ID")
    warehouse_id: str = Field(..., description="Warehouse ID")
    quantity: float = Field(..., description="Stock quantity")
    variant_id: Optional[str] = Field(default=None, description="Variant ID if applicable")


class WarehouseStockUpdate(BaseModel):
    """Model for updating warehouse stock."""
    
    product_id: str = Field(..., description="Product ID")
    warehouse_id: str = Field(..., description="Warehouse ID")
    quantity: float = Field(..., description="New stock quantity")
    variant_id: Optional[str] = Field(default=None, description="Variant ID if applicable")
    notes: Optional[str] = Field(default=None, description="Stock update notes")


class WarehouseStockMovement(BaseModel):
    """Warehouse stock movement model."""
    
    id: str = Field(..., description="Movement ID")
    product_id: str = Field(..., description="Product ID")
    warehouse_id: str = Field(..., description="Warehouse ID")
    quantity: float = Field(..., description="Movement quantity")
    type: str = Field(..., description="Movement type (in, out)")
    date: datetime = Field(..., description="Movement date")
    notes: Optional[str] = Field(default=None, description="Movement notes")
    document_id: Optional[str] = Field(default=None, description="Related document ID")
    variant_id: Optional[str] = Field(default=None, description="Variant ID if applicable")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")


class WarehouseStockMovementCreate(BaseModel):
    """Model for creating a warehouse stock movement."""
    
    product_id: str = Field(..., description="Product ID")
    warehouse_id: str = Field(..., description="Warehouse ID")
    quantity: float = Field(..., description="Movement quantity")
    type: str = Field(..., description="Movement type (in, out)")
    date: datetime = Field(..., description="Movement date")
    notes: Optional[str] = Field(default=None, description="Movement notes")
    document_id: Optional[str] = Field(default=None, description="Related document ID")
    variant_id: Optional[str] = Field(default=None, description="Variant ID if applicable")


class WarehouseStockMovementListParams(PaginationParams, DateRangeParams):
    """Parameters for listing warehouse stock movements."""
    
    product_id: Optional[str] = Field(default=None, description="Filter by product ID")
    warehouse_id: Optional[str] = Field(default=None, description="Filter by warehouse ID")
    type: Optional[str] = Field(default=None, description="Filter by movement type")
    variant_id: Optional[str] = Field(default=None, description="Filter by variant ID")


# Response models
class WarehouseResponse(BaseResponse, Warehouse):
    """Response model for a single warehouse."""
    pass


class WarehouseListResponse(BaseResponse):
    """Response model for a list of warehouses."""
    
    items: List[Warehouse] = Field(..., description="List of warehouses")
    total: Optional[int] = Field(default=None, description="Total number of warehouses")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class WarehouseStockItemResponse(BaseResponse, WarehouseStockItem):
    """Response model for a single warehouse stock item."""
    pass


class WarehouseStockListResponse(BaseResponse):
    """Response model for a list of warehouse stock items."""
    
    items: List[WarehouseStockItem] = Field(..., description="List of stock items")
    total: Optional[int] = Field(default=None, description="Total number of stock items")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class WarehouseStockMovementResponse(BaseResponse, WarehouseStockMovement):
    """Response model for a single warehouse stock movement."""
    pass


class WarehouseStockMovementListResponse(BaseResponse):
    """Response model for a list of warehouse stock movements."""
    
    items: List[WarehouseStockMovement] = Field(..., description="List of stock movements")
    total: Optional[int] = Field(default=None, description="Total number of stock movements")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page") 