"""
Models for the Numbering Series API.
"""
from datetime import datetime
from typing import List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse


class NumberingSeriesCreate(BaseModel):
    """Model for creating a numbering series."""
    
    name: str = Field(..., description="Numbering series name")
    type: str = Field(..., description="Document type (invoice, order, etc.)")
    prefix: Optional[str] = Field(default=None, description="Prefix for the numbering")
    suffix: Optional[str] = Field(default=None, description="Suffix for the numbering")
    next_number: int = Field(..., description="Next number in the series")
    padding: Optional[int] = Field(default=None, description="Padding for the number")
    is_default: Optional[bool] = Field(default=None, description="Whether this is the default series for the type")


class NumberingSeriesUpdate(BaseModel):
    """Model for updating a numbering series."""
    
    name: Optional[str] = Field(default=None, description="Numbering series name")
    prefix: Optional[str] = Field(default=None, description="Prefix for the numbering")
    suffix: Optional[str] = Field(default=None, description="Suffix for the numbering")
    next_number: Optional[int] = Field(default=None, description="Next number in the series")
    padding: Optional[int] = Field(default=None, description="Padding for the number")
    is_default: Optional[bool] = Field(default=None, description="Whether this is the default series for the type")


class NumberingSeries(NumberingSeriesCreate):
    """Numbering series model."""
    
    id: str = Field(..., description="Numbering series ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


# Response models
class NumberingSeriesResponse(BaseResponse, NumberingSeries):
    """Response model for a single numbering series."""
    pass


class NumberingSeriesListResponse(BaseResponse):
    """Response model for a list of numbering series."""
    
    items: List[NumberingSeries] = Field(..., description="List of numbering series")
    total: Optional[int] = Field(default=None, description="Total number of numbering series") 