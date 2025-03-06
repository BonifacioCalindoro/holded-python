"""
Models for the Projects API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from enum import Enum

from pydantic import Field, field_validator

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class ProjectStatus(str, Enum):
    """Project status enum."""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class ProjectTaskStatus(str, Enum):
    """Project task status enum."""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    DONE = "done"
    CANCELLED = "cancelled"


class TaskPriority(str, Enum):
    """Task priority enum."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class BillingType(str, Enum):
    """Project billing type enum."""
    HOURLY = "hourly"
    FIXED = "fixed"
    NON_BILLABLE = "non_billable"


class ProjectMember(BaseModel):
    """Project member model."""
    
    user_id: str = Field(..., description="User ID")
    user_name: Optional[str] = Field(default=None, description="User name")
    role: Optional[str] = Field(default=None, description="Member role")
    hourly_rate: Optional[float] = Field(default=None, description="Hourly rate")
    is_manager: Optional[bool] = Field(default=False, description="Whether the member is a project manager")


class ProjectCreate(BaseModel):
    """Model for creating a project."""
    
    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(default=None, description="Project description")
    contact_id: Optional[str] = Field(default=None, description="Contact ID")
    start_date: Optional[datetime] = Field(default=None, description="Project start date")
    end_date: Optional[datetime] = Field(default=None, description="Project end date")
    budget: Optional[float] = Field(default=None, description="Project budget")
    status: Optional[ProjectStatus] = Field(default=ProjectStatus.NOT_STARTED, description="Project status")
    billing_type: Optional[BillingType] = Field(default=BillingType.HOURLY, description="Project billing type")
    hourly_rate: Optional[float] = Field(default=None, description="Project hourly rate")
    currency: Optional[str] = Field(default="EUR", description="Project currency")
    members: Optional[List[ProjectMember]] = Field(default=None, description="Project members")
    tags: Optional[List[str]] = Field(default=None, description="Project tags")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    is_template: Optional[bool] = Field(default=False, description="Whether this is a project template")
    template_id: Optional[str] = Field(default=None, description="Template ID if creating from template")
    
    @field_validator('end_date')
    def validate_end_date(cls, v, values):
        """Validate that end_date is after start_date."""
        if v and 'start_date' in values.data and values.data['start_date'] and v < values.data['start_date']:
            raise ValueError("End date must be after start date")
        return v


class ProjectUpdate(BaseModel):
    """Model for updating a project."""
    
    name: Optional[str] = Field(default=None, description="Project name")
    description: Optional[str] = Field(default=None, description="Project description")
    contact_id: Optional[str] = Field(default=None, description="Contact ID")
    start_date: Optional[datetime] = Field(default=None, description="Project start date")
    end_date: Optional[datetime] = Field(default=None, description="Project end date")
    budget: Optional[float] = Field(default=None, description="Project budget")
    status: Optional[ProjectStatus] = Field(default=None, description="Project status")
    billing_type: Optional[BillingType] = Field(default=None, description="Project billing type")
    hourly_rate: Optional[float] = Field(default=None, description="Project hourly rate")
    currency: Optional[str] = Field(default=None, description="Project currency")
    members: Optional[List[ProjectMember]] = Field(default=None, description="Project members")
    tags: Optional[List[str]] = Field(default=None, description="Project tags")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    is_template: Optional[bool] = Field(default=None, description="Whether this is a project template")
    
    @field_validator('end_date')
    def validate_end_date(cls, v, values):
        """Validate that end_date is after start_date."""
        if v and 'start_date' in values.data and values.data['start_date'] and v < values.data['start_date']:
            raise ValueError("End date must be after start date")
        return v


