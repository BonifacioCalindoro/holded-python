"""
Models for the Accounting API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class AccountCreate(BaseModel):
    """Model for creating an accounting account."""
    
    code: str = Field(..., description="Account code")
    name: str = Field(..., description="Account name")
    description: Optional[str] = Field(default=None, description="Account description")
    type: str = Field(..., description="Account type")
    parent_id: Optional[str] = Field(default=None, description="Parent account ID")
    is_tax_account: Optional[bool] = Field(default=None, description="Whether this is a tax account")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class AccountUpdate(BaseModel):
    """Model for updating an accounting account."""
    
    code: Optional[str] = Field(default=None, description="Account code")
    name: Optional[str] = Field(default=None, description="Account name")
    description: Optional[str] = Field(default=None, description="Account description")
    type: Optional[str] = Field(default=None, description="Account type")
    parent_id: Optional[str] = Field(default=None, description="Parent account ID")
    is_tax_account: Optional[bool] = Field(default=None, description="Whether this is a tax account")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class Account(AccountCreate):
    """Accounting account model."""
    
    id: str = Field(..., description="Account ID")
    balance: Optional[float] = Field(default=None, description="Account balance")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class AccountListParams(PaginationParams):
    """Parameters for listing accounting accounts."""
    
    type: Optional[str] = Field(default=None, description="Filter by account type")
    parent_id: Optional[str] = Field(default=None, description="Filter by parent account ID")
    query: Optional[str] = Field(default=None, description="Search query")


class JournalEntryCreate(BaseModel):
    """Model for creating a journal entry."""
    
    date: datetime = Field(..., description="Entry date")
    concept: str = Field(..., description="Entry concept/description")
    document_id: Optional[str] = Field(default=None, description="Related document ID")
    reference: Optional[str] = Field(default=None, description="Entry reference")
    notes: Optional[str] = Field(default=None, description="Entry notes")
    lines: List["JournalEntryLine"] = Field(..., description="Entry lines")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class JournalEntryLine(BaseModel):
    """Journal entry line model."""
    
    account_id: str = Field(..., description="Account ID")
    debit: Optional[float] = Field(default=None, description="Debit amount")
    credit: Optional[float] = Field(default=None, description="Credit amount")
    description: Optional[str] = Field(default=None, description="Line description")
    contact_id: Optional[str] = Field(default=None, description="Related contact ID")
    tax_id: Optional[str] = Field(default=None, description="Tax ID")
    tax_rate: Optional[float] = Field(default=None, description="Tax rate")


class JournalEntry(JournalEntryCreate):
    """Journal entry model."""
    
    id: str = Field(..., description="Entry ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class JournalEntryListParams(PaginationParams, DateRangeParams):
    """Parameters for listing journal entries."""
    
    account_id: Optional[str] = Field(default=None, description="Filter by account ID")
    document_id: Optional[str] = Field(default=None, description="Filter by document ID")
    contact_id: Optional[str] = Field(default=None, description="Filter by contact ID")
    query: Optional[str] = Field(default=None, description="Search query")


class FiscalYearCreate(BaseModel):
    """Model for creating a fiscal year."""
    
    name: str = Field(..., description="Fiscal year name")
    start_date: datetime = Field(..., description="Start date")
    end_date: datetime = Field(..., description="End date")
    is_closed: Optional[bool] = Field(default=None, description="Whether the fiscal year is closed")
    notes: Optional[str] = Field(default=None, description="Fiscal year notes")


class FiscalYearUpdate(BaseModel):
    """Model for updating a fiscal year."""
    
    name: Optional[str] = Field(default=None, description="Fiscal year name")
    start_date: Optional[datetime] = Field(default=None, description="Start date")
    end_date: Optional[datetime] = Field(default=None, description="End date")
    is_closed: Optional[bool] = Field(default=None, description="Whether the fiscal year is closed")
    notes: Optional[str] = Field(default=None, description="Fiscal year notes")


class FiscalYear(FiscalYearCreate):
    """Fiscal year model."""
    
    id: str = Field(..., description="Fiscal year ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class FiscalYearListParams(PaginationParams):
    """Parameters for listing fiscal years."""
    
    is_closed: Optional[bool] = Field(default=None, description="Filter by closed status")
    query: Optional[str] = Field(default=None, description="Search query")


class TaxCreate(BaseModel):
    """Model for creating a tax."""
    
    name: str = Field(..., description="Tax name")
    rate: float = Field(..., description="Tax rate")
    type: str = Field(..., description="Tax type")
    account_id: Optional[str] = Field(default=None, description="Account ID")
    is_default: Optional[bool] = Field(default=None, description="Whether this is the default tax")


class TaxUpdate(BaseModel):
    """Model for updating a tax."""
    
    name: Optional[str] = Field(default=None, description="Tax name")
    rate: Optional[float] = Field(default=None, description="Tax rate")
    type: Optional[str] = Field(default=None, description="Tax type")
    account_id: Optional[str] = Field(default=None, description="Account ID")
    is_default: Optional[bool] = Field(default=None, description="Whether this is the default tax")


class Tax(TaxCreate):
    """Tax model."""
    
    id: str = Field(..., description="Tax ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class TaxListParams(PaginationParams):
    """Parameters for listing taxes."""
    
    type: Optional[str] = Field(default=None, description="Filter by tax type")
    query: Optional[str] = Field(default=None, description="Search query")


class FinancialReportParams(DateRangeParams):
    """Parameters for generating financial reports."""
    
    type: str = Field(..., description="Report type")
    format: Optional[str] = Field(default=None, description="Report format")
    fiscal_year_id: Optional[str] = Field(default=None, description="Fiscal year ID")
    account_id: Optional[str] = Field(default=None, description="Account ID")
    contact_id: Optional[str] = Field(default=None, description="Contact ID")


# Response models
class AccountResponse(BaseResponse, Account):
    """Response model for a single accounting account."""
    pass


class AccountListResponse(BaseResponse):
    """Response model for a list of accounting accounts."""
    
    items: List[Account] = Field(..., description="List of accounts")
    total: Optional[int] = Field(default=None, description="Total number of accounts")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class JournalEntryResponse(BaseResponse, JournalEntry):
    """Response model for a single journal entry."""
    pass


class JournalEntryListResponse(BaseResponse):
    """Response model for a list of journal entries."""
    
    items: List[JournalEntry] = Field(..., description="List of journal entries")
    total: Optional[int] = Field(default=None, description="Total number of journal entries")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class FiscalYearResponse(BaseResponse, FiscalYear):
    """Response model for a single fiscal year."""
    pass


class FiscalYearListResponse(BaseResponse):
    """Response model for a list of fiscal years."""
    
    items: List[FiscalYear] = Field(..., description="List of fiscal years")
    total: Optional[int] = Field(default=None, description="Total number of fiscal years")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class TaxResponse(BaseResponse, Tax):
    """Response model for a single tax."""
    pass


class TaxListResponse(BaseResponse):
    """Response model for a list of taxes."""
    
    items: List[Tax] = Field(..., description="List of taxes")
    total: Optional[int] = Field(default=None, description="Total number of taxes")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class FinancialReportResponse(BaseResponse):
    """Response model for a financial report."""
    
    data: Dict[str, Any] = Field(..., description="Report data")
    report_type: str = Field(..., description="Report type")
    start_date: Optional[datetime] = Field(default=None, description="Report start date")
    end_date: Optional[datetime] = Field(default=None, description="Report end date")


# Fix forward references
JournalEntryCreate.update_forward_refs() 