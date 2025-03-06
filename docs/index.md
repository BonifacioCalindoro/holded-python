# Holded API Wrapper Documentation

Welcome to the documentation for the Holded API Wrapper, a comprehensive Python library for interacting with the Holded API.

## Overview

The Holded API Wrapper provides a simple and intuitive interface to the Holded API, allowing you to manage your Holded account programmatically. It supports both synchronous and asynchronous operations, making it suitable for a wide range of applications.

## Features

- Complete coverage of all Holded API endpoints
- Type hints for better IDE support
- Comprehensive error handling with specific exception classes
- Pagination support for list endpoints
- Both synchronous and asynchronous clients
- Pydantic data models for request and response validation
- Detailed documentation for all methods

## Installation

```bash
pip install holded-python
```

## Quick Start

```python
from holded.client import HoldedClient
from holded.models.contacts import ContactCreate

# Initialize the client
client = HoldedClient(api_key="your_api_key")

# Create a contact
contact_data = ContactCreate(
    name="John Doe",
    email="john.doe@example.com",
    phone="123456789"
)
new_contact = client.contacts.create(contact_data)
print(f"Created contact: {new_contact.name} with ID: {new_contact.id}")
```

## Documentation Sections

- [Getting Started](getting_started.md): Installation and basic usage
- [API Reference](api_reference/index.md): Detailed documentation for all classes and methods
- [Examples](examples.md): Code examples for common tasks
- [Error Handling](error_handling.md): How to handle errors and exceptions
- [Advanced Usage](advanced_usage.md): Advanced topics and techniques

## Disclaimer

This is an unofficial library for the Holded API. It is not affiliated with, officially maintained, or endorsed by Holded. The author(s) of this library are not responsible for any misuse or damage caused by using this code. Use at your own risk. 