"""
Models for the Contacts API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams


class ContactAddress(BaseModel):
    """Contact address model."""
    
    street: Optional[str] = Field(default=None, description="Street address")
    city: Optional[str] = Field(default=None, description="City")
    postal_code: Optional[str] = Field(default=None, description="Postal code")
    province: Optional[str] = Field(default=None, description="Province or state")
    country: Optional[str] = Field(default=None, description="Country")


class ContactBankAccount(BaseModel):
    """Contact bank account model."""
    
    bank_name: Optional[str] = Field(default=None, description="Bank name")
    account_number: Optional[str] = Field(default=None, description="Account number")
    iban: Optional[str] = Field(default=None, description="IBAN")
    swift: Optional[str] = Field(default=None, description="SWIFT/BIC code")


class ContactTax(BaseModel):
    """Contact tax information model."""
    
    tax_id: Optional[str] = Field(default=None, description="Tax ID")
    tax_regime: Optional[str] = Field(default=None, description="Tax regime")
    vat_number: Optional[str] = Field(default=None, description="VAT number")


class ContactCreate(BaseModel):
    """Model for creating a contact."""
    
    name: str = Field(..., description="Contact name")
    code: Optional[str] = Field(default=None, description="Contact code")
    email: Optional[str] = Field(default=None, description="Contact email")
    phone: Optional[str] = Field(default=None, description="Contact phone")
    mobile: Optional[str] = Field(default=None, description="Contact mobile phone")
    fax: Optional[str] = Field(default=None, description="Contact fax")
    website: Optional[str] = Field(default=None, description="Contact website")
    notes: Optional[str] = Field(default=None, description="Contact notes")
    contact_person: Optional[str] = Field(default=None, description="Contact person")
    type: Optional[str] = Field(default=None, description="Contact type (client, supplier, etc.)")
    billing_address: Optional[ContactAddress] = Field(default=None, description="Billing address")
    shipping_address: Optional[ContactAddress] = Field(default=None, description="Shipping address")
    bank_account: Optional[ContactBankAccount] = Field(default=None, description="Bank account information")
    tax_info: Optional[ContactTax] = Field(default=None, description="Tax information")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class ContactUpdate(ContactCreate):
    """Model for updating a contact."""
    
    name: Optional[str] = Field(default=None, description="Contact name")


class Contact(ContactCreate):
    """Contact model."""
    
    id: str = Field(..., description="Contact ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class ContactListParams(PaginationParams):
    """Parameters for listing contacts."""
    
    type: Optional[str] = Field(default=None, description="Filter by contact type")
    query: Optional[str] = Field(default=None, description="Search query")


class ContactAttachment(BaseModel):
    """Contact attachment model."""
    
    id: str = Field(..., description="Attachment ID")
    name: str = Field(..., description="Attachment name")
    size: Optional[int] = Field(default=None, description="Attachment size in bytes")
    type: Optional[str] = Field(default=None, description="Attachment MIME type")
    url: Optional[str] = Field(default=None, description="Attachment URL")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")


# Response models
class ContactResponse(BaseResponse, Contact):
    """Response model for a single contact."""
    pass


class ContactListResponse(BaseResponse):
    """Response model for a list of contacts."""
    
    items: List[Contact] = Field(..., description="List of contacts")
    total: Optional[int] = Field(default=None, description="Total number of contacts")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class ContactAttachmentListResponse(BaseResponse):
    """Response model for a list of contact attachments."""
    
    items: List[ContactAttachment] = Field(..., description="List of attachments")


class ContactAttachmentResponse(BaseResponse, ContactAttachment):
    """Response model for a single contact attachment."""
    pass 