#!/usr/bin/env python
"""
Example script demonstrating how to use the Holded API wrapper for CRM functionality.
"""
import os
import asyncio
from datetime import datetime, timedelta
from pprint import pprint

from holded.client import HoldedClient
from holded.async_client import AsyncHoldedClient
from holded.models.crm import (
    FunnelCreate, LeadCreate, LeadUpdate, LeadNoteCreate, LeadTaskCreate,
    EventCreate, BookingLocationCreate, BookingCreate
)
from holded.models.contacts import ContactCreate
from holded.exceptions import HoldedError


def sync_example():
    """Example using the synchronous client."""
    # Get API key from environment variable
    api_key = os.environ.get("HOLDED_API_KEY")
    if not api_key:
        print("Please set the HOLDED_API_KEY environment variable.")
        return

    # Initialize the client
    client = HoldedClient(api_key=api_key)

    try:
        # Create a contact for the CRM examples
        print("\n=== Creating a contact for CRM examples ===")
        contact_data = ContactCreate(
            name="CRM Example Contact",
            email="crm.example@example.com",
            phone="123456789",
            type="client"
        )
        contact = client.contacts.create(contact_data)
        print(f"Created contact: {contact.name} with ID: {contact.id}")

        # Create a sales funnel
        print("\n=== Creating a sales funnel ===")
        funnel_data = FunnelCreate(
            name="Example Sales Funnel",
            description="A funnel for example leads",
            stages=["New", "Contacted", "Qualified", "Proposal", "Negotiation", "Won", "Lost"]
        )
        funnel = client.crm.create_funnel(funnel_data)
        print(f"Created funnel: {funnel.get('name')} with ID: {funnel.get('id')}")

        # Create a lead
        print("\n=== Creating a lead ===")
        lead_data = LeadCreate(
            name="Example Lead",
            contact_id=contact.id,
            funnel_id=funnel.get('id'),
            stage="New",
            value=1000.0,
            description="This is an example lead",
            expected_close_date=datetime.now() + timedelta(days=30)
        )
        lead = client.crm.create_lead(lead_data)
        print(f"Created lead: {lead.get('name')} with ID: {lead.get('id')}")

        # Get the lead details
        print("\n=== Getting lead details ===")
        lead_details = client.crm.get_lead(lead.get('id'))
        print(f"Lead details:")
        pprint(lead_details)

        # Add a note to the lead
        print("\n=== Adding a note to the lead ===")
        note_data = LeadNoteCreate(
            content="This is an example note for the lead"
        )
        note = client.crm.create_lead_note(lead.get('id'), note_data)
        print(f"Added note to lead")

        # Add a task to the lead
        print("\n=== Adding a task to the lead ===")
        task_data = LeadTaskCreate(
            title="Follow up with lead",
            description="Call the lead to discuss their needs",
            due_date=datetime.now() + timedelta(days=2),
            priority="high"
        )
        task = client.crm.create_lead_task(lead.get('id'), task_data)
        print(f"Added task to lead with ID: {task.get('id')}")

        # Update the lead stage
        print("\n=== Updating lead stage ===")
        update_data = LeadUpdate(
            stage="Contacted"
        )
        updated_lead = client.crm.update_lead(lead.get('id'), update_data)
        print(f"Updated lead stage to: {updated_lead.get('stage')}")

        # Create an event
        print("\n=== Creating an event ===")
        event_data = EventCreate(
            title="Meeting with Example Lead",
            description="Initial meeting to discuss requirements",
            start_date=datetime.now() + timedelta(days=1),
            end_date=datetime.now() + timedelta(days=1, hours=1),
            location="Office",
            lead_id=lead.get('id')
        )
        event = client.crm.create_event(event_data)
        print(f"Created event: {event.get('title')} with ID: {event.get('id')}")

        # Create a booking location
        print("\n=== Creating a booking location ===")
        location_data = BookingLocationCreate(
            name="Example Meeting Room",
            description="A meeting room for client meetings",
            capacity=10,
            availability={
                "monday": ["09:00-12:00", "13:00-17:00"],
                "tuesday": ["09:00-12:00", "13:00-17:00"],
                "wednesday": ["09:00-12:00", "13:00-17:00"],
                "thursday": ["09:00-12:00", "13:00-17:00"],
                "friday": ["09:00-12:00", "13:00-17:00"]
            }
        )
        location = client.crm.create_booking_location(location_data)
        print(f"Created booking location: {location.get('name')} with ID: {location.get('id')}")

        # Get booking slots
        print("\n=== Getting booking slots ===")
        tomorrow = datetime.now() + timedelta(days=1)
        slots = client.crm.get_booking_location_slots(
            location.get('id'),
            date=tomorrow.strftime("%Y-%m-%d")
        )
        print(f"Available slots for {tomorrow.strftime('%Y-%m-%d')}:")
        for slot in slots.get('items', [])[:3]:  # Show first 3 slots
            print(f"- {slot.get('start_time')} to {slot.get('end_time')}")

        # Create a booking
        print("\n=== Creating a booking ===")
        booking_data = BookingCreate(
            location_id=location.get('id'),
            date=tomorrow,
            start_time="10:00",
            end_time="11:00",
            title="Meeting with Example Lead",
            description="Follow-up meeting",
            lead_id=lead.get('id')
        )
        booking = client.crm.create_booking(booking_data)
        print(f"Created booking with ID: {booking.get('id')}")

        # Clean up - delete everything we created
        print("\n=== Cleaning up ===")
        client.crm.delete_booking(booking.get('id'))
        print(f"Deleted booking")
        client.crm.delete_event(event.get('id'))
        print(f"Deleted event")
        client.crm.delete_lead(lead.get('id'))
        print(f"Deleted lead")
        client.crm.delete_funnel(funnel.get('id'))
        print(f"Deleted funnel")
        client.contacts.delete(contact.id)
        print(f"Deleted contact: {contact.name}")

    except HoldedError as e:
        print(f"Error: {e.message}")
        if hasattr(e, 'error_data') and e.error_data:
            print(f"Error data: {e.error_data}")
    finally:
        client.close()


