"""
Models for the Contacts API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from enum import Enum

from pydantic import Field, EmailStr, field_validator, AnyHttpUrl

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class ContactType(str, Enum):
    """Contact type enum."""
    CLIENT = "client"
    SUPPLIER = "supplier"
    LEAD = "lead"
    PROSPECT = "prospect"
    EMPLOYEE = "employee"
    OTHER = "other"


class ContactStatus(str, Enum):
    """Contact status enum."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    BLOCKED = "blocked"


class ContactAddress(BaseModel):
    """Contact address model."""
    
    street: Optional[str] = Field(default=None, description="Street address")
    city: Optional[str] = Field(default=None, description="City")
    postal_code: Optional[str] = Field(default=None, description="Postal code")
    province: Optional[str] = Field(default=None, description="Province or state")
    country: Optional[str] = Field(default=None, description="Country")
    address_line2: Optional[str] = Field(default=None, description="Additional address information")
    coordinates: Optional[Dict[str, float]] = Field(default=None, description="GPS coordinates")


class ContactBankAccount(BaseModel):
    """Contact bank account model."""
    
    bank_name: Optional[str] = Field(default=None, description="Bank name")
    account_number: Optional[str] = Field(default=None, description="Account number")
    iban: Optional[str] = Field(default=None, description="IBAN")
    swift: Optional[str] = Field(default=None, description="SWIFT/BIC code")
    account_holder: Optional[str] = Field(default=None, description="Account holder name")
    bank_address: Optional[str] = Field(default=None, description="Bank address")
    is_default: Optional[bool] = Field(default=None, description="Whether this is the default bank account")


class ContactTax(BaseModel):
    """Contact tax information model."""
    
    tax_id: Optional[str] = Field(default=None, description="Tax ID")
    tax_regime: Optional[str] = Field(default=None, description="Tax regime")
    vat_number: Optional[str] = Field(default=None, description="VAT number")
    intra_community: Optional[bool] = Field(default=None, description="Whether the contact is intra-community")
    tax_exempt: Optional[bool] = Field(default=None, description="Whether the contact is tax exempt")
    tax_retention: Optional[float] = Field(default=None, description="Tax retention percentage")


class ContactSocialMedia(BaseModel):
    """Contact social media model."""
    
    linkedin: Optional[str] = Field(default=None, description="LinkedIn profile URL")
    twitter: Optional[str] = Field(default=None, description="Twitter profile URL")
    facebook: Optional[str] = Field(default=None, description="Facebook profile URL")
    instagram: Optional[str] = Field(default=None, description="Instagram profile URL")
    youtube: Optional[str] = Field(default=None, description="YouTube channel URL")
    other: Optional[Dict[str, str]] = Field(default=None, description="Other social media profiles")


class ContactPaymentSettings(BaseModel):
    """Contact payment settings model."""
    
    payment_method: Optional[str] = Field(default=None, description="Default payment method")
    payment_terms: Optional[int] = Field(default=None, description="Payment terms in days")
    credit_limit: Optional[float] = Field(default=None, description="Credit limit")
    currency: Optional[str] = Field(default=None, description="Default currency")
    language: Optional[str] = Field(default=None, description="Default language for documents")


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
    type: Optional[ContactType] = Field(default=ContactType.CLIENT, description="Contact type")
    status: Optional[ContactStatus] = Field(default=ContactStatus.ACTIVE, description="Contact status")
    billing_address: Optional[ContactAddress] = Field(default=None, description="Billing address")
    shipping_address: Optional[ContactAddress] = Field(default=None, description="Shipping address")
    bank_account: Optional[ContactBankAccount] = Field(default=None, description="Bank account information")
    tax_info: Optional[ContactTax] = Field(default=None, description="Tax information")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    social_media: Optional[ContactSocialMedia] = Field(default=None, description="Social media profiles")
    payment_settings: Optional[ContactPaymentSettings] = Field(default=None, description="Payment settings")
    tags: Optional[List[str]] = Field(default=None, description="Contact tags")
    salesperson_id: Optional[str] = Field(default=None, description="Salesperson ID")
    company_name: Optional[str] = Field(default=None, description="Company name (if different from contact name)")
    job_title: Optional[str] = Field(default=None, description="Job title")
    department: Optional[str] = Field(default=None, description="Department")
    date_of_birth: Optional[datetime] = Field(default=None, description="Date of birth")
    
    @field_validator('email')
    def validate_email(cls, v):
        """Validate email format."""
        if v is not None and v.strip() != "":
            # Simple validation, could use EmailStr from pydantic if needed
            if '@' not in v:
                raise ValueError('Invalid email format')
        return v
    
    @field_validator('website')
    def validate_website(cls, v):
        """Validate website URL format."""
        if v is not None and v.strip() != "":
            # Simple validation, could use AnyHttpUrl from pydantic if needed
            if not (v.startswith('http://') or v.startswith('https://')):
                v = 'https://' + v
        return v


