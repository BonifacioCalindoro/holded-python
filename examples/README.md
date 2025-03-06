# Holded API Wrapper Examples

This directory contains example scripts demonstrating how to use the Holded API wrapper for various tasks.

## Prerequisites

Before running these examples, make sure you have:

1. Installed the Holded API wrapper:
   ```bash
   pip install holded-python
   ```

2. Set your Holded API key as an environment variable:
   ```bash
   # Linux/macOS
   export HOLDED_API_KEY="your_api_key_here"
   
   # Windows (Command Prompt)
   set HOLDED_API_KEY=your_api_key_here
   
   # Windows (PowerShell)
   $env:HOLDED_API_KEY="your_api_key_here"
   ```

## Available Examples

### 1. Contacts Management (`contacts_example.py`)

Demonstrates how to:
- List contacts with pagination and filtering
- Create new contacts
- Get contact details
- Update contacts
- Get contact attachments
- Delete contacts

### 2. Invoices and Documents (`invoices_example.py`)

Demonstrates how to:
- Create invoices with line items
- Get invoice details
- List invoices with filtering
- Send invoices by email
- Get invoice PDFs
- Process payments
- Delete invoices

### 3. Products and Inventory (`products_inventory_example.py`)

Demonstrates how to:
- Create product categories
- Create products with variants
- List products with filtering
- Create warehouses
- Update product stock
- Create stock movements
- List product stock
- Update products
- Delete products, categories, and warehouses

### 4. CRM Functionality (`crm_example.py`)

Demonstrates how to:
- Create sales funnels
- Create and manage leads
- Add notes and tasks to leads
- Update lead stages
- Create events
- Create booking locations
- Get booking slots
- Create bookings

### 5. Error Handling (`error_handling_example.py`)

Demonstrates how to:
- Handle authentication errors
- Handle not found errors
- Handle validation errors
- Handle connection errors
- Use try-except-finally patterns for robust error handling

### 6. Using Models (`using_models.py`)

Demonstrates how to:
- Use Pydantic models for request validation
- Create custom models with additional validation
- Handle model serialization and deserialization
- Use model inheritance for related data structures

## Running the Examples

To run any example, simply execute the script:

```bash
python contacts_example.py
```

Each example includes both synchronous and asynchronous versions of the code, demonstrating how to use both the `HoldedClient` and `AsyncHoldedClient` classes.

## Notes

- These examples are for demonstration purposes only and may create, modify, or delete data in your Holded account.
- Most examples include cleanup code to delete any data created during the example, but you should review the code before running it.
- Some examples include commented-out code for operations that would send emails or perform other actions with external effects.

## Disclaimer

This is an unofficial library for the Holded API. It is not affiliated with, officially maintained, or endorsed by Holded. The author(s) of this library are not responsible for any misuse or damage caused by using this code. Use at your own risk. 