class Project(BaseModel):
    """Project model."""
    
    id: str = Field(..., description="Project ID")
    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(default=None, description="Project description")
    contact_id: Optional[str] = Field(default=None, description="Contact ID")
    contact_name: Optional[str] = Field(default=None, description="Contact name")
    start_date: Optional[datetime] = Field(default=None, description="Project start date")
    end_date: Optional[datetime] = Field(default=None, description="Project end date")
    budget: Optional[float] = Field(default=None, description="Project budget")
    status: ProjectStatus = Field(..., description="Project status")
    billing_type: BillingType = Field(..., description="Project billing type")
    hourly_rate: Optional[float] = Field(default=None, description="Project hourly rate")
    currency: str = Field(..., description="Project currency")
    members: List[ProjectMember] = Field(default_factory=list, description="Project members")
    tags: Optional[List[str]] = Field(default=None, description="Project tags")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    is_template: bool = Field(default=False, description="Whether this is a project template")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")
    created_by_id: Optional[str] = Field(default=None, description="Creator ID")
    created_by_name: Optional[str] = Field(default=None, description="Creator name")
    progress_percentage: Optional[float] = Field(default=None, description="Project progress percentage")
    total_hours: Optional[float] = Field(default=None, description="Total hours logged")
    billable_hours: Optional[float] = Field(default=None, description="Billable hours logged")
    non_billable_hours: Optional[float] = Field(default=None, description="Non-billable hours logged")


class ProjectListParams(PaginationParams, DateRangeParams):
    """Parameters for listing projects."""
    
    status: Optional[ProjectStatus] = Field(default=None, description="Filter by project status")
    contact_id: Optional[str] = Field(default=None, description="Filter by contact ID")
    query: Optional[str] = Field(default=None, description="Search query")
    tags: Optional[List[str]] = Field(default=None, description="Filter by tags")
    member_id: Optional[str] = Field(default=None, description="Filter by member ID")
    billing_type: Optional[BillingType] = Field(default=None, description="Filter by billing type")
    is_template: Optional[bool] = Field(default=None, description="Filter by template status")
    start_date_start: Optional[datetime] = Field(default=None, description="Filter by start date (from)")
    start_date_end: Optional[datetime] = Field(default=None, description="Filter by start date (to)")
    end_date_start: Optional[datetime] = Field(default=None, description="Filter by end date (from)")
    end_date_end: Optional[datetime] = Field(default=None, description="Filter by end date (to)")


class ProjectSummary(BaseModel):
    """Project summary model."""
    
    total_tasks: int = Field(..., description="Total number of tasks")
    completed_tasks: int = Field(..., description="Number of completed tasks")
    total_time: float = Field(..., description="Total time spent in hours")
    billable_time: Optional[float] = Field(default=None, description="Billable time spent in hours")
    non_billable_time: Optional[float] = Field(default=None, description="Non-billable time spent in hours")
    budget_spent: Optional[float] = Field(default=None, description="Budget spent")
    budget_remaining: Optional[float] = Field(default=None, description="Budget remaining")
    budget_percentage: Optional[float] = Field(default=None, description="Budget spent percentage")
    progress_percentage: Optional[float] = Field(default=None, description="Project progress percentage")
    days_remaining: Optional[int] = Field(default=None, description="Days remaining until deadline")
    is_overdue: Optional[bool] = Field(default=None, description="Whether the project is overdue")


class TaskAttachment(BaseModel):
    """Task attachment model."""
    
    id: str = Field(..., description="Attachment ID")
    name: str = Field(..., description="Attachment name")
    size: Optional[int] = Field(default=None, description="Attachment size in bytes")
    type: Optional[str] = Field(default=None, description="Attachment MIME type")
    url: Optional[str] = Field(default=None, description="Attachment URL")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    created_by_id: Optional[str] = Field(default=None, description="Creator ID")
    created_by_name: Optional[str] = Field(default=None, description="Creator name")


class TaskComment(BaseModel):
    """Task comment model."""
    
    id: str = Field(..., description="Comment ID")
    task_id: str = Field(..., description="Task ID")
    content: str = Field(..., description="Comment content")
    user_id: str = Field(..., description="User ID")
    user_name: Optional[str] = Field(default=None, description="User name")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")
    attachments: Optional[List[TaskAttachment]] = Field(default=None, description="Comment attachments")


