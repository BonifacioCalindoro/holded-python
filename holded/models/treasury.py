"""
Models for the Treasury API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from enum import Enum

from pydantic import Field, field_validator

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class AccountType(str, Enum):
    """Account type enum."""
    BANK = "bank"
    CASH = "cash"
    CREDIT_CARD = "creditcard"
    PAYPAL = "paypal"
    OTHER = "other"


class AccountCreate(BaseModel):
    """Model for creating a treasury account."""
    
    name: str = Field(..., description="Account name")
    type: AccountType = Field(..., description="Account type")
    currency: Optional[str] = Field(default=None, description="Account currency (ISO code)")
    initial_balance: Optional[float] = Field(default=0.0, description="Initial balance")
    description: Optional[str] = Field(default=None, description="Account description")
    is_active: Optional[bool] = Field(default=True, description="Whether the account is active")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class AccountUpdate(BaseModel):
    """Model for updating a treasury account."""
    
    name: Optional[str] = Field(default=None, description="Account name")
    type: Optional[AccountType] = Field(default=None, description="Account type")
    currency: Optional[str] = Field(default=None, description="Account currency (ISO code)")
    description: Optional[str] = Field(default=None, description="Account description")
    is_active: Optional[bool] = Field(default=None, description="Whether the account is active")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class Account(AccountCreate):
    """Treasury account model."""
    
    id: str = Field(..., description="Account ID")
    balance: float = Field(..., description="Current balance")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class AccountListParams(PaginationParams):
    """Parameters for listing treasury accounts."""
    
    type: Optional[AccountType] = Field(default=None, description="Filter by account type")
    is_active: Optional[bool] = Field(default=None, description="Filter by active status")
    query: Optional[str] = Field(default=None, description="Search query")


class TransactionType(str, Enum):
    """Transaction type enum."""
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"


class TransactionStatus(str, Enum):
    """Transaction status enum."""
    PENDING = "pending"
    RECONCILED = "reconciled"


class TransactionCreate(BaseModel):
    """Model for creating a treasury transaction."""
    
    account_id: str = Field(..., description="Account ID")
    date: datetime = Field(..., description="Transaction date")
    amount: float = Field(..., description="Transaction amount")
    type: TransactionType = Field(..., description="Transaction type")
    concept: str = Field(..., description="Transaction concept/description")
    notes: Optional[str] = Field(default=None, description="Transaction notes")
    category_id: Optional[str] = Field(default=None, description="Category ID")
    contact_id: Optional[str] = Field(default=None, description="Contact ID")
    document_id: Optional[str] = Field(default=None, description="Document ID")
    reference: Optional[str] = Field(default=None, description="Transaction reference")
    status: Optional[TransactionStatus] = Field(default=TransactionStatus.PENDING, description="Transaction status")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    
    @field_validator('amount')
    def validate_amount(cls, v, values):
        """Validate amount based on transaction type."""
        if 'type' in values.data:
            if values.data['type'] == TransactionType.EXPENSE and v > 0:
                return -v  # Expenses should be negative
            elif values.data['type'] == TransactionType.INCOME and v < 0:
                return abs(v)  # Income should be positive
        return v


class TransactionUpdate(BaseModel):
    """Model for updating a treasury transaction."""
    
    account_id: Optional[str] = Field(default=None, description="Account ID")
    date: Optional[datetime] = Field(default=None, description="Transaction date")
    amount: Optional[float] = Field(default=None, description="Transaction amount")
    type: Optional[TransactionType] = Field(default=None, description="Transaction type")
    concept: Optional[str] = Field(default=None, description="Transaction concept/description")
    notes: Optional[str] = Field(default=None, description="Transaction notes")
    category_id: Optional[str] = Field(default=None, description="Category ID")
    contact_id: Optional[str] = Field(default=None, description="Contact ID")
    document_id: Optional[str] = Field(default=None, description="Document ID")
    reference: Optional[str] = Field(default=None, description="Transaction reference")
    status: Optional[TransactionStatus] = Field(default=None, description="Transaction status")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class Transaction(TransactionCreate):
    """Treasury transaction model."""
    
    id: str = Field(..., description="Transaction ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class TransactionListParams(PaginationParams, DateRangeParams):
    """Parameters for listing treasury transactions."""
    
    account_id: Optional[str] = Field(default=None, description="Filter by account ID")
    type: Optional[TransactionType] = Field(default=None, description="Filter by transaction type")
    status: Optional[TransactionStatus] = Field(default=None, description="Filter by transaction status")
    category_id: Optional[str] = Field(default=None, description="Filter by category ID")
    contact_id: Optional[str] = Field(default=None, description="Filter by contact ID")
    document_id: Optional[str] = Field(default=None, description="Filter by document ID")
    min_amount: Optional[float] = Field(default=None, description="Filter by minimum amount")
    max_amount: Optional[float] = Field(default=None, description="Filter by maximum amount")
    query: Optional[str] = Field(default=None, description="Search query")


class TransactionReconcileParams(BaseModel):
    """Parameters for reconciling a treasury transaction."""
    
    status: TransactionStatus = Field(..., description="Transaction status")


class CategoryCreate(BaseModel):
    """Model for creating a treasury category."""
    
    name: str = Field(..., description="Category name")
    type: TransactionType = Field(..., description="Category type")
    parent_id: Optional[str] = Field(default=None, description="Parent category ID")
    description: Optional[str] = Field(default=None, description="Category description")
    color: Optional[str] = Field(default=None, description="Category color (hex code)")
    is_active: Optional[bool] = Field(default=True, description="Whether the category is active")


class CategoryUpdate(BaseModel):
    """Model for updating a treasury category."""
    
    name: Optional[str] = Field(default=None, description="Category name")
    type: Optional[TransactionType] = Field(default=None, description="Category type")
    parent_id: Optional[str] = Field(default=None, description="Parent category ID")
    description: Optional[str] = Field(default=None, description="Category description")
    color: Optional[str] = Field(default=None, description="Category color (hex code)")
    is_active: Optional[bool] = Field(default=None, description="Whether the category is active")


class Category(CategoryCreate):
    """Treasury category model."""
    
    id: str = Field(..., description="Category ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class CategoryListParams(PaginationParams):
    """Parameters for listing treasury categories."""
    
    type: Optional[TransactionType] = Field(default=None, description="Filter by category type")
    parent_id: Optional[str] = Field(default=None, description="Filter by parent category ID")
    is_active: Optional[bool] = Field(default=None, description="Filter by active status")
    query: Optional[str] = Field(default=None, description="Search query")


# Response models
class AccountResponse(BaseResponse, Account):
    """Response model for a single treasury account."""
    pass


class AccountListResponse(BaseResponse):
    """Response model for a list of treasury accounts."""
    
    items: List[Account] = Field(..., description="List of accounts")
    total: Optional[int] = Field(default=None, description="Total number of accounts")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class TransactionResponse(BaseResponse, Transaction):
    """Response model for a single treasury transaction."""
    pass


class TransactionListResponse(BaseResponse):
    """Response model for a list of treasury transactions."""
    
    items: List[Transaction] = Field(..., description="List of transactions")
    total: Optional[int] = Field(default=None, description="Total number of transactions")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class CategoryResponse(BaseResponse, Category):
    """Response model for a single treasury category."""
    pass


class CategoryListResponse(BaseResponse):
    """Response model for a list of treasury categories."""
    
    items: List[Category] = Field(..., description="List of categories")
    total: Optional[int] = Field(default=None, description="Total number of categories")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page") 