#!/usr/bin/env python
"""
Example script demonstrating how to use the Holded API wrapper for invoices and documents.
"""
import os
import asyncio
from datetime import datetime
from pprint import pprint

from holded.client import HoldedClient
from holded.async_client import AsyncHoldedClient
from holded.models.documents import (
    DocumentCreate, DocumentItem, DocumentListParams
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
        # First, create a contact to associate with the invoice
        print("\n=== Creating a contact for the invoice ===")
        contact_data = ContactCreate(
            name="Invoice Example Client",
            email="invoice.example@example.com",
            type="client"
        )
        contact = client.contacts.create(contact_data)
        print(f"Created contact: {contact.name} with ID: {contact.id}")

        # List document types
        print("\n=== Listing payment methods ===")
        payment_methods = client.documents.list_payment_methods()
        print("Available payment methods:")
        for method in payment_methods:
            print(f"- {method.get('name')}")

        # Create an invoice
        print("\n=== Creating an invoice ===")
        invoice_data = DocumentCreate(
            contact_id=contact.id,
            date=datetime.now(),
            number="INV-EXAMPLE-001",
            notes="Example invoice created via API",
            items=[
                DocumentItem(
                    name="Product 1",
                    units=2,
                    price=100.00,
                    tax=21.0,
                    description="Example product"
                ),
                DocumentItem(
                    name="Service 1",
                    units=1,
                    price=50.00,
                    tax=21.0,
                    description="Example service"
                )
            ]
        )
        invoice = client.documents.create(invoice_data)
        print(f"Created invoice with ID: {invoice.get('id')}")

        # Get the invoice details
        print("\n=== Getting invoice details ===")
        invoice_details = client.documents.get(invoice.get('id'))
        print(f"Invoice details:")
        pprint(invoice_details)

        # List invoices with filtering
        print("\n=== Listing invoices ===")
        params = DocumentListParams(
            page=1,
            limit=5,
            type="invoice",
            contact_id=contact.id
        )
        invoices = client.documents.list(params)
        print(f"Found {len(invoices.items)} invoices for the contact:")
        for doc in invoices.items:
            print(f"- {doc.number} (ID: {doc.id}, Total: {doc.total})")

        # Send the invoice by email (commented out to avoid actual email sending)
        """
        print("\n=== Sending invoice by email ===")
        email_params = DocumentSendParams(
            email=contact.email,
            subject="Your Invoice",
            message="Please find your invoice attached."
        )
        send_result = client.documents.send(invoice.get('id'), email_params)
        print(f"Invoice sent: {send_result.get('message')}")
        """

        # Get invoice PDF URL
        print("\n=== Getting invoice PDF ===")
        pdf_result = client.documents.get_pdf(invoice.get('id'))
        print(f"Invoice PDF URL: {pdf_result.get('url')}")

        # Pay the invoice
        print("\n=== Paying the invoice ===")
        payment_data = {
            "date": datetime.now().isoformat(),
            "amount": invoice_details.get('total'),
            "method": payment_methods[0].get('id') if payment_methods else None
        }
        pay_result = client.documents.pay(invoice.get('id'), payment_data)
        print(f"Invoice payment result: {pay_result}")

        # Clean up - delete the invoice and contact
        print("\n=== Cleaning up ===")
        client.documents.delete(invoice.get('id'))
        print(f"Deleted invoice")
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
        # First, create a contact to associate with the invoice
        print("\n=== Creating a contact for the invoice (async) ===")
        contact_data = ContactCreate(
            name="Async Invoice Example Client",
            email="async.invoice.example@example.com",
            type="client"
        )
        contact = await client.contacts.create(contact_data)
        print(f"Created contact: {contact.name} with ID: {contact.id}")

        # List document types
        print("\n=== Listing payment methods (async) ===")
        payment_methods = await client.documents.list_payment_methods()
        print("Available payment methods:")
        for method in payment_methods:
            print(f"- {method.get('name')}")

        # Create an invoice
        print("\n=== Creating an invoice (async) ===")
        invoice_data = DocumentCreate(
            contact_id=contact.id,
            date=datetime.now(),
            number="ASYNC-INV-001",
            notes="Example async invoice created via API",
            items=[
                DocumentItem(
                    name="Async Product",
                    units=1,
                    price=75.00,
                    tax=21.0,
                    description="Example async product"
                )
            ]
        )
        invoice = await client.documents.create(invoice_data)
        print(f"Created invoice with ID: {invoice.get('id')}")

        # Get the invoice details
        print("\n=== Getting invoice details (async) ===")
        invoice_details = await client.documents.get(invoice.get('id'))
        print(f"Invoice details:")
        pprint(invoice_details)

        # Clean up - delete the invoice and contact
        print("\n=== Cleaning up (async) ===")
        await client.documents.delete(invoice.get('id'))
        print(f"Deleted invoice")
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