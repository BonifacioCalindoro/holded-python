# Error Handling

This guide explains how to handle errors when using the Holded API Wrapper.

## Exception Hierarchy

The Holded API Wrapper provides a hierarchy of exception classes to help you handle different types of errors:

- `HoldedError`: Base exception class for all Holded API errors
  - `HoldedAPIError`: Base class for API-related errors
    - `HoldedAuthError`: Authentication errors (401)
    - `HoldedNotFoundError`: Resource not found errors (404)
    - `HoldedValidationError`: Validation errors (422)
    - `HoldedRateLimitError`: Rate limit exceeded errors (429)
    - `HoldedServerError`: Server errors (500+)
  - `HoldedConnectionError`: Connection errors
  - `HoldedTimeoutError`: Request timeout errors

## Basic Error Handling

Here's a basic example of how to handle errors:

```python
from holded.client import HoldedClient
from holded.exceptions import (
    HoldedAuthError, HoldedNotFoundError, HoldedValidationError,
    HoldedRateLimitError, HoldedServerError, HoldedError
)

client = HoldedClient(api_key="your_api_key")

try:
    contact = client.contacts.get("contact_id")
except HoldedAuthError:
    print("Authentication failed. Check your API key.")
except HoldedNotFoundError:
    print("Contact not found.")
except HoldedValidationError as e:
    print(f"Validation error: {e.message}")
except HoldedRateLimitError:
    print("Rate limit exceeded. Please try again later.")
except HoldedServerError:
    print("Holded server error. Please try again later.")
except HoldedError as e:
    print(f"An error occurred: {e.message}")
```

## Accessing Error Details

All exception classes provide access to the error details:

```python
try:
    contact = client.contacts.get("contact_id")
except HoldedError as e:
    print(f"Error message: {e.message}")
    print(f"Status code: {e.status_code}")
    print(f"Error data: {e.error_data}")
```

## Handling Rate Limits

The Holded API may have rate limits. You can implement retry logic to handle rate limit errors:

```python
import time
from holded.exceptions import HoldedRateLimitError

max_retries = 3
retry_delay = 1

for attempt in range(max_retries):
    try:
        contact = client.contacts.get("contact_id")
        break  # Success, exit the loop
    except HoldedRateLimitError:
        if attempt < max_retries - 1:
            # Wait longer for each retry
            wait_time = retry_delay * (attempt + 1)
            print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print("Rate limit exceeded. Maximum retries reached.")
            raise
```

## Asynchronous Error Handling

When using the asynchronous client, error handling works the same way:

```python
import asyncio
from holded.async_client import AsyncHoldedClient
from holded.exceptions import HoldedError

async def main():
    client = AsyncHoldedClient(api_key="your_api_key")
    
    try:
        contact = await client.contacts.get("contact_id")
    except HoldedError as e:
        print(f"An error occurred: {e.message}")
    finally:
        await client.close()

asyncio.run(main())
```

## Best Practices

1. **Always handle exceptions**: Wrap API calls in try-except blocks to handle errors gracefully.
2. **Be specific**: Catch specific exceptions first, then more general ones.
3. **Log errors**: Log error details for debugging.
4. **Implement retries**: Use retry logic for transient errors like rate limits or server errors.
5. **Close the client**: Always close the client in a finally block to release resources. 