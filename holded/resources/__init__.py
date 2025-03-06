"""
Resources for the Holded API.
"""
from abc import ABC


class BaseResource(ABC):
    """Base resource for the Holded API."""

    def __init__(self, client):
        """Initialize the resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client


class AsyncBaseResource(ABC):
    """Base resource for the Holded API (async)."""

    def __init__(self, client):
        """Initialize the resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client


__all__ = [
    "BaseResource",
    "AsyncBaseResource",
    "ContactsResource",
    "AsyncContactsResource",
    "DocumentsResource",
    "AsyncDocumentsResource",
    "ProductsResource",
    "AsyncProductsResource",
    "WarehouseResource",
    "AsyncWarehouseResource",
    "TreasuryResource",
    "AsyncTreasuryResource",
    "AccountingResource",
    "AsyncAccountingResource",
    "EmployeesResource",
    "AsyncEmployeesResource",
    "ProjectsResource",
    "AsyncProjectsResource",
    "CRMResource",
    "AsyncCRMResource",
    "SalesChannelsResource",
    "AsyncSalesChannelsResource",
    "NumberingSeriesResource",
    "AsyncNumberingSeriesResource",
    "ExpenseAccountsResource",
    "AsyncExpenseAccountsResource",
    "RemittancesResource",
    "AsyncRemittancesResource",
] 