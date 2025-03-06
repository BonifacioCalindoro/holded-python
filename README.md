# Holded API Wrapper

A comprehensive Python wrapper for the Holded API, providing a clean, type-safe interface for interacting with Holded's services.

**DISCLAIMER: This is an unofficial library for the Holded API. It is not affiliated with, officially maintained, or endorsed by Holded. The author(s) of this library are not responsible for any misuse or damage caused by using this code. Use at your own risk.**

## Features

- **Complete API Coverage**: Supports all Holded API endpoints across Invoice, CRM, Projects, Team, and Accounting services
- **Type Safety**: Comprehensive Pydantic models for request and response validation
- **Synchronous and Asynchronous**: Choose between synchronous and asynchronous clients based on your needs
- **Pagination Handling**: Automatic pagination for list endpoints
- **Error Handling**: Robust error handling with detailed exception hierarchy
- **Rate Limiting**: Built-in rate limit handling with exponential backoff

## Installation

```bash
pip install holded-api
```

## Quick Start

```python
import os
from holded import HoldedClient

# Initialize the client with your API key
api_key = os.environ.get("HOLDED_API_KEY")
client = HoldedClient(api_key=api_key)

# List contacts
contacts = client.contacts.list(limit=10)
for contact in contacts.items:
    print(f"Contact: {contact.name} ({contact.id})")

# Create a new contact
new_contact = client.contacts.create(
    name="Acme Inc.",
    email="info@acme.com",
    type="client"
)
print(f"Created contact with ID: {new_contact.id}")

# Create an invoice
invoice = client.documents.create(
    contact_id=new_contact.id,
    type="invoice",
    date="2023-01-01",
    items=[
        {
            "name": "Product A",
            "units": 2,
            "price": 100
        }
    ]
)
print(f"Created invoice with ID: {invoice.id}")
```

## Asynchronous Usage

```python
import asyncio
import os
from holded import AsyncHoldedClient

async def main():
    api_key = os.environ.get("HOLDED_API_KEY")
    client = AsyncHoldedClient(api_key=api_key)
    
    # List contacts
    contacts = await client.contacts.list(limit=10)
    for contact in contacts.items:
        print(f"Contact: {contact.name} ({contact.id})")
    
    # Don't forget to close the client
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Enhanced Data Models

The wrapper includes comprehensive data models for all Holded API resources:

### Base Models

- `BaseModel`: Foundation for all models with Pydantic configuration
- `BaseResponse`: Common response structure
- `PaginationParams`: Parameters for paginated endpoints
- `DateRangeParams`: Parameters for date filtering
- `SortParams`: Parameters for sorting results
- `ErrorResponse`: Structure for API errors

### Resource-Specific Models

- **Contacts**: Contact management with address, bank account, and tax information
- **Documents**: Invoices, estimates, orders, and other document types
- **Products**: Product catalog with variants, categories, and stock management
- **CRM**: Leads, funnels, tasks, and notes
- **Treasury**: Accounts, transactions, and categories
- **Projects**: Project management, tasks, and time tracking
- **Accounting**: Journal entries, accounts, and financial reports
- **Team**: Employee management and permissions

## Documentation

For more detailed documentation, see:

- [Getting Started](docs/getting_started.md)
- [API Reference](docs/api_reference/index.md)
- [Examples](docs/examples.md)
- [Advanced Usage](docs/advanced_usage.md)
- [Error Handling](docs/error_handling.md)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 