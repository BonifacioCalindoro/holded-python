"""
Models for the CRM API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from enum import Enum

from pydantic import Field, field_validator

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class LeadStage(str, Enum):
    """Lead stage enum."""
    NEW = "new"
    QUALIFIED = "qualified"
    PROPOSAL = "proposal"
    NEGOTIATION = "negotiation"
    WON = "won"
    LOST = "lost"


class TaskPriority(str, Enum):
    """Task priority enum."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class TaskStatus(str, Enum):
    """Task status enum."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class FunnelCreate(BaseModel):
    """Model for creating a funnel."""
    
    name: str = Field(..., description="Funnel name")
    description: Optional[str] = Field(default=None, description="Funnel description")
    stages: List[str] = Field(..., description="Funnel stages")
    color: Optional[str] = Field(default=None, description="Funnel color (hex code)")
    is_default: Optional[bool] = Field(default=False, description="Whether this is the default funnel")


class FunnelUpdate(BaseModel):
    """Model for updating a funnel."""
    
    name: Optional[str] = Field(default=None, description="Funnel name")
    description: Optional[str] = Field(default=None, description="Funnel description")
    stages: Optional[List[str]] = Field(default=None, description="Funnel stages")
    color: Optional[str] = Field(default=None, description="Funnel color (hex code)")
    is_default: Optional[bool] = Field(default=None, description="Whether this is the default funnel")


class Funnel(BaseModel):
    """Funnel model."""
    
    id: str = Field(..., description="Funnel ID")
    name: str = Field(..., description="Funnel name")
    description: Optional[str] = Field(default=None, description="Funnel description")
    stages: List[str] = Field(..., description="Funnel stages")
    color: Optional[str] = Field(default=None, description="Funnel color (hex code)")
    is_default: Optional[bool] = Field(default=False, description="Whether this is the default funnel")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")
    lead_count: Optional[int] = Field(default=None, description="Number of leads in this funnel")
    stage_counts: Optional[Dict[str, int]] = Field(default=None, description="Number of leads in each stage")


class FunnelListParams(PaginationParams):
    """Parameters for listing funnels."""
    
    query: Optional[str] = Field(default=None, description="Search query")
    is_default: Optional[bool] = Field(default=None, description="Filter by default status")


class LeadCreate(BaseModel):
    """Model for creating a lead."""
    
    name: str = Field(..., description="Lead name")
    contact_id: Optional[str] = Field(default=None, description="Contact ID")
    funnel_id: str = Field(..., description="Funnel ID")
    stage: str = Field(..., description="Lead stage")
    value: Optional[float] = Field(default=None, description="Lead value")
    description: Optional[str] = Field(default=None, description="Lead description")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    expected_close_date: Optional[datetime] = Field(default=None, description="Expected close date")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    tags: Optional[List[str]] = Field(default=None, description="Lead tags")
    source: Optional[str] = Field(default=None, description="Lead source")
    probability: Optional[int] = Field(default=None, description="Win probability percentage (0-100)")
    currency: Optional[str] = Field(default="EUR", description="Lead value currency")
    company_name: Optional[str] = Field(default=None, description="Company name if no contact is linked")
    email: Optional[str] = Field(default=None, description="Email if no contact is linked")
    phone: Optional[str] = Field(default=None, description="Phone if no contact is linked")


class LeadUpdate(BaseModel):
    """Model for updating a lead."""
    
    name: Optional[str] = Field(default=None, description="Lead name")
    contact_id: Optional[str] = Field(default=None, description="Contact ID")
    funnel_id: Optional[str] = Field(default=None, description="Funnel ID")
    stage: Optional[str] = Field(default=None, description="Lead stage")
    value: Optional[float] = Field(default=None, description="Lead value")
    description: Optional[str] = Field(default=None, description="Lead description")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    expected_close_date: Optional[datetime] = Field(default=None, description="Expected close date")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    tags: Optional[List[str]] = Field(default=None, description="Lead tags")
    source: Optional[str] = Field(default=None, description="Lead source")
    probability: Optional[int] = Field(default=None, description="Win probability percentage (0-100)")
    currency: Optional[str] = Field(default=None, description="Lead value currency")
    company_name: Optional[str] = Field(default=None, description="Company name if no contact is linked")
    email: Optional[str] = Field(default=None, description="Email if no contact is linked")
    phone: Optional[str] = Field(default=None, description="Phone if no contact is linked")


class Lead(BaseModel):
    """Lead model."""
    
    id: str = Field(..., description="Lead ID")
    name: str = Field(..., description="Lead name")
    contact_id: Optional[str] = Field(default=None, description="Contact ID")
    contact_name: Optional[str] = Field(default=None, description="Contact name")
    funnel_id: str = Field(..., description="Funnel ID")
    funnel_name: Optional[str] = Field(default=None, description="Funnel name")
    stage: str = Field(..., description="Lead stage")
    value: Optional[float] = Field(default=None, description="Lead value")
    description: Optional[str] = Field(default=None, description="Lead description")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    assignee_name: Optional[str] = Field(default=None, description="Assignee name")
    expected_close_date: Optional[datetime] = Field(default=None, description="Expected close date")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    tags: Optional[List[str]] = Field(default=None, description="Lead tags")
    source: Optional[str] = Field(default=None, description="Lead source")
    probability: Optional[int] = Field(default=None, description="Win probability percentage (0-100)")
    currency: Optional[str] = Field(default="EUR", description="Lead value currency")
    company_name: Optional[str] = Field(default=None, description="Company name if no contact is linked")
    email: Optional[str] = Field(default=None, description="Email if no contact is linked")
    phone: Optional[str] = Field(default=None, description="Phone if no contact is linked")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")
    last_activity_at: Optional[datetime] = Field(default=None, description="Last activity date")
    task_count: Optional[int] = Field(default=None, description="Number of tasks")
    note_count: Optional[int] = Field(default=None, description="Number of notes")
    document_count: Optional[int] = Field(default=None, description="Number of documents")


class LeadListParams(PaginationParams, DateRangeParams):
    """Parameters for listing leads."""
    
    funnel_id: Optional[str] = Field(default=None, description="Filter by funnel ID")
    stage: Optional[str] = Field(default=None, description="Filter by stage")
    contact_id: Optional[str] = Field(default=None, description="Filter by contact ID")
    assignee_id: Optional[str] = Field(default=None, description="Filter by assignee ID")
    query: Optional[str] = Field(default=None, description="Search query")
    tags: Optional[List[str]] = Field(default=None, description="Filter by tags")
    source: Optional[str] = Field(default=None, description="Filter by source")
    min_value: Optional[float] = Field(default=None, description="Filter by minimum value")
    max_value: Optional[float] = Field(default=None, description="Filter by maximum value")
    min_probability: Optional[int] = Field(default=None, description="Filter by minimum probability")
    max_probability: Optional[int] = Field(default=None, description="Filter by maximum probability")
    expected_close_date_start: Optional[datetime] = Field(default=None, description="Filter by expected close date start")
    expected_close_date_end: Optional[datetime] = Field(default=None, description="Filter by expected close date end")


class LeadNoteCreate(BaseModel):
    """Model for creating a lead note."""
    
    content: str = Field(..., description="Note content")
    user_id: Optional[str] = Field(default=None, description="User ID")
    pinned: Optional[bool] = Field(default=False, description="Whether the note is pinned")


class LeadNoteUpdate(BaseModel):
    """Model for updating a lead note."""
    
    content: Optional[str] = Field(default=None, description="Note content")
    pinned: Optional[bool] = Field(default=None, description="Whether the note is pinned")


class LeadNote(BaseModel):
    """Lead note model."""
    
    id: str = Field(..., description="Note ID")
    lead_id: str = Field(..., description="Lead ID")
    content: str = Field(..., description="Note content")
    user_id: Optional[str] = Field(default=None, description="User ID")
    user_name: Optional[str] = Field(default=None, description="User name")
    pinned: Optional[bool] = Field(default=False, description="Whether the note is pinned")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class LeadNoteListParams(PaginationParams):
    """Parameters for listing lead notes."""
    
    pinned: Optional[bool] = Field(default=None, description="Filter by pinned status")
    user_id: Optional[str] = Field(default=None, description="Filter by user ID")


class LeadTaskCreate(BaseModel):
    """Model for creating a lead task."""
    
    title: str = Field(..., description="Task title")
    description: Optional[str] = Field(default=None, description="Task description")
    due_date: Optional[datetime] = Field(default=None, description="Due date")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    priority: Optional[TaskPriority] = Field(default=TaskPriority.MEDIUM, description="Task priority")
    status: Optional[TaskStatus] = Field(default=TaskStatus.PENDING, description="Task status")
    reminder_date: Optional[datetime] = Field(default=None, description="Reminder date")


class LeadTaskUpdate(BaseModel):
    """Model for updating a lead task."""
    
    title: Optional[str] = Field(default=None, description="Task title")
    description: Optional[str] = Field(default=None, description="Task description")
    due_date: Optional[datetime] = Field(default=None, description="Due date")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    priority: Optional[TaskPriority] = Field(default=None, description="Task priority")
    status: Optional[TaskStatus] = Field(default=None, description="Task status")
    reminder_date: Optional[datetime] = Field(default=None, description="Reminder date")


class LeadTask(BaseModel):
    """Lead task model."""
    
    id: str = Field(..., description="Task ID")
    lead_id: str = Field(..., description="Lead ID")
    title: str = Field(..., description="Task title")
    description: Optional[str] = Field(default=None, description="Task description")
    due_date: Optional[datetime] = Field(default=None, description="Due date")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    assignee_name: Optional[str] = Field(default=None, description="Assignee name")
    priority: TaskPriority = Field(..., description="Task priority")
    status: TaskStatus = Field(..., description="Task status")
    reminder_date: Optional[datetime] = Field(default=None, description="Reminder date")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")
    completed_at: Optional[datetime] = Field(default=None, description="Completion date")
    created_by_id: Optional[str] = Field(default=None, description="Creator ID")
    created_by_name: Optional[str] = Field(default=None, description="Creator name")


class LeadTaskListParams(PaginationParams, DateRangeParams):
    """Parameters for listing lead tasks."""
    
    status: Optional[TaskStatus] = Field(default=None, description="Filter by status")
    priority: Optional[TaskPriority] = Field(default=None, description="Filter by priority")
    assignee_id: Optional[str] = Field(default=None, description="Filter by assignee ID")
    due_date_start: Optional[datetime] = Field(default=None, description="Filter by due date start")
    due_date_end: Optional[datetime] = Field(default=None, description="Filter by due date end")


class LeadDocumentLink(BaseModel):
    """Model for linking a document to a lead."""
    
    document_id: str = Field(..., description="Document ID")
    document_type: Optional[str] = Field(default=None, description="Document type")


class LeadDocument(BaseModel):
    """Lead document model."""
    
    id: str = Field(..., description="Link ID")
    lead_id: str = Field(..., description="Lead ID")
    document_id: str = Field(..., description="Document ID")
    document_type: str = Field(..., description="Document type")
    document_number: Optional[str] = Field(default=None, description="Document number")
    document_date: Optional[datetime] = Field(default=None, description="Document date")
    document_total: Optional[float] = Field(default=None, description="Document total")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")


class LeadDocumentListParams(PaginationParams):
    """Parameters for listing lead documents."""
    
    document_type: Optional[str] = Field(default=None, description="Filter by document type")


class LeadStageUpdate(BaseModel):
    """Model for updating a lead stage."""
    
    stage: str = Field(..., description="New stage")
    reason: Optional[str] = Field(default=None, description="Reason for the stage change")


class LeadConvertParams(BaseModel):
    """Parameters for converting a lead to a customer."""
    
    document_type: Optional[str] = Field(default="invoice", description="Document type to create")
    create_document: Optional[bool] = Field(default=False, description="Whether to create a document")


# Response models
class FunnelResponse(BaseResponse):
    """Response model for a single funnel."""
    
    funnel: Funnel = Field(..., description="Funnel data")


class FunnelListResponse(BaseResponse):
    """Response model for a list of funnels."""
    
    items: List[Funnel] = Field(..., description="List of funnels")
    total: Optional[int] = Field(default=None, description="Total number of funnels")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class LeadResponse(BaseResponse):
    """Response model for a single lead."""
    
    lead: Lead = Field(..., description="Lead data")


class LeadListResponse(BaseResponse):
    """Response model for a list of leads."""
    
    items: List[Lead] = Field(..., description="List of leads")
    total: Optional[int] = Field(default=None, description="Total number of leads")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class LeadNoteResponse(BaseResponse):
    """Response model for a single lead note."""
    
    note: LeadNote = Field(..., description="Note data")


class LeadNoteListResponse(BaseResponse):
    """Response model for a list of lead notes."""
    
    items: List[LeadNote] = Field(..., description="List of notes")
    total: Optional[int] = Field(default=None, description="Total number of notes")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class LeadTaskResponse(BaseResponse):
    """Response model for a single lead task."""
    
    task: LeadTask = Field(..., description="Task data")


class LeadTaskListResponse(BaseResponse):
    """Response model for a list of lead tasks."""
    
    items: List[LeadTask] = Field(..., description="List of tasks")
    total: Optional[int] = Field(default=None, description="Total number of tasks")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class LeadDocumentResponse(BaseResponse):
    """Response model for a single lead document."""
    
    document: LeadDocument = Field(..., description="Document link data")


class LeadDocumentListResponse(BaseResponse):
    """Response model for a list of lead documents."""
    
    items: List[LeadDocument] = Field(..., description="List of document links")
    total: Optional[int] = Field(default=None, description="Total number of document links")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class LeadConvertResponse(BaseResponse):
    """Response model for converting a lead."""
    
    contact_id: Optional[str] = Field(default=None, description="Created or linked contact ID")
    document_id: Optional[str] = Field(default=None, description="Created document ID")
    message: Optional[str] = Field(default=None, description="Response message") 