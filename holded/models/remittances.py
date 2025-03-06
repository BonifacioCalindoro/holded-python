"""
Models for the Remittances API.
"""
from datetime import datetime
from typing import List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class RemittanceItem(BaseModel):
    """Remittance item model."""
    
    document_id: str = Field(..., description="Document ID")
    amount: float = Field(..., description="Amount")
    due_date: datetime = Field(..., description="Due date")
    notes: Optional[str] = Field(default=None, description="Notes")


class Remittance(BaseModel):
    """Remittance model."""
    
    id: str = Field(..., description="Remittance ID")
    date: datetime = Field(..., description="Remittance date")
    reference: Optional[str] = Field(default=None, description="Remittance reference")
    bank_account_id: str = Field(..., description="Bank account ID")
    total_amount: float = Field(..., description="Total amount")
    status: str = Field(..., description="Remittance status")
    items: List[RemittanceItem] = Field(..., description="Remittance items")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class RemittanceListParams(PaginationParams, DateRangeParams):
    """Parameters for listing remittances."""
    
    status: Optional[str] = Field(default=None, description="Filter by status")
    bank_account_id: Optional[str] = Field(default=None, description="Filter by bank account ID")
    query: Optional[str] = Field(default=None, description="Search query")


# Response models
class RemittanceResponse(BaseResponse, Remittance):
    """Response model for a single remittance."""
    pass


class RemittanceListResponse(BaseResponse):
    """Response model for a list of remittances."""
    
    items: List[Remittance] = Field(..., description="List of remittances")
    total: Optional[int] = Field(default=None, description="Total number of remittances")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page") 