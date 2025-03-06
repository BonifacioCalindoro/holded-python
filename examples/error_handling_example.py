#!/usr/bin/env python
"""
Example script demonstrating error handling with the Holded API wrapper.
"""
import os
import asyncio
import uuid

from holded.client import HoldedClient
from holded.async_client import AsyncHoldedClient
from holded.exceptions import (
    HoldedError, HoldedAuthError, HoldedNotFoundError, HoldedValidationError,
    HoldedRateLimitError, HoldedServerError, HoldedTimeoutError, HoldedConnectionError
)


def sync_example():
    """Example using the synchronous client with error handling."""
    # Get API key from environment variable
    api_key = os.environ.get("HOLDED_API_KEY", "invalid_api_key")  # Intentionally use invalid key if not set

    # Initialize the client
    client = HoldedClient(api_key=api_key)

    # Example 1: Authentication Error
    print("\n=== Example 1: Authentication Error ===")
    try:
        # Try to list contacts with an invalid API key
        client.contacts.list()
    except HoldedAuthError as e:
        print(f"Authentication Error: {e.message}")
        print(f"Status Code: {e.status_code}")
        print(f"Error Data: {e.error_data}")
    except HoldedError as e:
        print(f"Unexpected error: {e.message}")

    # Use a valid API key for the rest of the examples
    valid_api_key = os.environ.get("HOLDED_API_KEY")
    if not valid_api_key:
        print("\nPlease set the HOLDED_API_KEY environment variable for the remaining examples.")
        return
    
    client = HoldedClient(api_key=valid_api_key)

    # Example 2: Not Found Error
    print("\n=== Example 2: Not Found Error ===")
    try:
        # Try to get a non-existent contact
        non_existent_id = str(uuid.uuid4())  # Generate a random ID
        client.contacts.get(non_existent_id)
    except HoldedNotFoundError as e:
        print(f"Not Found Error: {e.message}")
        print(f"Status Code: {e.status_code}")
        print(f"Error Data: {e.error_data}")
    except HoldedError as e:
        print(f"Unexpected error: {e.message}")

    # Example 3: Validation Error
    print("\n=== Example 3: Validation Error ===")
    try:
        # Try to create a contact with invalid data
        client.contacts.create({})  # Empty data, missing required fields
    except HoldedValidationError as e:
        print(f"Validation Error: {e.message}")
        print(f"Status Code: {e.status_code}")
        print(f"Error Data: {e.error_data}")
    except HoldedError as e:
        print(f"Unexpected error: {e.message}")

    # Example 4: Connection Error Simulation
    print("\n=== Example 4: Connection Error Simulation ===")
    try:
        # Create a client with an invalid base URL to simulate a connection error
        bad_client = HoldedClient(
            api_key=valid_api_key,
            base_url="https://invalid-domain.example.com/",
            timeout=2,  # Short timeout
            max_retries=1  # Only one retry
        )
        bad_client.contacts.list()
    except HoldedConnectionError as e:
        print(f"Connection Error: {e.message}")
    except HoldedTimeoutError as e:
        print(f"Timeout Error: {e.message}")
    except HoldedError as e:
        print(f"Unexpected error: {e.message}")

    # Example 5: Using a try-except-finally pattern
    print("\n=== Example 5: Using a try-except-finally pattern ===")
    try:
        # Try some operations
        contacts = client.contacts.list(limit=1)
        print(f"Successfully retrieved {len(contacts.items)} contacts")
        
        # Intentionally cause an error
        client.contacts.get("non-existent-id")
    except HoldedNotFoundError as e:
        print(f"Not Found Error: {e.message}")
    except HoldedAuthError as e:
        print(f"Authentication Error: {e.message}")
    except HoldedValidationError as e:
        print(f"Validation Error: {e.message}")
    except HoldedRateLimitError as e:
        print(f"Rate Limit Error: {e.message}")
    except HoldedServerError as e:
        print(f"Server Error: {e.message}")
    except HoldedTimeoutError as e:
        print(f"Timeout Error: {e.message}")
    except HoldedConnectionError as e:
        print(f"Connection Error: {e.message}")
    except HoldedError as e:
        print(f"Generic Holded Error: {e.message}")
    except Exception as e:
        print(f"Unexpected Exception: {str(e)}")
    finally:
        # Always close the client
        client.close()
        print("Client closed in finally block")


async def async_example():
    """Example using the asynchronous client with error handling."""
    # Get API key from environment variable
    valid_api_key = os.environ.get("HOLDED_API_KEY")
    if not valid_api_key:
        print("\nPlease set the HOLDED_API_KEY environment variable for the async examples.")
        return

    # Initialize the client
    client = AsyncHoldedClient(api_key=valid_api_key)

    # Example 1: Not Found Error (Async)
    print("\n=== Example 1: Not Found Error (Async) ===")
    try:
        # Try to get a non-existent contact
        non_existent_id = str(uuid.uuid4())  # Generate a random ID
        await client.contacts.get(non_existent_id)
    except HoldedNotFoundError as e:
        print(f"Not Found Error: {e.message}")
        print(f"Status Code: {e.status_code}")
        print(f"Error Data: {e.error_data}")
    except HoldedError as e:
        print(f"Unexpected error: {e.message}")

    # Example 2: Using a try-except-finally pattern (Async)
    print("\n=== Example 2: Using a try-except-finally pattern (Async) ===")
    try:
        # Try some operations
        contacts = await client.contacts.list(limit=1)
        print(f"Successfully retrieved {len(contacts.items)} contacts")
        
        # Intentionally cause an error
        await client.contacts.get("non-existent-id")
    except HoldedNotFoundError as e:
        print(f"Not Found Error: {e.message}")
    except HoldedError as e:
        print(f"Generic Holded Error: {e.message}")
    finally:
        # Always close the client
        await client.close()
        print("Async client closed in finally block")


if __name__ == "__main__":
    print("Running synchronous error handling examples...")
    sync_example()
    
    print("\nRunning asynchronous error handling examples...")
    asyncio.run(async_example()) 