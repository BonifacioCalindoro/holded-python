"""
CRM resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import BaseResource


class CRMResource(BaseResource):
    """
    Resource for interacting with the CRM API.
    """

    def list_funnels(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all funnels.

        Args:
            params: Optional query parameters.

        Returns:
            A list of funnels.
        """
        return cast(List[Dict[str, Any]], self.client.get("crm/funnels", params=params))

    def create_funnel(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new funnel.

        Args:
            data: Funnel data.

        Returns:
            The created funnel.
        """
        return cast(Dict[str, Any], self.client.post("crm/funnels", data=data))

    def get_funnel(self, funnel_id: str) -> Dict[str, Any]:
        """
        Get a specific funnel.

        Args:
            funnel_id: The funnel ID.

        Returns:
            The funnel.
        """
        return cast(Dict[str, Any], self.client.get(f"crm/funnels/{funnel_id}"))

    def update_funnel(self, funnel_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a funnel.

        Args:
            funnel_id: The funnel ID.
            data: Updated funnel data.

        Returns:
            The updated funnel.
        """
        return cast(Dict[str, Any], self.client.put(f"crm/funnels/{funnel_id}", data=data))

    def delete_funnel(self, funnel_id: str) -> Dict[str, Any]:
        """
        Delete a funnel.

        Args:
            funnel_id: The funnel ID.

        Returns:
            A confirmation message.
        """
        return cast(Dict[str, Any], self.client.delete(f"crm/funnels/{funnel_id}"))

    def list_leads(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all leads.

        Args:
            params: Optional query parameters.

        Returns:
            A list of leads.
        """
        return cast(List[Dict[str, Any]], self.client.get("crm/leads", params=params))

    def create_lead(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new lead.

        Args:
            data: Lead data.

        Returns:
            The created lead.
        """
        return cast(Dict[str, Any], self.client.post("crm/leads", data=data))

    def get_lead(self, lead_id: str) -> Dict[str, Any]:
        """
        Get a specific lead.

        Args:
            lead_id: The lead ID.

        Returns:
            The lead.
        """
        return cast(Dict[str, Any], self.client.get(f"crm/leads/{lead_id}"))

    def update_lead(self, lead_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a lead.

        Args:
            lead_id: The lead ID.
            data: Updated lead data.

        Returns:
            The updated lead.
        """
        return cast(Dict[str, Any], self.client.put(f"crm/leads/{lead_id}", data=data))

    def delete_lead(self, lead_id: str) -> Dict[str, Any]:
        """
        Delete a lead.

        Args:
            lead_id: The lead ID.

        Returns:
            A confirmation message.
        """
        return cast(Dict[str, Any], self.client.delete(f"crm/leads/{lead_id}"))

    def add_lead_note(self, lead_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add a note to a lead.

        Args:
            lead_id: The lead ID.
            data: Note data.

        Returns:
            The created note.
        """
        return cast(Dict[str, Any], self.client.post(f"crm/leads/{lead_id}/notes", data=data))

    def add_lead_task(self, lead_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add a task to a lead.

        Args:
            lead_id: The lead ID.
            data: Task data.

        Returns:
            The created task.
        """
        return cast(Dict[str, Any], self.client.post(f"crm/leads/{lead_id}/tasks", data=data))

    def update_lead_stage(self, lead_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update the stage of a lead.

        Args:
            lead_id: The lead ID.
            data: Stage data.

        Returns:
            The updated lead.
        """
        return cast(Dict[str, Any], self.client.post(f"crm/leads/{lead_id}/stage", data=data))

    def list_events(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all events.

        Args:
            params: Optional query parameters.

        Returns:
            A list of events.
        """
        return cast(List[Dict[str, Any]], self.client.get("crm/events", params=params))

    def create_event(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new event.

        Args:
            data: Event data.

        Returns:
            The created event.
        """
        return cast(Dict[str, Any], self.client.post("crm/events", data=data))

    def get_event(self, event_id: str) -> Dict[str, Any]:
        """
        Get a specific event.

        Args:
            event_id: The event ID.

        Returns:
            The event.
        """
        return cast(Dict[str, Any], self.client.get(f"crm/events/{event_id}"))

    def update_event(self, event_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an event.

        Args:
            event_id: The event ID.
            data: Updated event data.

        Returns:
            The updated event.
        """
        return cast(Dict[str, Any], self.client.put(f"crm/events/{event_id}", data=data))

    def delete_event(self, event_id: str) -> Dict[str, Any]:
        """
        Delete an event.

        Args:
            event_id: The event ID.

        Returns:
            A confirmation message.
        """
        return cast(Dict[str, Any], self.client.delete(f"crm/events/{event_id}"))

    def list_booking_locations(self) -> List[Dict[str, Any]]:
        """
        List all booking locations.

        Returns:
            A list of booking locations.
        """
        return cast(List[Dict[str, Any]], self.client.get("crm/bookings/locations"))

    def create_booking_location(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new booking location.

        Args:
            data: Booking location data.

        Returns:
            The created booking location.
        """
        return cast(Dict[str, Any], self.client.post("crm/bookings/locations", data=data))

    def list_bookings(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all bookings.

        Args:
            params: Optional query parameters.

        Returns:
            A list of bookings.
        """
        return cast(List[Dict[str, Any]], self.client.get("crm/bookings", params=params))

    def create_booking(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new booking.

        Args:
            data: Booking data.

        Returns:
            The created booking.
        """
        return cast(Dict[str, Any], self.client.post("crm/bookings", data=data))

    def get_booking(self, booking_id: str) -> Dict[str, Any]:
        """
        Get a specific booking.

        Args:
            booking_id: The booking ID.

        Returns:
            The booking.
        """
        return cast(Dict[str, Any], self.client.get(f"crm/bookings/{booking_id}"))

    def update_booking(self, booking_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a booking.

        Args:
            booking_id: The booking ID.
            data: Updated booking data.

        Returns:
            The updated booking.
        """
        return cast(Dict[str, Any], self.client.put(f"crm/bookings/{booking_id}", data=data))

    def delete_booking(self, booking_id: str) -> Dict[str, Any]:
        """
        Delete a booking.

        Args:
            booking_id: The booking ID.

        Returns:
            A confirmation message.
        """
        return cast(Dict[str, Any], self.client.delete(f"crm/bookings/{booking_id}")) 