class ProjectTaskCreate(BaseModel):
    """Model for creating a project task."""
    
    name: str = Field(..., description="Task name")
    description: Optional[str] = Field(default=None, description="Task description")
    project_id: str = Field(..., description="Project ID")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    due_date: Optional[datetime] = Field(default=None, description="Task due date")
    status: Optional[ProjectTaskStatus] = Field(default=ProjectTaskStatus.TODO, description="Task status")
    priority: Optional[TaskPriority] = Field(default=TaskPriority.MEDIUM, description="Task priority")
    estimated_hours: Optional[float] = Field(default=None, description="Estimated hours")
    parent_task_id: Optional[str] = Field(default=None, description="Parent task ID for subtasks")
    tags: Optional[List[str]] = Field(default=None, description="Task tags")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    is_billable: Optional[bool] = Field(default=True, description="Whether the task is billable")
    hourly_rate: Optional[float] = Field(default=None, description="Task hourly rate (overrides project rate)")


class ProjectTaskUpdate(BaseModel):
    """Model for updating a project task."""
    
    name: Optional[str] = Field(default=None, description="Task name")
    description: Optional[str] = Field(default=None, description="Task description")
    project_id: Optional[str] = Field(default=None, description="Project ID")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    due_date: Optional[datetime] = Field(default=None, description="Task due date")
    status: Optional[ProjectTaskStatus] = Field(default=None, description="Task status")
    priority: Optional[TaskPriority] = Field(default=None, description="Task priority")
    estimated_hours: Optional[float] = Field(default=None, description="Estimated hours")
    parent_task_id: Optional[str] = Field(default=None, description="Parent task ID for subtasks")
    tags: Optional[List[str]] = Field(default=None, description="Task tags")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    is_billable: Optional[bool] = Field(default=None, description="Whether the task is billable")
    hourly_rate: Optional[float] = Field(default=None, description="Task hourly rate (overrides project rate)")


class ProjectTask(BaseModel):
    """Project task model."""
    
    id: str = Field(..., description="Task ID")
    name: str = Field(..., description="Task name")
    description: Optional[str] = Field(default=None, description="Task description")
    project_id: str = Field(..., description="Project ID")
    project_name: Optional[str] = Field(default=None, description="Project name")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    assignee_name: Optional[str] = Field(default=None, description="Assignee name")
    due_date: Optional[datetime] = Field(default=None, description="Task due date")
    status: ProjectTaskStatus = Field(..., description="Task status")
    priority: TaskPriority = Field(..., description="Task priority")
    estimated_hours: Optional[float] = Field(default=None, description="Estimated hours")
    actual_hours: Optional[float] = Field(default=None, description="Actual hours spent")
    parent_task_id: Optional[str] = Field(default=None, description="Parent task ID for subtasks")
    parent_task_name: Optional[str] = Field(default=None, description="Parent task name")
    subtasks: Optional[List['ProjectTask']] = Field(default=None, description="Subtasks")
    tags: Optional[List[str]] = Field(default=None, description="Task tags")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    is_billable: bool = Field(default=True, description="Whether the task is billable")
    hourly_rate: Optional[float] = Field(default=None, description="Task hourly rate")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")
    created_by_id: Optional[str] = Field(default=None, description="Creator ID")
    created_by_name: Optional[str] = Field(default=None, description="Creator name")
    comments: Optional[List[TaskComment]] = Field(default=None, description="Task comments")
    attachments: Optional[List[TaskAttachment]] = Field(default=None, description="Task attachments")
    is_overdue: Optional[bool] = Field(default=None, description="Whether the task is overdue")
    completion_percentage: Optional[float] = Field(default=None, description="Task completion percentage")


