#!/usr/bin/env python
"""
Example script demonstrating how to use the Holded API wrapper for contacts management.
"""
import os
import asyncio
from pprint import pprint

from holded.client import HoldedClient
from holded.async_client import AsyncHoldedClient
from holded.models.contacts import ContactCreate, ContactUpdate, ContactListParams
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
        # List contacts with pagination and filtering
        print("\n=== Listing contacts ===")
        params = ContactListParams(page=1, limit=5, type="client")
        contacts = client.contacts.list(params)
        print(f"Found {len(contacts.items)} contacts:")
        for contact in contacts.items:
            print(f"- {contact.name} (ID: {contact.id})")

        # Create a new contact
        print("\n=== Creating a new contact ===")
        contact_data = ContactCreate(
            name="John Doe (Example)",
            email="john.doe.example@example.com",
            phone="123456789",
            type="client",
            notes="Created via API example script"
        )
        new_contact = client.contacts.create(contact_data)
        print(f"Created contact: {new_contact.name} with ID: {new_contact.id}")

        # Get the contact details
        print("\n=== Getting contact details ===")
        contact = client.contacts.get(new_contact.id)
        print(f"Contact details:")
        pprint(vars(contact))

        # Update the contact
        print("\n=== Updating contact ===")
        update_data = ContactUpdate(
            name="John Doe (Updated)",
            notes="Updated via API example script"
        )
        updated_contact = client.contacts.update(new_contact.id, update_data)
        print(f"Updated contact: {updated_contact.name}")

        # Get contact attachments
        print("\n=== Getting contact attachments ===")
        attachments = client.contacts.get_attachments(new_contact.id)
        print(f"Contact has {len(attachments.items)} attachments")

        # Clean up - delete the contact
        print("\n=== Deleting contact ===")
        client.contacts.delete(new_contact.id)
        print(f"Deleted contact: {new_contact.name}")

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
        # List contacts with pagination and filtering
        print("\n=== Listing contacts (async) ===")
        params = ContactListParams(page=1, limit=5, type="client")
        contacts = await client.contacts.list(params)
        print(f"Found {len(contacts.items)} contacts:")
        for contact in contacts.items:
            print(f"- {contact.name} (ID: {contact.id})")

        # Create a new contact
        print("\n=== Creating a new contact (async) ===")
        contact_data = ContactCreate(
            name="Jane Doe (Async Example)",
            email="jane.doe.example@example.com",
            phone="987654321",
            type="client",
            notes="Created via async API example script"
        )
        new_contact = await client.contacts.create(contact_data)
        print(f"Created contact: {new_contact.name} with ID: {new_contact.id}")

        # Get the contact details
        print("\n=== Getting contact details (async) ===")
        contact = await client.contacts.get(new_contact.id)
        print(f"Contact details:")
        pprint(vars(contact))

        # Update the contact
        print("\n=== Updating contact (async) ===")
        update_data = ContactUpdate(
            name="Jane Doe (Updated)",
            notes="Updated via async API example script"
        )
        updated_contact = await client.contacts.update(new_contact.id, update_data)
        print(f"Updated contact: {updated_contact.name}")

        # Clean up - delete the contact
        print("\n=== Deleting contact (async) ===")
        await client.contacts.delete(new_contact.id)
        print(f"Deleted contact: {new_contact.name}")

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