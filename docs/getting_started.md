# Getting Started

This guide will help you get started with the Holded API Wrapper.

## Installation

You can install the Holded API Wrapper using pip:

```bash
pip install holded-python
```

## Authentication

To use the Holded API, you need an API key. You can obtain an API key from your Holded account:

1. Log in to your Holded account
2. Go to Menu > Settings > Developers
3. Click "+ New API Key"
4. Enter a name/description for the key
5. Click Save
6. Copy the generated alphanumeric code

## Basic Usage

### Initializing the Client

```python
from holded.client import HoldedClient

# Initialize the client
client = HoldedClient(api_key="your_api_key")
```

### Making API Calls

The client provides access to various resources, each corresponding to a section of the Holded API:

```python
# List contacts
contacts = client.contacts.list(limit=10)
print(f"Found {len(contacts.items)} contacts")

# Get a specific contact
contact = client.contacts.get("contact_id")
print(f"Contact name: {contact.name}")
```

### Using Models

The library provides Pydantic models for all API requests and responses, ensuring type safety and validation:

```python
from holded.models.contacts import ContactCreate

# Create a contact using a model
contact_data = ContactCreate(
    name="John Doe",
    email="john.doe@example.com",
    phone="123456789",
    type="client"
)
new_contact = client.contacts.create(contact_data)
```

### Error Handling

The library provides specific exception classes for different types of errors:

```python
from holded.exceptions import HoldedAuthError, HoldedNotFoundError, HoldedValidationError

try:
    contact = client.contacts.get("non_existent_id")
except HoldedAuthError:
    print("Authentication failed. Check your API key.")
except HoldedNotFoundError:
    print("Contact not found.")
except HoldedValidationError as e:
    print(f"Validation error: {e}")
```

### Closing the Client

When you're done using the client, it's good practice to close it:

```python
client.close()
```

## Asynchronous Usage

The library also provides an asynchronous client for use with asyncio:

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

## Next Steps

- Check out the [Examples](examples.md) for more detailed usage examples
- Refer to the [API Reference](api_reference/index.md) for detailed documentation of all classes and methods
- Learn about [Error Handling](error_handling.md) for more information on handling errors and exceptions
- Explore [Advanced Usage](advanced_usage.md) for more advanced features and patterns 