class ProjectTaskListParams(PaginationParams, DateRangeParams):
    """Parameters for listing project tasks."""
    
    project_id: Optional[str] = Field(default=None, description="Filter by project ID")
    assignee_id: Optional[str] = Field(default=None, description="Filter by assignee ID")
    status: Optional[ProjectTaskStatus] = Field(default=None, description="Filter by task status")
    priority: Optional[TaskPriority] = Field(default=None, description="Filter by task priority")
    query: Optional[str] = Field(default=None, description="Search query")
    tags: Optional[List[str]] = Field(default=None, description="Filter by tags")
    parent_task_id: Optional[str] = Field(default=None, description="Filter by parent task ID")
    is_billable: Optional[bool] = Field(default=None, description="Filter by billable status")
    due_date_start: Optional[datetime] = Field(default=None, description="Filter by due date (from)")
    due_date_end: Optional[datetime] = Field(default=None, description="Filter by due date (to)")
    is_overdue: Optional[bool] = Field(default=None, description="Filter by overdue status")


class TaskCommentCreate(BaseModel):
    """Model for creating a task comment."""
    
    content: str = Field(..., description="Comment content")
    attachments: Optional[List[Dict[str, Any]]] = Field(default=None, description="Comment attachments")


class TaskCommentUpdate(BaseModel):
    """Model for updating a task comment."""
    
    content: Optional[str] = Field(default=None, description="Comment content")


class TaskAttachmentUpload(BaseModel):
    """Parameters for uploading a task attachment."""
    
    name: str = Field(..., description="Attachment name")
    file: str = Field(..., description="Base64 encoded file content")
    type: Optional[str] = Field(default=None, description="Attachment MIME type")


class TimeTrackingCreate(BaseModel):
    """Model for creating a time tracking entry."""
    
    project_id: str = Field(..., description="Project ID")
    task_id: Optional[str] = Field(default=None, description="Task ID")
    user_id: Optional[str] = Field(default=None, description="User ID")
    date: datetime = Field(..., description="Time tracking date")
    hours: float = Field(..., description="Hours spent")
    description: Optional[str] = Field(default=None, description="Time tracking description")
    billable: Optional[bool] = Field(default=True, description="Whether the time is billable")
    hourly_rate: Optional[float] = Field(default=None, description="Hourly rate for this entry")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    
    @field_validator('hours')
    def validate_hours(cls, v):
        """Validate that hours is positive."""
        if v <= 0:
            raise ValueError("Hours must be positive")
        return v


class TimeTrackingUpdate(BaseModel):
    """Model for updating a time tracking entry."""
    
    project_id: Optional[str] = Field(default=None, description="Project ID")
    task_id: Optional[str] = Field(default=None, description="Task ID")
    user_id: Optional[str] = Field(default=None, description="User ID")
    date: Optional[datetime] = Field(default=None, description="Time tracking date")
    hours: Optional[float] = Field(default=None, description="Hours spent")
    description: Optional[str] = Field(default=None, description="Time tracking description")
    billable: Optional[bool] = Field(default=None, description="Whether the time is billable")
    hourly_rate: Optional[float] = Field(default=None, description="Hourly rate for this entry")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    
    @field_validator('hours')
    def validate_hours(cls, v):
        """Validate that hours is positive."""
        if v is not None and v <= 0:
            raise ValueError("Hours must be positive")
        return v


class TimeTracking(BaseModel):
    """Time tracking model."""
    
    id: str = Field(..., description="Time tracking ID")
    project_id: str = Field(..., description="Project ID")
    project_name: Optional[str] = Field(default=None, description="Project name")
    task_id: Optional[str] = Field(default=None, description="Task ID")
    task_name: Optional[str] = Field(default=None, description="Task name")
    user_id: str = Field(..., description="User ID")
    user_name: Optional[str] = Field(default=None, description="User name")
    date: datetime = Field(..., description="Time tracking date")
    hours: float = Field(..., description="Hours spent")
    description: Optional[str] = Field(default=None, description="Time tracking description")
    billable: bool = Field(..., description="Whether the time is billable")
    hourly_rate: Optional[float] = Field(default=None, description="Hourly rate for this entry")
    amount: Optional[float] = Field(default=None, description="Calculated amount (hours * hourly_rate)")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")
    created_by_id: Optional[str] = Field(default=None, description="Creator ID")
    created_by_name: Optional[str] = Field(default=None, description="Creator name")


