"""
Holded API Wrapper.

A comprehensive Python wrapper for the Holded API, providing both synchronous and asynchronous clients.
"""

__version__ = "0.1.0"
__author__ = "BonifacioCalindoro"
__license__ = "MIT"

# Import main client classes for easier access
from .client import HoldedClient
from .async_client import AsyncHoldedClient

# Import exceptions
from .exceptions import (
    HoldedError,
    HoldedAPIError,
    HoldedAuthError,
    HoldedNotFoundError,
    HoldedValidationError,
    HoldedRateLimitError,
    HoldedServerError,
    HoldedTimeoutError,
    HoldedConnectionError,
)

# Import resources for direct access if needed
from .resources.accounting import AccountingResource
from .resources.contacts import ContactsResource
from .resources.crm import CRMResource
from .resources.documents import DocumentsResource
from .resources.employees import EmployeesResource
from .resources.products import ProductsResource
from .resources.projects import ProjectsResource
from .resources.treasury import TreasuryResource
from .resources.warehouse import WarehouseResource

# Import async resources
from .resources.async_accounting import AsyncAccountingResource
from .resources.async_contacts import AsyncContactsResource
from .resources.async_crm import AsyncCRMResource
from .resources.async_documents import AsyncDocumentsResource
from .resources.async_employees import AsyncEmployeesResource
from .resources.async_products import AsyncProductsResource
from .resources.async_projects import AsyncProjectsResource
from .resources.async_treasury import AsyncTreasuryResource
from .resources.async_warehouse import AsyncWarehouseResource

__all__ = [
    "HoldedClient",
    "AsyncHoldedClient",
    "HoldedError",
    "HoldedAPIError",
    "HoldedAuthError",
    "HoldedNotFoundError",
    "HoldedValidationError",
    "HoldedRateLimitError",
    "HoldedServerError",
    "HoldedTimeoutError",
    "HoldedConnectionError",
]