"""
Base models for the Holded API.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel as PydanticBaseModel, Field, field_validator


class BaseModel(PydanticBaseModel):
    """Base model for all Holded API models."""
    
    class Config:
        """Pydantic configuration."""
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
        }


class BaseResponse(BaseModel):
    """Base response model for all Holded API responses."""
    
    # Some responses include a success field
    success: Optional[bool] = None


class PaginationParams(BaseModel):
    """Pagination parameters for list endpoints."""
    
    page: Optional[int] = Field(default=None, description="Page number")
    limit: Optional[int] = Field(default=None, description="Number of items per page")


class DateRangeParams(BaseModel):
    """Date range parameters for filtering by date."""
    
    start_date: Optional[datetime] = Field(default=None, description="Start date for filtering")
    end_date: Optional[datetime] = Field(default=None, description="End date for filtering")


class SortParams(BaseModel):
    """Sorting parameters."""
    
    sort_field: Optional[str] = Field(default=None, description="Field to sort by")
    sort_order: Optional[str] = Field(default=None, description="Sort order (asc or desc)")
    
    @field_validator('sort_order')
    def validate_sort_order(cls, v):
        """Validate sort order."""
        if v is not None and v not in ('asc', 'desc'):
            raise ValueError('sort_order must be either "asc" or "desc"')
        return v


class ErrorResponse(BaseModel):
    """Error response model."""
    
    message: str = Field(..., description="Error message")
    error: Optional[str] = Field(default=None, description="Error code")
    status: Optional[int] = Field(default=None, description="HTTP status code") 