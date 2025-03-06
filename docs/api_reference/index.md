# API Reference

This section provides detailed documentation for all classes and methods in the Holded API Wrapper.

## Client Classes

- [HoldedClient](client.md): The synchronous client for the Holded API
- [AsyncHoldedClient](async_client.md): The asynchronous client for the Holded API

## Resource Classes

### Invoice API

- [ContactsResource](resources/contacts.md): Resource for interacting with the Contacts API
- [DocumentsResource](resources/documents.md): Resource for interacting with the Documents API
- [ProductsResource](resources/products.md): Resource for interacting with the Products API
- [WarehouseResource](resources/warehouse.md): Resource for interacting with the Warehouse API
- [TreasuryResource](resources/treasury.md): Resource for interacting with the Treasury API
- [SalesChannelsResource](resources/sales_channels.md): Resource for interacting with the Sales Channels API
- [NumberingSeriesResource](resources/numbering_series.md): Resource for interacting with the Numbering Series API
- [ExpenseAccountsResource](resources/expense_accounts.md): Resource for interacting with the Expense Accounts API
- [RemittancesResource](resources/remittances.md): Resource for interacting with the Remittances API

### CRM API

- [CRMResource](resources/crm.md): Resource for interacting with the CRM API

### Projects API

- [ProjectsResource](resources/projects.md): Resource for interacting with the Projects API

### Team API

- [EmployeesResource](resources/employees.md): Resource for interacting with the Employees API

### Accounting API

- [AccountingResource](resources/accounting.md): Resource for interacting with the Accounting API

## Models

### Base Models

- [BaseModel](models/base.md): Base model for all Holded API models
- [BaseResponse](models/base.md#baseresponse): Base model for API responses

### Invoice API Models

- [Contact Models](models/contacts.md): Models for the Contacts API
- [Document Models](models/documents.md): Models for the Documents API
- [Product Models](models/products.md): Models for the Products API
- [Warehouse Models](models/warehouse.md): Models for the Warehouse API
- [Treasury Models](models/treasury.md): Models for the Treasury API
- [Sales Channel Models](models/sales_channels.md): Models for the Sales Channels API
- [Numbering Series Models](models/numbering_series.md): Models for the Numbering Series API
- [Expense Account Models](models/expense_accounts.md): Models for the Expense Accounts API
- [Remittance Models](models/remittances.md): Models for the Remittances API

### CRM API Models

- [CRM Models](models/crm.md): Models for the CRM API

### Projects API Models

- [Project Models](models/projects.md): Models for the Projects API

### Team API Models

- [Employee Models](models/employees.md): Models for the Employees API

### Accounting API Models

- [Accounting Models](models/accounting.md): Models for the Accounting API

## Exceptions

- [HoldedError](exceptions.md#holdederror): Base exception for all Holded API errors
- [HoldedAPIError](exceptions.md#holdedapierror): Base class for API-related errors
- [HoldedAuthError](exceptions.md#holdedautherror): Authentication errors
- [HoldedNotFoundError](exceptions.md#holdednotfounderror): Resource not found errors
- [HoldedValidationError](exceptions.md#holdedvalidationerror): Validation errors
- [HoldedRateLimitError](exceptions.md#holdedratelimiterror): Rate limit exceeded errors
- [HoldedServerError](exceptions.md#holdedservererror): Server errors
- [HoldedConnectionError](exceptions.md#holdedconnectionerror): Connection errors
- [HoldedTimeoutError](exceptions.md#holdedtimeouterror): Request timeout errors 