class ContactUpdate(BaseModel):
    """Model for updating a contact."""
    
    name: Optional[str] = Field(default=None, description="Contact name")
    code: Optional[str] = Field(default=None, description="Contact code")
    email: Optional[str] = Field(default=None, description="Contact email")
    phone: Optional[str] = Field(default=None, description="Contact phone")
    mobile: Optional[str] = Field(default=None, description="Contact mobile phone")
    fax: Optional[str] = Field(default=None, description="Contact fax")
    website: Optional[str] = Field(default=None, description="Contact website")
    notes: Optional[str] = Field(default=None, description="Contact notes")
    contact_person: Optional[str] = Field(default=None, description="Contact person")
    type: Optional[ContactType] = Field(default=None, description="Contact type")
    status: Optional[ContactStatus] = Field(default=None, description="Contact status")
    billing_address: Optional[ContactAddress] = Field(default=None, description="Billing address")
    shipping_address: Optional[ContactAddress] = Field(default=None, description="Shipping address")
    bank_account: Optional[ContactBankAccount] = Field(default=None, description="Bank account information")
    tax_info: Optional[ContactTax] = Field(default=None, description="Tax information")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    social_media: Optional[ContactSocialMedia] = Field(default=None, description="Social media profiles")
    payment_settings: Optional[ContactPaymentSettings] = Field(default=None, description="Payment settings")
    tags: Optional[List[str]] = Field(default=None, description="Contact tags")
    salesperson_id: Optional[str] = Field(default=None, description="Salesperson ID")
    company_name: Optional[str] = Field(default=None, description="Company name (if different from contact name)")
    job_title: Optional[str] = Field(default=None, description="Job title")
    department: Optional[str] = Field(default=None, description="Department")
    date_of_birth: Optional[datetime] = Field(default=None, description="Date of birth")
    
    @field_validator('email')
    def validate_email(cls, v):
        """Validate email format."""
        if v is not None and v.strip() != "":
            if '@' not in v:
                raise ValueError('Invalid email format')
        return v
    
    @field_validator('website')
    def validate_website(cls, v):
        """Validate website URL format."""
        if v is not None and v.strip() != "":
            if not (v.startswith('http://') or v.startswith('https://')):
                v = 'https://' + v
        return v


