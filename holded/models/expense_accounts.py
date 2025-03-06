"""
Models for the Expense Accounts API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams


class ExpenseAccountCreate(BaseModel):
    """Model for creating an expense account."""
    
    name: str = Field(..., description="Expense account name")
    description: Optional[str] = Field(default=None, description="Expense account description")
    accounting_account_id: Optional[str] = Field(default=None, description="Associated accounting account ID")
    is_active: Optional[bool] = Field(default=None, description="Whether the expense account is active")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class ExpenseAccountUpdate(BaseModel):
    """Model for updating an expense account."""
    
    name: Optional[str] = Field(default=None, description="Expense account name")
    description: Optional[str] = Field(default=None, description="Expense account description")
    accounting_account_id: Optional[str] = Field(default=None, description="Associated accounting account ID")
    is_active: Optional[bool] = Field(default=None, description="Whether the expense account is active")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class ExpenseAccount(ExpenseAccountCreate):
    """Expense account model."""
    
    id: str = Field(..., description="Expense account ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class ExpenseAccountListParams(PaginationParams):
    """Parameters for listing expense accounts."""
    
    query: Optional[str] = Field(default=None, description="Search query")


# Response models
class ExpenseAccountResponse(BaseResponse, ExpenseAccount):
    """Response model for a single expense account."""
    pass


class ExpenseAccountListResponse(BaseResponse):
    """Response model for a list of expense accounts."""
    
    items: List[ExpenseAccount] = Field(..., description="List of expense accounts")
    total: Optional[int] = Field(default=None, description="Total number of expense accounts")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page") 