class TimeTrackingListParams(PaginationParams, DateRangeParams):
    """Parameters for listing time tracking entries."""
    
    project_id: Optional[str] = Field(default=None, description="Filter by project ID")
    task_id: Optional[str] = Field(default=None, description="Filter by task ID")
    user_id: Optional[str] = Field(default=None, description="Filter by user ID")
    billable: Optional[bool] = Field(default=None, description="Filter by billable status")
    query: Optional[str] = Field(default=None, description="Search query")
    min_hours: Optional[float] = Field(default=None, description="Filter by minimum hours")
    max_hours: Optional[float] = Field(default=None, description="Filter by maximum hours")
    date_start: Optional[datetime] = Field(default=None, description="Filter by date (from)")
    date_end: Optional[datetime] = Field(default=None, description="Filter by date (to)")


class TimeTrackingSummary(BaseModel):
    """Time tracking summary model."""
    
    total_hours: float = Field(..., description="Total hours")
    billable_hours: float = Field(..., description="Billable hours")
    non_billable_hours: float = Field(..., description="Non-billable hours")
    total_amount: Optional[float] = Field(default=None, description="Total amount")
    by_project: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, description="Hours by project")
    by_user: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, description="Hours by user")
    by_date: Optional[Dict[str, float]] = Field(default=None, description="Hours by date")


# Response models
class ProjectResponse(BaseResponse):
    """Response model for a single project."""
    
    project: Project = Field(..., description="Project data")


class ProjectListResponse(BaseResponse):
    """Response model for a list of projects."""
    
    items: List[Project] = Field(..., description="List of projects")
    total: Optional[int] = Field(default=None, description="Total number of projects")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class ProjectSummaryResponse(BaseResponse):
    """Response model for a project summary."""
    
    summary: ProjectSummary = Field(..., description="Project summary data")


class ProjectTaskResponse(BaseResponse):
    """Response model for a single project task."""
    
    task: ProjectTask = Field(..., description="Task data")


class ProjectTaskListResponse(BaseResponse):
    """Response model for a list of project tasks."""
    
    items: List[ProjectTask] = Field(..., description="List of tasks")
    total: Optional[int] = Field(default=None, description="Total number of tasks")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class TaskCommentResponse(BaseResponse):
    """Response model for a single task comment."""
    
    comment: TaskComment = Field(..., description="Comment data")


class TaskCommentListResponse(BaseResponse):
    """Response model for a list of task comments."""
    
    items: List[TaskComment] = Field(..., description="List of comments")
    total: Optional[int] = Field(default=None, description="Total number of comments")


class TaskAttachmentResponse(BaseResponse):
    """Response model for a single task attachment."""
    
    attachment: TaskAttachment = Field(..., description="Attachment data")


class TaskAttachmentListResponse(BaseResponse):
    """Response model for a list of task attachments."""
    
    items: List[TaskAttachment] = Field(..., description="List of attachments")
    total: Optional[int] = Field(default=None, description="Total number of attachments")


class TimeTrackingResponse(BaseResponse):
    """Response model for a single time tracking entry."""
    
    time_tracking: TimeTracking = Field(..., description="Time tracking data")


class TimeTrackingListResponse(BaseResponse):
    """Response model for a list of time tracking entries."""
    
    items: List[TimeTracking] = Field(..., description="List of time tracking entries")
    total: Optional[int] = Field(default=None, description="Total number of time tracking entries")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class TimeTrackingSummaryResponse(BaseResponse):
    """Response model for a time tracking summary."""
    
    summary: TimeTrackingSummary = Field(..., description="Time tracking summary data") 