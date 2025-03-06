"""
Models for the Documents API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from enum import Enum

from pydantic import Field, field_validator

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class DocumentType(str, Enum):
    """Document type enum."""
    INVOICE = "invoice"
    ESTIMATE = "estimate"
    ORDER = "order"
    PROFORMA = "proforma"
    DELIVERY_NOTE = "deliverynote"
    CREDIT_NOTE = "creditnote"
    BILL = "bill"
    SUPPLIER_ORDER = "supplierorder"
    WAYBILL = "waybill"
    RECEIPT = "receipt"


class DocumentStatus(str, Enum):
    """Document status enum."""
    DRAFT = "draft"
    SENT = "sent"
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    PAID = "paid"
    EXPIRED = "expired"
    PENDING = "pending"
    REJECTED = "rejected"
    PARTIALLY_PAID = "partially_paid"


class PaymentMethod(str, Enum):
    """Payment method enum."""
    CASH = "cash"
    BANK_TRANSFER = "bank_transfer"
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    CHECK = "check"
    OTHER = "other"


class DocumentItem(BaseModel):
    """Document item model."""
    
    name: str = Field(..., description="Item name")
    units: float = Field(..., description="Number of units")
    price: float = Field(..., description="Unit price")
    discount: Optional[float] = Field(default=None, description="Discount percentage")
    tax: Optional[float] = Field(default=None, description="Tax percentage")
    description: Optional[str] = Field(default=None, description="Item description")
    product_id: Optional[str] = Field(default=None, description="Product ID if linked to a product")
    sku: Optional[str] = Field(default=None, description="Product SKU")
    variant_id: Optional[str] = Field(default=None, description="Product variant ID")
    tax_id: Optional[str] = Field(default=None, description="Tax ID")
    discount_id: Optional[str] = Field(default=None, description="Discount ID")
    subtotal: Optional[float] = Field(default=None, description="Item subtotal")
    total: Optional[float] = Field(default=None, description="Item total with taxes")


class DocumentPayment(BaseModel):
    """Document payment model."""
    
    date: datetime = Field(..., description="Payment date")
    amount: float = Field(..., description="Payment amount")
    method: Union[PaymentMethod, str] = Field(..., description="Payment method")
    notes: Optional[str] = Field(default=None, description="Payment notes")
    account_id: Optional[str] = Field(default=None, description="Treasury account ID")
    transaction_id: Optional[str] = Field(default=None, description="Treasury transaction ID")
    
    @field_validator('method')
    def validate_method(cls, v):
        """Convert string payment method to enum if possible."""
        if isinstance(v, str) and v not in PaymentMethod.__members__:
            return v
        return v


class DocumentTax(BaseModel):
    """Document tax model."""
    
    id: Optional[str] = Field(default=None, description="Tax ID")
    name: str = Field(..., description="Tax name")
    rate: float = Field(..., description="Tax rate percentage")
    amount: float = Field(..., description="Tax amount")


class DocumentCreate(BaseModel):
    """Model for creating a document."""
    
    contact_id: str = Field(..., description="Contact ID")
    date: datetime = Field(..., description="Document date")
    type: DocumentType = Field(..., description="Document type")
    number: Optional[str] = Field(default=None, description="Document number")
    notes: Optional[str] = Field(default=None, description="Document notes")
    items: List[DocumentItem] = Field(..., description="Document items")
    payments: Optional[List[DocumentPayment]] = Field(default=None, description="Document payments")
    currency: Optional[str] = Field(default="EUR", description="Document currency")
    exchange_rate: Optional[float] = Field(default=1.0, description="Exchange rate")
    due_date: Optional[datetime] = Field(default=None, description="Due date")
    reference: Optional[str] = Field(default=None, description="Document reference")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    shipping_address: Optional[Dict[str, Any]] = Field(default=None, description="Shipping address")
    billing_address: Optional[Dict[str, Any]] = Field(default=None, description="Billing address")
    salesperson_id: Optional[str] = Field(default=None, description="Salesperson ID")
    tags: Optional[List[str]] = Field(default=None, description="Document tags")
    language: Optional[str] = Field(default=None, description="Document language")
    payment_method: Optional[Union[PaymentMethod, str]] = Field(default=None, description="Default payment method")
    payment_terms: Optional[int] = Field(default=None, description="Payment terms in days")
    taxes: Optional[List[DocumentTax]] = Field(default=None, description="Document taxes")
    discount: Optional[float] = Field(default=None, description="Global discount percentage")
    series_id: Optional[str] = Field(default=None, description="Numbering series ID")


class DocumentUpdate(BaseModel):
    """Model for updating a document."""
    
    contact_id: Optional[str] = Field(default=None, description="Contact ID")
    date: Optional[datetime] = Field(default=None, description="Document date")
    number: Optional[str] = Field(default=None, description="Document number")
    notes: Optional[str] = Field(default=None, description="Document notes")
    items: Optional[List[DocumentItem]] = Field(default=None, description="Document items")
    payments: Optional[List[DocumentPayment]] = Field(default=None, description="Document payments")
    currency: Optional[str] = Field(default=None, description="Document currency")
    exchange_rate: Optional[float] = Field(default=None, description="Exchange rate")
    due_date: Optional[datetime] = Field(default=None, description="Due date")
    reference: Optional[str] = Field(default=None, description="Document reference")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    shipping_address: Optional[Dict[str, Any]] = Field(default=None, description="Shipping address")
    billing_address: Optional[Dict[str, Any]] = Field(default=None, description="Billing address")
    salesperson_id: Optional[str] = Field(default=None, description="Salesperson ID")
    tags: Optional[List[str]] = Field(default=None, description="Document tags")
    language: Optional[str] = Field(default=None, description="Document language")
    payment_method: Optional[Union[PaymentMethod, str]] = Field(default=None, description="Default payment method")
    payment_terms: Optional[int] = Field(default=None, description="Payment terms in days")
    taxes: Optional[List[DocumentTax]] = Field(default=None, description="Document taxes")
    discount: Optional[float] = Field(default=None, description="Global discount percentage")
    series_id: Optional[str] = Field(default=None, description="Numbering series ID")
    status: Optional[DocumentStatus] = Field(default=None, description="Document status")


class Document(BaseModel):
    """Document model."""
    
    id: str = Field(..., description="Document ID")
    type: DocumentType = Field(..., description="Document type")
    status: DocumentStatus = Field(..., description="Document status")
    contact_id: str = Field(..., description="Contact ID")
    date: datetime = Field(..., description="Document date")
    number: str = Field(..., description="Document number")
    notes: Optional[str] = Field(default=None, description="Document notes")
    items: List[DocumentItem] = Field(..., description="Document items")
    payments: Optional[List[DocumentPayment]] = Field(default=None, description="Document payments")
    currency: str = Field(..., description="Document currency")
    exchange_rate: float = Field(..., description="Exchange rate")
    due_date: Optional[datetime] = Field(default=None, description="Due date")
    reference: Optional[str] = Field(default=None, description="Document reference")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    shipping_address: Optional[Dict[str, Any]] = Field(default=None, description="Shipping address")
    billing_address: Optional[Dict[str, Any]] = Field(default=None, description="Billing address")
    salesperson_id: Optional[str] = Field(default=None, description="Salesperson ID")
    tags: Optional[List[str]] = Field(default=None, description="Document tags")
    language: Optional[str] = Field(default=None, description="Document language")
    payment_method: Optional[Union[PaymentMethod, str]] = Field(default=None, description="Default payment method")
    payment_terms: Optional[int] = Field(default=None, description="Payment terms in days")
    taxes: Optional[List[DocumentTax]] = Field(default=None, description="Document taxes")
    discount: Optional[float] = Field(default=None, description="Global discount percentage")
    series_id: Optional[str] = Field(default=None, description="Numbering series ID")
    total: float = Field(..., description="Document total amount")
    subtotal: float = Field(..., description="Document subtotal amount")
    tax_amount: Optional[float] = Field(default=None, description="Total tax amount")
    discount_amount: Optional[float] = Field(default=None, description="Total discount amount")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")
    contact_name: Optional[str] = Field(default=None, description="Contact name")
    contact_email: Optional[str] = Field(default=None, description="Contact email")
    public_link: Optional[str] = Field(default=None, description="Public link to the document")
    pdf_link: Optional[str] = Field(default=None, description="Link to download the PDF")


class DocumentListParams(PaginationParams, DateRangeParams):
    """Parameters for listing documents."""
    
    type: Optional[DocumentType] = Field(default=None, description="Filter by document type")
    status: Optional[DocumentStatus] = Field(default=None, description="Filter by document status")
    contact_id: Optional[str] = Field(default=None, description="Filter by contact ID")
    query: Optional[str] = Field(default=None, description="Search query")
    min_amount: Optional[float] = Field(default=None, description="Filter by minimum amount")
    max_amount: Optional[float] = Field(default=None, description="Filter by maximum amount")
    salesperson_id: Optional[str] = Field(default=None, description="Filter by salesperson ID")
    tags: Optional[List[str]] = Field(default=None, description="Filter by tags")
    series_id: Optional[str] = Field(default=None, description="Filter by numbering series ID")
    payment_method: Optional[Union[PaymentMethod, str]] = Field(default=None, description="Filter by payment method")
    due_date_start: Optional[datetime] = Field(default=None, description="Filter by due date start")
    due_date_end: Optional[datetime] = Field(default=None, description="Filter by due date end")


class DocumentSendParams(BaseModel):
    """Parameters for sending a document."""
    
    email: str = Field(..., description="Recipient email")
    subject: Optional[str] = Field(default=None, description="Email subject")
    message: Optional[str] = Field(default=None, description="Email message")
    cc: Optional[List[str]] = Field(default=None, description="CC recipients")
    bcc: Optional[List[str]] = Field(default=None, description="BCC recipients")
    attach_pdf: Optional[bool] = Field(default=True, description="Whether to attach the PDF")
    include_payment_link: Optional[bool] = Field(default=False, description="Whether to include a payment link")


class DocumentAttachment(BaseModel):
    """Document attachment model."""
    
    id: str = Field(..., description="Attachment ID")
    name: str = Field(..., description="Attachment name")
    size: Optional[int] = Field(default=None, description="Attachment size in bytes")
    type: Optional[str] = Field(default=None, description="Attachment MIME type")
    url: Optional[str] = Field(default=None, description="Attachment URL")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")


class DocumentAttachmentUpload(BaseModel):
    """Parameters for uploading a document attachment."""
    
    name: str = Field(..., description="Attachment name")
    file: str = Field(..., description="Base64 encoded file content")
    type: Optional[str] = Field(default=None, description="Attachment MIME type")


class DocumentPaymentCreate(BaseModel):
    """Model for creating a document payment."""
    
    date: datetime = Field(..., description="Payment date")
    amount: float = Field(..., description="Payment amount")
    method: Union[PaymentMethod, str] = Field(..., description="Payment method")
    notes: Optional[str] = Field(default=None, description="Payment notes")
    account_id: Optional[str] = Field(default=None, description="Treasury account ID")
    create_transaction: Optional[bool] = Field(default=False, description="Whether to create a treasury transaction")


class DocumentStatusUpdate(BaseModel):
    """Model for updating a document status."""
    
    status: DocumentStatus = Field(..., description="New document status")


# Response models
class DocumentResponse(BaseResponse):
    """Response model for a single document."""
    
    document: Document = Field(..., description="Document data")


class DocumentListResponse(BaseResponse):
    """Response model for a list of documents."""
    
    items: List[Document] = Field(..., description="List of documents")
    total: Optional[int] = Field(default=None, description="Total number of documents")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class DocumentSendResponse(BaseResponse):
    """Response model for sending a document."""
    
    sent: bool = Field(..., description="Whether the document was sent successfully")
    message: Optional[str] = Field(default=None, description="Response message")


class DocumentAttachmentResponse(BaseResponse):
    """Response model for a single document attachment."""
    
    attachment: DocumentAttachment = Field(..., description="Attachment data")


class DocumentAttachmentListResponse(BaseResponse):
    """Response model for a list of document attachments."""
    
    items: List[DocumentAttachment] = Field(..., description="List of attachments")
    total: Optional[int] = Field(default=None, description="Total number of attachments")


class DocumentPaymentResponse(BaseResponse):
    """Response model for a document payment."""
    
    payment: DocumentPayment = Field(..., description="Payment data")
    transaction_id: Optional[str] = Field(default=None, description="Created treasury transaction ID")


class DocumentPaymentListResponse(BaseResponse):
    """Response model for a list of document payments."""
    
    items: List[DocumentPayment] = Field(..., description="List of payments")
    total: Optional[int] = Field(default=None, description="Total number of payments") 