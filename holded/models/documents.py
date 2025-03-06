"""
Models for the Documents API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class DocumentItem(BaseModel):
    """Document item model."""
    
    name: str = Field(..., description="Item name")
    units: float = Field(..., description="Number of units")
    price: float = Field(..., description="Unit price")
    discount: Optional[float] = Field(default=None, description="Discount percentage")
    tax: Optional[float] = Field(default=None, description="Tax percentage")
    description: Optional[str] = Field(default=None, description="Item description")
    product_id: Optional[str] = Field(default=None, description="Product ID if linked to a product")


class DocumentPayment(BaseModel):
    """Document payment model."""
    
    date: datetime = Field(..., description="Payment date")
    amount: float = Field(..., description="Payment amount")
    method: str = Field(..., description="Payment method")
    notes: Optional[str] = Field(default=None, description="Payment notes")


class DocumentCreate(BaseModel):
    """Model for creating a document."""
    
    contact_id: str = Field(..., description="Contact ID")
    date: datetime = Field(..., description="Document date")
    number: Optional[str] = Field(default=None, description="Document number")
    notes: Optional[str] = Field(default=None, description="Document notes")
    items: List[DocumentItem] = Field(..., description="Document items")
    payments: Optional[List[DocumentPayment]] = Field(default=None, description="Document payments")
    currency: Optional[str] = Field(default=None, description="Document currency")
    exchange_rate: Optional[float] = Field(default=None, description="Exchange rate")
    due_date: Optional[datetime] = Field(default=None, description="Due date")
    reference: Optional[str] = Field(default=None, description="Document reference")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


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


class Document(DocumentCreate):
    """Document model."""
    
    id: str = Field(..., description="Document ID")
    type: str = Field(..., description="Document type (invoice, order, etc.)")
    status: str = Field(..., description="Document status")
    total: float = Field(..., description="Document total amount")
    tax_amount: Optional[float] = Field(default=None, description="Total tax amount")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class DocumentListParams(PaginationParams, DateRangeParams):
    """Parameters for listing documents."""
    
    type: Optional[str] = Field(default=None, description="Filter by document type")
    status: Optional[str] = Field(default=None, description="Filter by document status")
    contact_id: Optional[str] = Field(default=None, description="Filter by contact ID")
    query: Optional[str] = Field(default=None, description="Search query")


class DocumentSendParams(BaseModel):
    """Parameters for sending a document."""
    
    email: str = Field(..., description="Recipient email")
    subject: Optional[str] = Field(default=None, description="Email subject")
    message: Optional[str] = Field(default=None, description="Email message")
    cc: Optional[List[str]] = Field(default=None, description="CC recipients")
    bcc: Optional[List[str]] = Field(default=None, description="BCC recipients")


class DocumentAttachment(BaseModel):
    """Document attachment model."""
    
    id: str = Field(..., description="Attachment ID")
    name: str = Field(..., description="Attachment name")
    size: Optional[int] = Field(default=None, description="Attachment size in bytes")
    type: Optional[str] = Field(default=None, description="Attachment MIME type")
    url: Optional[str] = Field(default=None, description="Attachment URL")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")


# Response models
class DocumentResponse(BaseResponse, Document):
    """Response model for a single document."""
    pass


class DocumentListResponse(BaseResponse):
    """Response model for a list of documents."""
    
    items: List[Document] = Field(..., description="List of documents")
    total: Optional[int] = Field(default=None, description="Total number of documents")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class DocumentSendResponse(BaseResponse):
    """Response model for sending a document."""
    
    message: Optional[str] = Field(default=None, description="Response message")


class DocumentAttachmentListResponse(BaseResponse):
    """Response model for a list of document attachments."""
    
    items: List[DocumentAttachment] = Field(..., description="List of attachments")


class DocumentAttachmentResponse(BaseResponse, DocumentAttachment):
    """Response model for a single document attachment."""
    pass 