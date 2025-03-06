"""
Models for the CRM API.
"""
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field

from .base import BaseModel, BaseResponse, PaginationParams, DateRangeParams


class FunnelCreate(BaseModel):
    """Model for creating a funnel."""
    
    name: str = Field(..., description="Funnel name")
    description: Optional[str] = Field(default=None, description="Funnel description")
    stages: List[str] = Field(..., description="Funnel stages")


class FunnelUpdate(BaseModel):
    """Model for updating a funnel."""
    
    name: Optional[str] = Field(default=None, description="Funnel name")
    description: Optional[str] = Field(default=None, description="Funnel description")
    stages: Optional[List[str]] = Field(default=None, description="Funnel stages")


class Funnel(FunnelCreate):
    """Funnel model."""
    
    id: str = Field(..., description="Funnel ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


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


class Lead(LeadCreate):
    """Lead model."""
    
    id: str = Field(..., description="Lead ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class LeadListParams(PaginationParams, DateRangeParams):
    """Parameters for listing leads."""
    
    funnel_id: Optional[str] = Field(default=None, description="Filter by funnel ID")
    stage: Optional[str] = Field(default=None, description="Filter by stage")
    contact_id: Optional[str] = Field(default=None, description="Filter by contact ID")
    assignee_id: Optional[str] = Field(default=None, description="Filter by assignee ID")
    query: Optional[str] = Field(default=None, description="Search query")


class LeadNoteCreate(BaseModel):
    """Model for creating a lead note."""
    
    content: str = Field(..., description="Note content")
    user_id: Optional[str] = Field(default=None, description="User ID")


class LeadNote(LeadNoteCreate):
    """Lead note model."""
    
    id: str = Field(..., description="Note ID")
    lead_id: str = Field(..., description="Lead ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class LeadTaskCreate(BaseModel):
    """Model for creating a lead task."""
    
    title: str = Field(..., description="Task title")
    description: Optional[str] = Field(default=None, description="Task description")
    due_date: Optional[datetime] = Field(default=None, description="Task due date")
    assignee_id: Optional[str] = Field(default=None, description="Assignee ID")
    status: Optional[str] = Field(default=None, description="Task status")
    priority: Optional[str] = Field(default=None, description="Task priority")


class LeadTask(LeadTaskCreate):
    """Lead task model."""
    
    id: str = Field(..., description="Task ID")
    lead_id: str = Field(..., description="Lead ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class EventCreate(BaseModel):
    """Model for creating an event."""
    
    title: str = Field(..., description="Event title")
    description: Optional[str] = Field(default=None, description="Event description")
    start_date: datetime = Field(..., description="Event start date")
    end_date: datetime = Field(..., description="Event end date")
    location: Optional[str] = Field(default=None, description="Event location")
    attendees: Optional[List[str]] = Field(default=None, description="Event attendees (user IDs)")
    lead_id: Optional[str] = Field(default=None, description="Related lead ID")
    contact_id: Optional[str] = Field(default=None, description="Related contact ID")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class EventUpdate(BaseModel):
    """Model for updating an event."""
    
    title: Optional[str] = Field(default=None, description="Event title")
    description: Optional[str] = Field(default=None, description="Event description")
    start_date: Optional[datetime] = Field(default=None, description="Event start date")
    end_date: Optional[datetime] = Field(default=None, description="Event end date")
    location: Optional[str] = Field(default=None, description="Event location")
    attendees: Optional[List[str]] = Field(default=None, description="Event attendees (user IDs)")
    lead_id: Optional[str] = Field(default=None, description="Related lead ID")
    contact_id: Optional[str] = Field(default=None, description="Related contact ID")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class Event(EventCreate):
    """Event model."""
    
    id: str = Field(..., description="Event ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class EventListParams(PaginationParams, DateRangeParams):
    """Parameters for listing events."""
    
    lead_id: Optional[str] = Field(default=None, description="Filter by lead ID")
    contact_id: Optional[str] = Field(default=None, description="Filter by contact ID")
    attendee_id: Optional[str] = Field(default=None, description="Filter by attendee ID")
    query: Optional[str] = Field(default=None, description="Search query")


class BookingLocationCreate(BaseModel):
    """Model for creating a booking location."""
    
    name: str = Field(..., description="Location name")
    description: Optional[str] = Field(default=None, description="Location description")
    address: Optional[str] = Field(default=None, description="Location address")
    capacity: Optional[int] = Field(default=None, description="Location capacity")
    availability: Optional[Dict[str, List[str]]] = Field(default=None, description="Location availability by day of week")


class BookingLocationUpdate(BaseModel):
    """Model for updating a booking location."""
    
    name: Optional[str] = Field(default=None, description="Location name")
    description: Optional[str] = Field(default=None, description="Location description")
    address: Optional[str] = Field(default=None, description="Location address")
    capacity: Optional[int] = Field(default=None, description="Location capacity")
    availability: Optional[Dict[str, List[str]]] = Field(default=None, description="Location availability by day of week")


class BookingLocation(BookingLocationCreate):
    """Booking location model."""
    
    id: str = Field(..., description="Location ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class BookingSlot(BaseModel):
    """Booking slot model."""
    
    date: datetime = Field(..., description="Slot date")
    start_time: str = Field(..., description="Slot start time")
    end_time: str = Field(..., description="Slot end time")
    available: bool = Field(..., description="Whether the slot is available")


class BookingCreate(BaseModel):
    """Model for creating a booking."""
    
    location_id: str = Field(..., description="Location ID")
    date: datetime = Field(..., description="Booking date")
    start_time: str = Field(..., description="Booking start time")
    end_time: str = Field(..., description="Booking end time")
    title: str = Field(..., description="Booking title")
    description: Optional[str] = Field(default=None, description="Booking description")
    attendees: Optional[List[str]] = Field(default=None, description="Booking attendees (user IDs)")
    lead_id: Optional[str] = Field(default=None, description="Related lead ID")
    contact_id: Optional[str] = Field(default=None, description="Related contact ID")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class BookingUpdate(BaseModel):
    """Model for updating a booking."""
    
    location_id: Optional[str] = Field(default=None, description="Location ID")
    date: Optional[datetime] = Field(default=None, description="Booking date")
    start_time: Optional[str] = Field(default=None, description="Booking start time")
    end_time: Optional[str] = Field(default=None, description="Booking end time")
    title: Optional[str] = Field(default=None, description="Booking title")
    description: Optional[str] = Field(default=None, description="Booking description")
    attendees: Optional[List[str]] = Field(default=None, description="Booking attendees (user IDs)")
    lead_id: Optional[str] = Field(default=None, description="Related lead ID")
    contact_id: Optional[str] = Field(default=None, description="Related contact ID")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields")


class Booking(BookingCreate):
    """Booking model."""
    
    id: str = Field(..., description="Booking ID")
    created_at: Optional[datetime] = Field(default=None, description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Last update date")


class BookingListParams(PaginationParams, DateRangeParams):
    """Parameters for listing bookings."""
    
    location_id: Optional[str] = Field(default=None, description="Filter by location ID")
    lead_id: Optional[str] = Field(default=None, description="Filter by lead ID")
    contact_id: Optional[str] = Field(default=None, description="Filter by contact ID")
    attendee_id: Optional[str] = Field(default=None, description="Filter by attendee ID")
    query: Optional[str] = Field(default=None, description="Search query")


# Response models
class FunnelResponse(BaseResponse, Funnel):
    """Response model for a single funnel."""
    pass


class FunnelListResponse(BaseResponse):
    """Response model for a list of funnels."""
    
    items: List[Funnel] = Field(..., description="List of funnels")
    total: Optional[int] = Field(default=None, description="Total number of funnels")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class LeadResponse(BaseResponse, Lead):
    """Response model for a single lead."""
    pass


class LeadListResponse(BaseResponse):
    """Response model for a list of leads."""
    
    items: List[Lead] = Field(..., description="List of leads")
    total: Optional[int] = Field(default=None, description="Total number of leads")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class LeadNoteResponse(BaseResponse, LeadNote):
    """Response model for a single lead note."""
    pass


class LeadNoteListResponse(BaseResponse):
    """Response model for a list of lead notes."""
    
    items: List[LeadNote] = Field(..., description="List of notes")
    total: Optional[int] = Field(default=None, description="Total number of notes")


class LeadTaskResponse(BaseResponse, LeadTask):
    """Response model for a single lead task."""
    pass


class LeadTaskListResponse(BaseResponse):
    """Response model for a list of lead tasks."""
    
    items: List[LeadTask] = Field(..., description="List of tasks")
    total: Optional[int] = Field(default=None, description="Total number of tasks")


class EventResponse(BaseResponse, Event):
    """Response model for a single event."""
    pass


class EventListResponse(BaseResponse):
    """Response model for a list of events."""
    
    items: List[Event] = Field(..., description="List of events")
    total: Optional[int] = Field(default=None, description="Total number of events")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class BookingLocationResponse(BaseResponse, BookingLocation):
    """Response model for a single booking location."""
    pass


class BookingLocationListResponse(BaseResponse):
    """Response model for a list of booking locations."""
    
    items: List[BookingLocation] = Field(..., description="List of booking locations")
    total: Optional[int] = Field(default=None, description="Total number of booking locations")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page")


class BookingSlotListResponse(BaseResponse):
    """Response model for a list of booking slots."""
    
    items: List[BookingSlot] = Field(..., description="List of booking slots")
    total: Optional[int] = Field(default=None, description="Total number of booking slots")


class BookingResponse(BaseResponse, Booking):
    """Response model for a single booking."""
    pass


class BookingListResponse(BaseResponse):
    """Response model for a list of bookings."""
    
    items: List[Booking] = Field(..., description="List of bookings")
    total: Optional[int] = Field(default=None, description="Total number of bookings")
    page: Optional[int] = Field(default=None, description="Current page")
    limit: Optional[int] = Field(default=None, description="Items per page") 