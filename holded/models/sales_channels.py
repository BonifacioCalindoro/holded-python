"""
Models for the Sales Channels API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams


class SalesChannelCreate(BaseModel):
    """Model for creating a sales channel."""
    
    name: str = Field(..., description="Sales channel name")
    description: Optional[str] = Field(default=None, description="Sales channel description")
    is_active: Optional[bool] = Field(default=None, description="Whether the sales channel is active")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class SalesChannelUpdate(BaseModel):
    """Model for updating a sales channel."""
    
    name: Optional[str] = Field(default=None, description="Sales channel name")
    description: Optional[str] = Field(default=None, description="Sales channel description")
    is_active: Optional[bool] = Field(default=None, description="Whether the sales channel is active")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class SalesChannel(SalesChannelCreate):
    """Sales channel model."""
    
    id: str = Field(..., description="Sales channel ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class SalesChannelListParams(PaginationParams):
    """Parameters for listing sales channels."""
    
    query: Optional[str] = Field(default=None, description="Search query")


# Response models
class SalesChannelResponse(BaseResponse, SalesChannel):
    """Response model for a single sales channel."""
    pass


class SalesChannelListResponse(BaseResponse):
    """Response model for a list of sales channels."""
    
    items: List[SalesChannel] = Field(..., description="List of sales channels")
    total: Optional[int] = Field(default=None, description="Total number of sales channels")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page") 