async def async_example():
    """Example using the asynchronous client."""
    # Get API key from environment variable
    api_key = os.environ.get("HOLDED_API_KEY")
    if not api_key:
        print("Please set the HOLDED_API_KEY environment variable.")
        return

    # Initialize the client
    client = AsyncHoldedClient(api_key=api_key)

    try:
        # Create a contact for the CRM examples
        print("\n=== Creating a contact for CRM examples (async) ===")
        contact_data = ContactCreate(
            name="Async CRM Example Contact",
            email="async.crm.example@example.com",
            phone="987654321",
            type="client"
        )
        contact = await client.contacts.create(contact_data)
        print(f"Created contact: {contact.name} with ID: {contact.id}")

        # Create a sales funnel
        print("\n=== Creating a sales funnel (async) ===")
        funnel_data = FunnelCreate(
            name="Async Example Sales Funnel",
            description="An async funnel for example leads",
            stages=["New", "Contacted", "Qualified", "Proposal", "Won", "Lost"]
        )
        funnel = await client.crm.create_funnel(funnel_data)
        print(f"Created funnel: {funnel.get('name')} with ID: {funnel.get('id')}")

        # Create a lead
        print("\n=== Creating a lead (async) ===")
        lead_data = LeadCreate(
            name="Async Example Lead",
            contact_id=contact.id,
            funnel_id=funnel.get('id'),
            stage="New",
            value=2000.0,
            description="This is an async example lead"
        )
        lead = await client.crm.create_lead(lead_data)
        print(f"Created lead: {lead.get('name')} with ID: {lead.get('id')}")

        # Clean up - delete everything we created
        print("\n=== Cleaning up (async) ===")
        await client.crm.delete_lead(lead.get('id'))
        print(f"Deleted lead")
        await client.crm.delete_funnel(funnel.get('id'))
        print(f"Deleted funnel")
        await client.contacts.delete(contact.id)
        print(f"Deleted contact: {contact.name}")

    except HoldedError as e:
        print(f"Error: {e.message}")
        if hasattr(e, 'error_data') and e.error_data:
            print(f"Error data: {e.error_data}")
    finally:
        await client.close()


if __name__ == "__main__":
    print("Running synchronous example...")
    sync_example()
    
    print("\nRunning asynchronous example...")
    asyncio.run(async_example()) 