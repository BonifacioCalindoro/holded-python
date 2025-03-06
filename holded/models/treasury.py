"""
Models for the Treasury API.
"""
from datetime import datetime
from typing import List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class TreasuryAccountCreate(BaseModel):
    """Model for creating a treasury account."""
    
    name: str = Field(..., description="Account name")
    type: str = Field(..., description="Account type (bank, cash, etc.)")
    currency: Optional[str] = Field(default=None, description="Account currency")
    initial_balance: Optional[float] = Field(default=None, description="Initial balance")
    notes: Optional[str] = Field(default=None, description="Account notes")
    is_default: Optional[bool] = Field(default=None, description="Whether this is the default account")


class TreasuryAccountUpdate(BaseModel):
    """Model for updating a treasury account."""
    
    name: Optional[str] = Field(default=None, description="Account name")
    type: Optional[str] = Field(default=None, description="Account type (bank, cash, etc.)")
    currency: Optional[str] = Field(default=None, description="Account currency")
    initial_balance: Optional[float] = Field(default=None, description="Initial balance")
    notes: Optional[str] = Field(default=None, description="Account notes")
    is_default: Optional[bool] = Field(default=None, description="Whether this is the default account")


class TreasuryAccount(TreasuryAccountCreate):
    """Treasury account model."""
    
    id: str = Field(..., description="Account ID")
    balance: float = Field(..., description="Current balance")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class TreasuryAccountListParams(PaginationParams):
    """Parameters for listing treasury accounts."""
    
    type: Optional[str] = Field(default=None, description="Filter by account type")
    query: Optional[str] = Field(default=None, description="Search query")


class TreasuryTransactionCreate(BaseModel):
    """Model for creating a treasury transaction."""
    
    account_id: str = Field(..., description="Account ID")
    date: datetime = Field(..., description="Transaction date")
    amount: float = Field(..., description="Transaction amount")
    concept: str = Field(..., description="Transaction concept/description")
    notes: Optional[str] = Field(default=None, description="Transaction notes")
    category_id: Optional[str] = Field(default=None, description="Category ID")
    document_id: Optional[str] = Field(default=None, description="Related document ID")
    contact_id: Optional[str] = Field(default=None, description="Related contact ID")
    is_reconciled: Optional[bool] = Field(default=None, description="Whether the transaction is reconciled")


class TreasuryTransactionUpdate(BaseModel):
    """Model for updating a treasury transaction."""
    
    account_id: Optional[str] = Field(default=None, description="Account ID")
    date: Optional[datetime] = Field(default=None, description="Transaction date")
    amount: Optional[float] = Field(default=None, description="Transaction amount")
    concept: Optional[str] = Field(default=None, description="Transaction concept/description")
    notes: Optional[str] = Field(default=None, description="Transaction notes")
    category_id: Optional[str] = Field(default=None, description="Category ID")
    document_id: Optional[str] = Field(default=None, description="Related document ID")
    contact_id: Optional[str] = Field(default=None, description="Related contact ID")
    is_reconciled: Optional[bool] = Field(default=None, description="Whether the transaction is reconciled")


class TreasuryTransaction(TreasuryTransactionCreate):
    """Treasury transaction model."""
    
    id: str = Field(..., description="Transaction ID")
    type: str = Field(..., description="Transaction type (income, expense)")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class TreasuryTransactionListParams(PaginationParams, DateRangeParams):
    """Parameters for listing treasury transactions."""
    
    account_id: Optional[str] = Field(default=None, description="Filter by account ID")
    type: Optional[str] = Field(default=None, description="Filter by transaction type")
    category_id: Optional[str] = Field(default=None, description="Filter by category ID")
    contact_id: Optional[str] = Field(default=None, description="Filter by contact ID")
    document_id: Optional[str] = Field(default=None, description="Filter by document ID")
    is_reconciled: Optional[bool] = Field(default=None, description="Filter by reconciliation status")
    query: Optional[str] = Field(default=None, description="Search query")


class TreasuryCategoryCreate(BaseModel):
    """Model for creating a treasury category."""
    
    name: str = Field(..., description="Category name")
    type: str = Field(..., description="Category type (income, expense)")
    parent_id: Optional[str] = Field(default=None, description="Parent category ID")


class TreasuryCategoryUpdate(BaseModel):
    """Model for updating a treasury category."""
    
    name: Optional[str] = Field(default=None, description="Category name")
    type: Optional[str] = Field(default=None, description="Category type (income, expense)")
    parent_id: Optional[str] = Field(default=None, description="Parent category ID")


class TreasuryCategory(TreasuryCategoryCreate):
    """Treasury category model."""
    
    id: str = Field(..., description="Category ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class TreasuryCategoryListParams(PaginationParams):
    """Parameters for listing treasury categories."""
    
    type: Optional[str] = Field(default=None, description="Filter by category type")
    query: Optional[str] = Field(default=None, description="Search query")


# Response models
class TreasuryAccountResponse(BaseResponse, TreasuryAccount):
    """Response model for a single treasury account."""
    pass


class TreasuryAccountListResponse(BaseResponse):
    """Response model for a list of treasury accounts."""
    
    items: List[TreasuryAccount] = Field(..., description="List of accounts")
    total: Optional[int] = Field(default=None, description="Total number of accounts")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class TreasuryTransactionResponse(BaseResponse, TreasuryTransaction):
    """Response model for a single treasury transaction."""
    pass


class TreasuryTransactionListResponse(BaseResponse):
    """Response model for a list of treasury transactions."""
    
    items: List[TreasuryTransaction] = Field(..., description="List of transactions")
    total: Optional[int] = Field(default=None, description="Total number of transactions")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class TreasuryCategoryResponse(BaseResponse, TreasuryCategory):
    """Response model for a single treasury category."""
    pass


class TreasuryCategoryListResponse(BaseResponse):
    """Response model for a list of treasury categories."""
    
    items: List[TreasuryCategory] = Field(..., description="List of categories")
    total: Optional[int] = Field(default=None, description="Total number of categories")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page") 