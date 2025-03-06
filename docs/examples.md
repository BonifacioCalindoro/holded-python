# Examples

This page provides examples of how to use the Holded API Wrapper for common tasks.

## Basic Examples

### Authentication

```python
from holded.client import HoldedClient

# Initialize the client with your API key
client = HoldedClient(api_key="your_api_key")
```

### Listing Contacts

```python
from holded.models.contacts import ContactListParams

# List all contacts
contacts = client.contacts.list()
print(f"Found {len(contacts.items)} contacts")

# List contacts with pagination and filtering
params = ContactListParams(
    page=1,
    limit=10,
    type="client"
)
contacts = client.contacts.list(params)
```

### Creating a Contact

```python
from holded.models.contacts import ContactCreate

# Create a contact
contact_data = ContactCreate(
    name="John Doe",
    email="john.doe@example.com",
    phone="123456789",
    type="client"
)
new_contact = client.contacts.create(contact_data)
print(f"Created contact: {new_contact.name} with ID: {new_contact.id}")
```

### Getting a Contact

```python
# Get a specific contact
contact = client.contacts.get("contact_id")
print(f"Contact name: {contact.name}")
print(f"Contact email: {contact.email}")
```

### Updating a Contact

```python
from holded.models.contacts import ContactUpdate

# Update a contact
update_data = ContactUpdate(
    name="John Smith",
    email="john.smith@example.com"
)
updated_contact = client.contacts.update("contact_id", update_data)
print(f"Updated contact: {updated_contact.name}")
```

### Deleting a Contact

```python
# Delete a contact
client.contacts.delete("contact_id")
print("Contact deleted")
```

## Document Examples

### Creating an Invoice

```python
from datetime import datetime
from holded.models.documents import DocumentCreate, DocumentItem

# Create an invoice
invoice_data = DocumentCreate(
    contact_id="contact_id",
    date=datetime.now(),
    number="INV-001",
    notes="Example invoice",
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
print(f"Created invoice with ID: {invoice.id}")
```

### Sending an Invoice

```python
from holded.models.documents import DocumentSendParams

# Send an invoice by email
email_params = DocumentSendParams(
    email="customer@example.com",
    subject="Your Invoice",
    message="Please find your invoice attached."
)
result = client.documents.send("invoice_id", email_params)
print(f"Invoice sent: {result.message}")
```

## Product Examples

### Creating a Product with Variants

```python
from holded.models.products import ProductCreate, ProductVariant

# Create a product with variants
product_data = ProductCreate(
    name="Example Product",
    description="This is an example product with variants",
    reference="PROD-001",
    price=99.99,
    tax=21.0,
    variants=[
        ProductVariant(
            name="Small",
            price=89.99,
            sku="PROD-001-S"
        ),
        ProductVariant(
            name="Medium",
            price=99.99,
            sku="PROD-001-M"
        ),
        ProductVariant(
            name="Large",
            price=109.99,
            sku="PROD-001-L"
        )
    ]
)
product = client.products.create(product_data)
print(f"Created product: {product.name} with ID: {product.id}")
```

## CRM Examples

### Creating a Sales Funnel

```python
from holded.models.crm import FunnelCreate

# Create a sales funnel
funnel_data = FunnelCreate(
    name="Sales Funnel",
    description="A funnel for sales leads",
    stages=["New", "Contacted", "Qualified", "Proposal", "Negotiation", "Won", "Lost"]
)
funnel = client.crm.create_funnel(funnel_data)
print(f"Created funnel: {funnel.name} with ID: {funnel.id}")
```

### Creating a Lead

```python
from holded.models.crm import LeadCreate

# Create a lead
lead_data = LeadCreate(
    name="Example Lead",
    contact_id="contact_id",
    funnel_id="funnel_id",
    stage="New",
    value=1000.0,
    description="This is an example lead"
)
lead = client.crm.create_lead(lead_data)
print(f"Created lead: {lead.name} with ID: {lead.id}")
```

## Asynchronous Examples

### Basic Async Usage

```python
import asyncio
from holded.async_client import AsyncHoldedClient
from holded.models.contacts import ContactCreate

async def main():
    # Initialize the client
    client = AsyncHoldedClient(api_key="your_api_key")
    
    try:
        # List contacts
        contacts = await client.contacts.list(limit=10)
        print(f"Found {len(contacts.items)} contacts")
        
        # Create a contact
        contact_data = ContactCreate(
            name="John Doe",
            email="john.doe@example.com",
            phone="123456789"
        )
        new_contact = await client.contacts.create(contact_data)
        print(f"Created contact: {new_contact.name}")
    finally:
        # Close the client
        await client.close()

# Run the async function
asyncio.run(main())
```

### Concurrent Operations

```python
import asyncio
from holded.async_client import AsyncHoldedClient

async def main():
    client = AsyncHoldedClient(api_key="your_api_key")
    
    try:
        # Perform multiple operations concurrently
        contacts_task = client.contacts.list(limit=5)
        products_task = client.products.list(limit=5)
        
        # Wait for both tasks to complete
        contacts, products = await asyncio.gather(contacts_task, products_task)
        
        print(f"Found {len(contacts.items)} contacts and {len(products.items)} products")
    finally:
        await client.close()

asyncio.run(main())
```

## More Examples

For more detailed examples, check out the example scripts in the `examples` directory of the repository:

- `contacts_example.py`: Examples for managing contacts
- `invoices_example.py`: Examples for managing invoices and documents
- `products_inventory_example.py`: Examples for managing products and inventory
- `crm_example.py`: Examples for using CRM functionality
- `error_handling_example.py`: Examples for handling errors 