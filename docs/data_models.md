# Data Models

This document provides an overview of the data models used in the Holded API Wrapper. These models are built using Pydantic, which provides validation, serialization, and documentation benefits.

## Base Models

The foundation of our data model structure is in `holded/models/base.py`:

- **BaseModel**: The foundation for all models with Pydantic configuration
- **BaseResponse**: Common response structure with a `success` field
- **PaginationParams**: Parameters for paginated endpoints (`page`, `limit`)
- **DateRangeParams**: Parameters for date filtering (`start_date`, `end_date`)
- **SortParams**: Parameters for sorting results (`sort_field`, `sort_order`)
- **ErrorResponse**: Structure for API errors (`message`, `error`, `status`)

## Contact Models

Contact models in `holded/models/contacts.py` represent clients, suppliers, and other business relationships:

### Core Models
- **Contact**: Complete contact information including personal details, addresses, and custom fields
- **ContactCreate**: Model for creating new contacts
- **ContactUpdate**: Model for updating existing contacts

### Supporting Models
- **ContactAddress**: Address information with street, city, postal code, etc.
- **ContactBankAccount**: Banking details including account numbers and IBAN
- **ContactTax**: Tax-related information like tax ID and VAT number
- **ContactSocialMedia**: Social media profile links
- **ContactPaymentSettings**: Default payment methods and terms

### Enums
- **ContactType**: Types of contacts (CLIENT, SUPPLIER, LEAD, etc.)
- **ContactStatus**: Status values (ACTIVE, INACTIVE, BLOCKED)

## Document Models

Document models in `holded/models/documents.py` handle invoices, estimates, orders, and other business documents:

### Core Models
- **Document**: Complete document information including items, payments, and totals
- **DocumentCreate**: Model for creating new documents
- **DocumentUpdate**: Model for updating existing documents

### Supporting Models
- **DocumentItem**: Line items in documents with product details and pricing
- **DocumentPayment**: Payment information for documents
- **DocumentTax**: Tax information applied to documents
- **DocumentSendParams**: Parameters for sending documents via email
- **DocumentAttachment**: Files attached to documents

### Enums
- **DocumentType**: Types of documents (INVOICE, ESTIMATE, ORDER, etc.)
- **DocumentStatus**: Status values (DRAFT, SENT, PAID, etc.)
- **PaymentMethod**: Payment methods (CASH, BANK_TRANSFER, etc.)

## Product Models

Product models in `holded/models/products.py` manage the product catalog:

### Core Models
- **Product**: Complete product information including pricing, stock, and variants
- **ProductCreate**: Model for creating new products
- **ProductUpdate**: Model for updating existing products
- **ProductCategory**: Categories for organizing products
- **ProductVariant**: Variations of products (sizes, colors, etc.)

### Supporting Models
- **ProductImage**: Product images with URLs and metadata
- **ProductTax**: Tax information for products
- **ProductSupplier**: Supplier information for products
- **ProductWarehouse**: Warehouse stock information
- **ProductVariantAttribute**: Attributes for product variants

### Enums
- **ProductType**: Types of products (PRODUCT, SERVICE, SUBSCRIPTION, etc.)
- **ProductStatus**: Status values (ACTIVE, INACTIVE, DISCONTINUED)
- **StockManagement**: Stock management types (SIMPLE, VARIANTS, NONE)

## CRM Models

CRM models in `holded/models/crm.py` handle leads, opportunities, and sales processes:

### Core Models
- **Lead**: Sales lead information
- **LeadCreate**: Model for creating new leads
- **LeadUpdate**: Model for updating existing leads
- **Funnel**: Sales funnel configuration
- **LeadTask**: Tasks associated with leads
- **LeadNote**: Notes attached to leads

### Enums
- **LeadStage**: Stages in the sales process (NEW, QUALIFIED, WON, etc.)
- **TaskPriority**: Priority levels for tasks (LOW, MEDIUM, HIGH, URGENT)
- **TaskStatus**: Status values for tasks (PENDING, IN_PROGRESS, COMPLETED, etc.)

## Treasury Models

Treasury models in `holded/models/treasury.py` manage financial accounts and transactions:

### Core Models
- **Account**: Financial account information
- **AccountCreate**: Model for creating new accounts
- **AccountUpdate**: Model for updating existing accounts
- **Transaction**: Financial transaction details
- **Category**: Categories for organizing transactions

### Enums
- **AccountType**: Types of accounts (BANK, CASH, CREDIT_CARD, etc.)
- **TransactionType**: Types of transactions (INCOME, EXPENSE, TRANSFER)
- **TransactionStatus**: Status values (PENDING, RECONCILED)

## Benefits of Our Model Structure

1. **Type Safety**: All models have proper type annotations, providing IDE autocompletion and type checking
2. **Validation**: Pydantic validates data at runtime, catching errors early
3. **Documentation**: Each field has a description, making the API self-documenting
4. **Serialization**: Automatic conversion between Python objects and JSON
5. **Consistency**: Uniform structure across all API resources
6. **Enums**: Restricted values for fields that accept only specific options

## Using Models in API Calls

```python
from holded import HoldedClient
from holded.models.contacts import ContactCreate, ContactType

# Initialize client
client = HoldedClient(api_key="your_api_key")

# Create a contact using the model
new_contact = client.contacts.create(
    ContactCreate(
        name="Acme Inc.",
        email="info@acme.com",
        type=ContactType.CLIENT,
        phone="123-456-7890"
    )
)

# The response is also a model
print(f"Created contact: {new_contact.id}, {new_contact.name}")

# List contacts with filtering
contacts = client.contacts.list(
    type=ContactType.CLIENT,
    limit=10
)

# Response items are models
for contact in contacts.items:
    print(f"Contact: {contact.name} ({contact.type})")
```

## Custom Validation

Many models include custom validators to ensure data integrity:

```python
@field_validator('email')
def validate_email(cls, v):
    """Validate email format."""
    if v is not None and v.strip() != "":
        if '@' not in v:
            raise ValueError('Invalid email format')
    return v
```

## Model Relationships

Models can reference other models to create complex structures:

```python
class Document(BaseModel):
    """Document model."""
    
    id: str = Field(..., description="Document ID")
    # ... other fields ...
    items: List[DocumentItem] = Field(..., description="Document items")
    payments: Optional[List[DocumentPayment]] = Field(default=None, description="Document payments")
```

## Extending Models

The model structure is designed to be extensible. If you need additional fields or validation, you can create your own models that inherit from the base models:

```python
from holded.models.contacts import Contact

class EnhancedContact(Contact):
    """Enhanced contact model with additional fields."""
    
    loyalty_points: int = Field(default=0, description="Customer loyalty points")
    account_manager: Optional[str] = Field(default=None, description="Account manager name")
``` 