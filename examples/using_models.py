"""
Example script demonstrating the use of Pydantic models with the Holded API wrapper.
"""
import asyncio
import os
from datetime import datetime

from holded.client import HoldedClient
from holded.async_client import AsyncHoldedClient
from holded.models.contacts import ContactCreate, ContactListParams, ContactResponse, ContactListResponse
from holded.models.documents import DocumentCreate, DocumentItem, DocumentListParams
from holded.models.products import ProductCreate, ProductVariant
from holded.exceptions import HoldedError


def synchronous_example():
    """Example using the synchronous client with Pydantic models."""
    # Get API key from environment variable
    api_key = os.environ.get("HOLDED_API_KEY")
    if not api_key:
        print("Please set the HOLDED_API_KEY environment variable.")
        return

    # Initialize the client
    client = HoldedClient(api_key=api_key)

    try:
        # List contacts with pagination parameters
        print("Listing contacts...")
        params = ContactListParams(page=1, limit=5, type="client")
        contacts_response: ContactListResponse = client.contacts.list(params)
        
        print(f"Found {len(contacts_response.items)} contacts:")
        for contact in contacts_response.items:
            print(f"- {contact.name} ({contact.id})")
        
        # Create a new contact
        print("\nCreating a new contact...")
        contact_data = ContactCreate(
            name="John Doe (Example)",
            email="john.doe.example@example.com",
            phone="123456789",
            type="client"
        )
        new_contact: ContactResponse = client.contacts.create(contact_data)
        print(f"Created contact: {new_contact.name} with ID: {new_contact.id}")
        
        # Create a product with variants
        print("\nCreating a new product...")
        product_data = ProductCreate(
            name="Example Product",
            description="This is an example product",
            price=99.99,
            tax=21.0,
            variants=[
                ProductVariant(
                    name="Small",
                    price=89.99
                ),
                ProductVariant(
                    name="Large",
                    price=109.99
                )
            ]
        )
        new_product = client.products.create(product_data)
        print(f"Created product: {new_product.get('name')} with ID: {new_product.get('id')}")
        
        # Create a document (invoice) for the new contact
        print("\nCreating a new invoice...")
        document_data = DocumentCreate(
            contact_id=new_contact.id,
            date=datetime.now(),
            items=[
                DocumentItem(
                    name="Example Product",
                    units=2,
                    price=99.99,
                    tax=21.0
                )
            ]
        )
        new_document = client.documents.create(document_data)
        print(f"Created document with ID: {new_document.get('id')}")
        
        # Clean up - delete the created contact
        print("\nCleaning up...")
        client.contacts.delete(new_contact.id)
        print(f"Deleted contact: {new_contact.name}")
        
    except HoldedError as e:
        print(f"Error: {e.message}")
        if e.error_data:
            print(f"Error data: {e.error_data}")
    finally:
        client.close()


async def asynchronous_example():
    """Example using the asynchronous client with Pydantic models."""
    # Get API key from environment variable
    api_key = os.environ.get("HOLDED_API_KEY")
    if not api_key:
        print("Please set the HOLDED_API_KEY environment variable.")
        return

    # Initialize the client
    client = AsyncHoldedClient(api_key=api_key)

    try:
        # List contacts with pagination parameters
        print("Listing contacts (async)...")
        params = ContactListParams(page=1, limit=5, type="client")
        contacts_response: ContactListResponse = await client.contacts.list(params)
        
        print(f"Found {len(contacts_response.items)} contacts:")
        for contact in contacts_response.items:
            print(f"- {contact.name} ({contact.id})")
        
        # Create a new contact
        print("\nCreating a new contact (async)...")
        contact_data = ContactCreate(
            name="Jane Doe (Async Example)",
            email="jane.doe.example@example.com",
            phone="987654321",
            type="client"
        )
        new_contact: ContactResponse = await client.contacts.create(contact_data)
        print(f"Created contact: {new_contact.name} with ID: {new_contact.id}")
        
        # Clean up - delete the created contact
        print("\nCleaning up...")
        await client.contacts.delete(new_contact.id)
        print(f"Deleted contact: {new_contact.name}")
        
    except HoldedError as e:
        print(f"Error: {e.message}")
        if e.error_data:
            print(f"Error data: {e.error_data}")
    finally:
        await client.close()


if __name__ == "__main__":
    print("Running synchronous example...")
    synchronous_example()
    
    print("\nRunning asynchronous example...")
    asyncio.run(asynchronous_example()) 