class Contact(BaseModel):
    """Contact model."""
    
    id: str = Field(..., description="Contact ID")
    name: str = Field(..., description="Contact name")
    code: Optional[str] = Field(default=None, description="Contact code")
    email: Optional[str] = Field(default=None, description="Contact email")
    phone: Optional[str] = Field(default=None, description="Contact phone")
    mobile: Optional[str] = Field(default=None, description="Contact mobile phone")
    fax: Optional[str] = Field(default=None, description="Contact fax")
    website: Optional[str] = Field(default=None, description="Contact website")
    notes: Optional[str] = Field(default=None, description="Contact notes")
    contact_person: Optional[str] = Field(default=None, description="Contact person")
    type: ContactType = Field(..., description="Contact type")
    status: ContactStatus = Field(..., description="Contact status")
    billing_address: Optional[ContactAddress] = Field(default=None, description="Billing address")
    shipping_address: Optional[ContactAddress] = Field(default=None, description="Shipping address")
    bank_account: Optional[ContactBankAccount] = Field(default=None, description="Bank account information")
    tax_info: Optional[ContactTax] = Field(default=None, description="Tax information")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    social_media: Optional[ContactSocialMedia] = Field(default=None, description="Social media profiles")
    payment_settings: Optional[ContactPaymentSettings] = Field(default=None, description="Payment settings")
    tags: Optional[List[str]] = Field(default=None, description="Contact tags")
    salesperson_id: Optional[str] = Field(default=None, description="Salesperson ID")
    salesperson_name: Optional[str] = Field(default=None, description="Salesperson name")
    company_name: Optional[str] = Field(default=None, description="Company name (if different from contact name)")
    job_title: Optional[str] = Field(default=None, description="Job title")
    department: Optional[str] = Field(default=None, description="Department")
    date_of_birth: Optional[datetime] = Field(default=None, description="Date of birth")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")
    last_activity_at: Optional[datetime] = Field(default=None, description="Last activity date")
    total_invoiced: Optional[float] = Field(default=None, description="Total amount invoiced")
    outstanding_balance: Optional[float] = Field(default=None, description="Outstanding balance")
    document_count: Optional[Dict[str, int]] = Field(default=None, description="Count of documents by type")


class ContactListParams(PaginationParams, DateRangeParams):
    """Parameters for listing contacts."""
    
    type: Optional[ContactType] = Field(default=None, description="Filter by contact type")
    status: Optional[ContactStatus] = Field(default=None, description="Filter by contact status")
    query: Optional[str] = Field(default=None, description="Search query")
    tags: Optional[List[str]] = Field(default=None, description="Filter by tags")
    salesperson_id: Optional[str] = Field(default=None, description="Filter by salesperson ID")
    has_outstanding_balance: Optional[bool] = Field(default=None, description="Filter by outstanding balance")
    min_total_invoiced: Optional[float] = Field(default=None, description="Filter by minimum total invoiced")
    max_total_invoiced: Optional[float] = Field(default=None, description="Filter by maximum total invoiced")


class ContactAttachment(BaseModel):
    """Contact attachment model."""
    
    id: str = Field(..., description="Attachment ID")
    name: str = Field(..., description="Attachment name")
    size: Optional[int] = Field(default=None, description="Attachment size in bytes")
    type: Optional[str] = Field(default=None, description="Attachment MIME type")
    url: Optional[str] = Field(default=None, description="Attachment URL")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")


class ContactAttachmentUpload(BaseModel):
    """Parameters for uploading a contact attachment."""
    
    name: str = Field(..., description="Attachment name")
    file: str = Field(..., description="Base64 encoded file content")
    type: Optional[str] = Field(default=None, description="Attachment MIME type")


class ContactImport(BaseModel):
    """Parameters for importing contacts."""
    
    file: str = Field(..., description="Base64 encoded CSV or Excel file content")
    file_type: str = Field(..., description="File type (csv, xlsx)")
    column_mapping: Dict[str, str] = Field(..., description="Mapping of file columns to contact fields")
    skip_first_row: Optional[bool] = Field(default=True, description="Whether to skip the first row (header)")


# Response models
class ContactResponse(BaseResponse):
    """Response model for a single contact."""
    
    contact: Contact = Field(..., description="Contact data")


class ContactListResponse(BaseResponse):
    """Response model for a list of contacts."""
    
    items: List[Contact] = Field(..., description="List of contacts")
    total: Optional[int] = Field(default=None, description="Total number of contacts")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class ContactAttachmentResponse(BaseResponse):
    """Response model for a single contact attachment."""
    
    attachment: ContactAttachment = Field(..., description="Attachment data")


class ContactAttachmentListResponse(BaseResponse):
    """Response model for a list of contact attachments."""
    
    items: List[ContactAttachment] = Field(..., description="List of attachments")
    total: Optional[int] = Field(default=None, description="Total number of attachments")


class ContactImportResponse(BaseResponse):
    """Response model for importing contacts."""
    
    imported: int = Field(..., description="Number of contacts imported")
    errors: Optional[List[Dict[str, Any]]] = Field(default=None, description="Import errors")
    message: Optional[str] = Field(default=None, description="Response message") 