# Advanced Usage

This guide covers advanced usage patterns for the Holded API Wrapper.

## Working with Pydantic Models

The Holded API Wrapper uses Pydantic models for request and response validation. This provides several benefits:

- Type safety and validation
- Automatic serialization/deserialization
- Clear documentation through type hints

### Custom Validation

You can extend the models with custom validation:

```python
from pydantic import field_validator
from holded.models.contacts import ContactCreate

class CustomContactCreate(ContactCreate):
    @field_validator('email')
    def validate_email_domain(cls, v):
        if v and not v.endswith('@company.com'):
            raise ValueError('Email must be a company email')
        return v

# Use the custom model
contact_data = CustomContactCreate(
    name="John Doe",
    email="john.doe@company.com",
    phone="123456789"
)
```

## Pagination

For endpoints that return lists of items, the Holded API Wrapper handles pagination automatically:

```python
from holded.models.contacts import ContactListParams

# Get the first page with 10 items per page
params = ContactListParams(page=1, limit=10)
first_page = client.contacts.list(params)

# Get the next page
params.page = 2
second_page = client.contacts.list(params)
```

### Iterating Through All Pages

You can iterate through all pages:

```python
def get_all_contacts(client):
    params = ContactListParams(page=1, limit=100)
    all_contacts = []
    
    while True:
        response = client.contacts.list(params)
        all_contacts.extend(response.items)
        
        # Check if there are more pages
        if len(response.items) < params.limit:
            break
            
        params.page += 1
        
    return all_contacts
```

## Asynchronous Batch Operations

You can perform multiple operations concurrently using the asynchronous client:

```python
import asyncio
from holded.async_client import AsyncHoldedClient

async def process_contacts(client, contact_ids):
    # Create tasks for all contact IDs
    tasks = [client.contacts.get(contact_id) for contact_id in contact_ids]
    
    # Execute all tasks concurrently
    contacts = await asyncio.gather(*tasks)
    
    return contacts

async def main():
    client = AsyncHoldedClient(api_key="your_api_key")
    
    try:
        contact_ids = ["id1", "id2", "id3", "id4", "id5"]
        contacts = await process_contacts(client, contact_ids)
        
        for contact in contacts:
            print(f"Contact: {contact.name}")
    finally:
        await client.close()

asyncio.run(main())
```

## Rate Limiting and Backoff

Implement a more sophisticated retry strategy with exponential backoff:

```python
import time
import random
from holded.exceptions import HoldedRateLimitError, HoldedServerError

def with_retry(func, max_retries=5, base_delay=1, max_delay=60):
    """Execute a function with retry logic and exponential backoff."""
    retries = 0
    
    while True:
        try:
            return func()
        except (HoldedRateLimitError, HoldedServerError) as e:
            retries += 1
            if retries > max_retries:
                raise
                
            # Calculate delay with exponential backoff and jitter
            delay = min(base_delay * (2 ** (retries - 1)), max_delay)
            jitter = random.uniform(0, 0.1 * delay)
            wait_time = delay + jitter
            
            print(f"Retrying in {wait_time:.2f} seconds...")
            time.sleep(wait_time)
```

## Extending the Client

You can extend the client with custom methods:

```python
from holded.client import HoldedClient

class CustomHoldedClient(HoldedClient):
    def get_contact_with_documents(self, contact_id):
        """Get a contact and all their documents."""
        contact = self.contacts.get(contact_id)
        documents = self.documents.list(contact_id=contact_id)
        
        return {
            "contact": contact,
            "documents": documents
        }
```

## Using Environment Variables

For better security, use environment variables for sensitive information:

```python
import os
from holded.client import HoldedClient

# Load API key from environment variable
api_key = os.environ.get("HOLDED_API_KEY")
if not api_key:
    raise ValueError("HOLDED_API_KEY environment variable not set")

client = HoldedClient(api_key=api_key)
```

## Logging

Enable logging to debug API interactions:

```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("holded")

# Now API calls will log detailed information
client = HoldedClient(api_key="your_api_key")
contacts = client.contacts.list()
``` 