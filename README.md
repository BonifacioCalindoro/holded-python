# Holded API Wrapper

A comprehensive Python wrapper for the Holded API, providing both synchronous and asynchronous clients.

**DISCLAIMER: This is an unofficial library for the Holded API. It is not affiliated with, officially maintained, or endorsed by Holded. The author(s) of this library are not responsible for any misuse or damage caused by using this code. Use at your own risk.**

## Features

- Complete coverage of all Holded API endpoints (Invoice, CRM, Projects, Team, and Accounting)
- Both synchronous and asynchronous clients
- Type hints for better IDE support
- Comprehensive error handling with specific exception classes
- Pagination support for list endpoints
- Pydantic data models for request and response validation
- Detailed documentation for all methods

## Installation

```bash
pip install holded-python
```

## Usage

### Synchronous API

```python
from holded.client import HoldedClient
from holded.models.contacts import ContactCreate

# Initialize the client
client = HoldedClient(api_key="your_api_key")

# List contacts
contacts = client.contacts.list(limit=10)

# Create a contact
contact_data = ContactCreate(
    name="John Doe",
    email="john.doe@example.com",
    phone="123456789"
)
new_contact = client.contacts.create(contact_data)

# Get a specific contact
contact = client.contacts.get("contact_id")

# Update a contact
client.contacts.update("contact_id", {"name": "Jane Doe"})

# Delete a contact
client.contacts.delete("contact_id")
```

### Asynchronous API

```python
import asyncio
from holded.async_client import AsyncHoldedClient
from holded.models.contacts import ContactCreate

async def main():
    # Initialize the client
    client = AsyncHoldedClient(api_key="your_api_key")

    # List contacts
    contacts = await client.contacts.list(limit=10)

    # Create a contact
    contact_data = ContactCreate(
        name="John Doe",
        email="john.doe@example.com",
        phone="123456789"
    )
    new_contact = await client.contacts.create(contact_data)

    # Get a specific contact
    contact = await client.contacts.get("contact_id")

    # Update a contact
    await client.contacts.update("contact_id", {"name": "Jane Doe"})

    # Delete a contact
    await client.contacts.delete("contact_id")

    # Close the client session
    await client.close()

# Run the async function
asyncio.run(main())
```

## API Categories Covered

### Invoice API
- **Contacts**: Manage clients and providers
- **Documents**: Handle invoices, orders, quotes, delivery notes, etc.
- **Products**: Manage product catalog, categories, and variants
- **Warehouses**: Control inventory locations and stock
- **Treasury**: Manage financial accounts and transactions
- **Taxes**: Configure tax rates and rules
- **Payments**: Process and track payments
- **Contact Groups**: Organize contacts into groups
- **Services**: Manage service offerings
- **Expense Accounts**: Track expense categories
- **Numbering Series**: Set up document numbering
- **Sales Channels**: Configure sales channels
- **Remittances**: Handle remittance documents

### CRM API
- **Funnels**: Set up and manage sales funnels
- **Leads**: Track and manage sales leads
- **Events**: Schedule and manage events
- **Bookings**: Handle booking locations and appointments

### Projects API
- **Projects**: Create and manage projects
- **Tasks**: Assign and track project tasks
- **Time Tracking**: Log time spent on projects

### Team API
- **Employees**: Manage employee records
- **Time Tracking**: Track employee time and attendance

### Accounting API
- **Daily Ledger**: Record and manage accounting entries
- **Chart of Accounts**: Manage accounting account structure

## Data Models

The library includes Pydantic models for all API requests and responses, providing:

- Type validation and enforcement
- Automatic serialization/deserialization
- Clear documentation through type hints and descriptions
- Consistent structure for all API interactions
- Proper handling of optional and required fields

Example of using models:

```python
from holded.models.contacts import ContactCreate, ContactListParams
from holded.client import HoldedClient

client = HoldedClient(api_key="your_api_key")

# Create a contact with validated data
contact_data = ContactCreate(
    name="John Doe",
    email="john.doe@example.com",
    phone="123456789"
)
new_contact = client.contacts.create(contact_data)

# List contacts with pagination parameters
params = ContactListParams(page=1, limit=25, type="client")
contacts = client.contacts.list(params)
```

## Error Handling

The library provides specific exception classes for different types of errors:

```python
from holded.client import HoldedClient
from holded.exceptions import HoldedAuthError, HoldedNotFoundError, HoldedValidationError, HoldedRateLimitError, HoldedServerError

client = HoldedClient(api_key="your_api_key")

try:
    contact = client.contacts.get("non_existent_id")
except HoldedAuthError:
    print("Authentication failed. Check your API key.")
except HoldedNotFoundError:
    print("Contact not found.")
except HoldedValidationError as e:
    print(f"Validation error: {e}")
except HoldedRateLimitError:
    print("Rate limit exceeded. Please try again later.")
except HoldedServerError:
    print("Holded server error. Please try again later.")
```

## Authentication

The Holded API uses API keys for authentication. To generate an API key:

1. Log in to your Holded account
2. Go to Menu > Settings > Developers
3. Click "+ New API Key"
4. Enter a name/description for the key
5. Click Save
6. Copy the generated alphanumeric code

Include this API key when initializing the client:

```python
client = HoldedClient(api_key="your_api_key")
```

## Rate Limiting

The Holded API may have rate limits. The wrapper handles rate limit errors by raising a `HoldedRateLimitError` exception. You can implement retry logic in your application to handle these errors.

## Documentation

For more detailed documentation, see the [docs](https://github.com/BonifacioCalindoro/holded-python/tree/main/docs) directory.

## Examples

For examples of how to use the library, see the [examples](https://github.com/BonifacioCalindoro/holded-python/tree/main/examples) directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT 