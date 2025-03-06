"""
Asynchronous CRM resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import AsyncBaseResource


class AsyncCRMResource(AsyncBaseResource):
    """
    Resource for interacting with the CRM API asynchronously.
    """

    async def list_funnels(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all funnels asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of funnels.
        """
        result = await self.client.get("crm/funnels", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_funnel(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new funnel asynchronously.

        Args:
            data: Funnel data.

        Returns:
            The created funnel.
        """
        result = await self.client.post("crm/funnels", data=data)
        return cast(Dict[str, Any], result)

    async def get_funnel(self, funnel_id: str) -> Dict[str, Any]:
        """
        Get a specific funnel asynchronously.

        Args:
            funnel_id: The funnel ID.

        Returns:
            The funnel.
        """
        result = await self.client.get(f"crm/funnels/{funnel_id}")
        return cast(Dict[str, Any], result)

    async def update_funnel(self, funnel_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a funnel asynchronously.

        Args:
            funnel_id: The funnel ID.
            data: Updated funnel data.

        Returns:
            The updated funnel.
        """
        result = await self.client.put(f"crm/funnels/{funnel_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_funnel(self, funnel_id: str) -> Dict[str, Any]:
        """
        Delete a funnel asynchronously.

        Args:
            funnel_id: The funnel ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"crm/funnels/{funnel_id}")
        return cast(Dict[str, Any], result)

    async def list_leads(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all leads asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of leads.
        """
        result = await self.client.get("crm/leads", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_lead(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new lead asynchronously.

        Args:
            data: Lead data.

        Returns:
            The created lead.
        """
        result = await self.client.post("crm/leads", data=data)
        return cast(Dict[str, Any], result)

    async def get_lead(self, lead_id: str) -> Dict[str, Any]:
        """
        Get a specific lead asynchronously.

        Args:
            lead_id: The lead ID.

        Returns:
            The lead.
        """
        result = await self.client.get(f"crm/leads/{lead_id}")
        return cast(Dict[str, Any], result)

    async def update_lead(self, lead_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a lead asynchronously.

        Args:
            lead_id: The lead ID.
            data: Updated lead data.

        Returns:
            The updated lead.
        """
        result = await self.client.put(f"crm/leads/{lead_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_lead(self, lead_id: str) -> Dict[str, Any]:
        """
        Delete a lead asynchronously.

        Args:
            lead_id: The lead ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"crm/leads/{lead_id}")
        return cast(Dict[str, Any], result)

    async def add_lead_note(self, lead_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add a note to a lead asynchronously.

        Args:
            lead_id: The lead ID.
            data: Note data.

        Returns:
            The created note.
        """
        result = await self.client.post(f"crm/leads/{lead_id}/notes", data=data)
        return cast(Dict[str, Any], result)

    async def add_lead_task(self, lead_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add a task to a lead asynchronously.

        Args:
            lead_id: The lead ID.
            data: Task data.

        Returns:
            The created task.
        """
        result = await self.client.post(f"crm/leads/{lead_id}/tasks", data=data)
        return cast(Dict[str, Any], result)

    async def update_lead_stage(self, lead_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update the stage of a lead asynchronously.

        Args:
            lead_id: The lead ID.
            data: Stage data.

        Returns:
            The updated lead.
        """
        result = await self.client.post(f"crm/leads/{lead_id}/stage", data=data)
        return cast(Dict[str, Any], result)

    async def list_events(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all events asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of events.
        """
        result = await self.client.get("crm/events", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_event(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new event asynchronously.

        Args:
            data: Event data.

        Returns:
            The created event.
        """
        result = await self.client.post("crm/events", data=data)
        return cast(Dict[str, Any], result)

    async def get_event(self, event_id: str) -> Dict[str, Any]:
        """
        Get a specific event asynchronously.

        Args:
            event_id: The event ID.

        Returns:
            The event.
        """
        result = await self.client.get(f"crm/events/{event_id}")
        return cast(Dict[str, Any], result)

    async def update_event(self, event_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an event asynchronously.

        Args:
            event_id: The event ID.
            data: Updated event data.

        Returns:
            The updated event.
        """
        result = await self.client.put(f"crm/events/{event_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_event(self, event_id: str) -> Dict[str, Any]:
        """
        Delete an event asynchronously.

        Args:
            event_id: The event ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"crm/events/{event_id}")
        return cast(Dict[str, Any], result)

    async def list_booking_locations(self) -> List[Dict[str, Any]]:
        """
        List all booking locations asynchronously.

        Returns:
            A list of booking locations.
        """
        result = await self.client.get("crm/bookings/locations")
        return cast(List[Dict[str, Any]], result)

    async def create_booking_location(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new booking location asynchronously.

        Args:
            data: Booking location data.

        Returns:
            The created booking location.
        """
        result = await self.client.post("crm/bookings/locations", data=data)
        return cast(Dict[str, Any], result)

    async def list_bookings(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all bookings asynchronously.

        Args:
            params: Optional query parameters.

        Returns:
            A list of bookings.
        """
        result = await self.client.get("crm/bookings", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_booking(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new booking asynchronously.

        Args:
            data: Booking data.

        Returns:
            The created booking.
        """
        result = await self.client.post("crm/bookings", data=data)
        return cast(Dict[str, Any], result)

    async def get_booking(self, booking_id: str) -> Dict[str, Any]:
        """
        Get a specific booking asynchronously.

        Args:
            booking_id: The booking ID.

        Returns:
            The booking.
        """
        result = await self.client.get(f"crm/bookings/{booking_id}")
        return cast(Dict[str, Any], result)

    async def update_booking(self, booking_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a booking asynchronously.

        Args:
            booking_id: The booking ID.
            data: Updated booking data.

        Returns:
            The updated booking.
        """
        result = await self.client.put(f"crm/bookings/{booking_id}", data=data)
        return cast(Dict[str, Any], result)

    async def delete_booking(self, booking_id: str) -> Dict[str, Any]:
        """
        Delete a booking asynchronously.

        Args:
            booking_id: The booking ID.

        Returns:
            A confirmation message.
        """
        result = await self.client.delete(f"crm/bookings/{booking_id}")
        return cast(Dict[str, Any], result) 