"""
Models for the Projects API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class ProjectCreate(BaseModel):
    """Model for creating a project."""
    
    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(default=None, description="Project description")
    contact_id: Optional[str] = Field(default=None, description="Contact ID")
    start_date: Optional[datetime] = Field(default=None, description="Project start date")
    end_date: Optional[datetime] = Field(default=None, description="Project end date")
    budget: Optional[float] = Field(default=None, description="Project budget")
    status: Optional[str] = Field(default=None, description="Project status")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class ProjectUpdate(BaseModel):
    """Model for updating a project."""
    
    name: Optional[str] = Field(default=None, description="Project name")
    description: Optional[str] = Field(default=None, description="Project description")
    contact_id: Optional[str] = Field(default=None, description="Contact ID")
    start_date: Optional[datetime] = Field(default=None, description="Project start date")
    end_date: Optional[datetime] = Field(default=None, description="Project end date")
    budget: Optional[float] = Field(default=None, description="Project budget")
    status: Optional[str] = Field(default=None, description="Project status")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class Project(ProjectCreate):
    """Project model."""
    
    id: str = Field(..., description="Project ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class ProjectListParams(PaginationParams, DateRangeParams):
    """Parameters for listing projects."""
    
    status: Optional[str] = Field(default=None, description="Filter by project status")
    contact_id: Optional[str] = Field(default=None, description="Filter by contact ID")
    query: Optional[str] = Field(default=None, description="Search query")


class ProjectSummary(BaseModel):
    """Project summary model."""
    
    total_tasks: int = Field(..., description="Total number of tasks")
    completed_tasks: int = Field(..., description="Number of completed tasks")
    total_time: float = Field(..., description="Total time spent in hours")
    budget_spent: Optional[float] = Field(default=None, description="Budget spent")
    budget_remaining: Optional[float] = Field(default=None, description="Budget remaining")


class ProjectTaskCreate(BaseModel):
    """Model for creating a project task."""
    
    name: str = Field(..., description="Task name")
    description: Optional[str] = Field(default=None, description="Task description")
    project_id: str = Field(..., description="Project ID")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    due_date: Optional[datetime] = Field(default=None, description="Task due date")
    status: Optional[str] = Field(default=None, description="Task status")
    priority: Optional[str] = Field(default=None, description="Task priority")
    estimated_hours: Optional[float] = Field(default=None, description="Estimated hours")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class ProjectTaskUpdate(BaseModel):
    """Model for updating a project task."""
    
    name: Optional[str] = Field(default=None, description="Task name")
    description: Optional[str] = Field(default=None, description="Task description")
    project_id: Optional[str] = Field(default=None, description="Project ID")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    due_date: Optional[datetime] = Field(default=None, description="Task due date")
    status: Optional[str] = Field(default=None, description="Task status")
    priority: Optional[str] = Field(default=None, description="Task priority")
    estimated_hours: Optional[float] = Field(default=None, description="Estimated hours")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class ProjectTask(ProjectTaskCreate):
    """Project task model."""
    
    id: str = Field(..., description="Task ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class ProjectTaskListParams(PaginationParams):
    """Parameters for listing project tasks."""
    
    project_id: Optional[str] = Field(default=None, description="Filter by project ID")
    assignee_id: Optional[str] = Field(default=None, description="Filter by assignee ID")
    status: Optional[str] = Field(default=None, description="Filter by task status")
    priority: Optional[str] = Field(default=None, description="Filter by task priority")
    query: Optional[str] = Field(default=None, description="Search query")


class TimeTrackingCreate(BaseModel):
    """Model for creating a time tracking entry."""
    
    project_id: str = Field(..., description="Project ID")
    task_id: Optional[str] = Field(default=None, description="Task ID")
    user_id: Optional[str] = Field(default=None, description="User ID")
    date: datetime = Field(..., description="Time tracking date")
    hours: float = Field(..., description="Hours spent")
    description: Optional[str] = Field(default=None, description="Time tracking description")
    billable: Optional[bool] = Field(default=None, description="Whether the time is billable")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class TimeTrackingUpdate(BaseModel):
    """Model for updating a time tracking entry."""
    
    project_id: Optional[str] = Field(default=None, description="Project ID")
    task_id: Optional[str] = Field(default=None, description="Task ID")
    user_id: Optional[str] = Field(default=None, description="User ID")
    date: Optional[datetime] = Field(default=None, description="Time tracking date")
    hours: Optional[float] = Field(default=None, description="Hours spent")
    description: Optional[str] = Field(default=None, description="Time tracking description")
    billable: Optional[bool] = Field(default=None, description="Whether the time is billable")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class TimeTracking(TimeTrackingCreate):
    """Time tracking model."""
    
    id: str = Field(..., description="Time tracking ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class TimeTrackingListParams(PaginationParams, DateRangeParams):
    """Parameters for listing time tracking entries."""
    
    project_id: Optional[str] = Field(default=None, description="Filter by project ID")
    task_id: Optional[str] = Field(default=None, description="Filter by task ID")
    user_id: Optional[str] = Field(default=None, description="Filter by user ID")
    billable: Optional[bool] = Field(default=None, description="Filter by billable status")
    query: Optional[str] = Field(default=None, description="Search query")


# Response models
class ProjectResponse(BaseResponse, Project):
    """Response model for a single project."""
    pass


class ProjectListResponse(BaseResponse):
    """Response model for a list of projects."""
    
    items: List[Project] = Field(..., description="List of projects")
    total: Optional[int] = Field(default=None, description="Total number of projects")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class ProjectSummaryResponse(BaseResponse, ProjectSummary):
    """Response model for a project summary."""
    pass


class ProjectTaskResponse(BaseResponse, ProjectTask):
    """Response model for a single project task."""
    pass


class ProjectTaskListResponse(BaseResponse):
    """Response model for a list of project tasks."""
    
    items: List[ProjectTask] = Field(..., description="List of tasks")
    total: Optional[int] = Field(default=None, description="Total number of tasks")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class TimeTrackingResponse(BaseResponse, TimeTracking):
    """Response model for a single time tracking entry."""
    pass


class TimeTrackingListResponse(BaseResponse):
    """Response model for a list of time tracking entries."""
    
    items: List[TimeTracking] = Field(..., description="List of time tracking entries")
    total: Optional[int] = Field(default=None, description="Total number of time tracking entries")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page") 