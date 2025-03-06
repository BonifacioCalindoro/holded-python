"""
Asynchronous resource for interacting with the Numbering Series API.
"""
from typing import Any, Dict, Union

from ..models.numbering_series import (
    NumberingSeriesCreate, NumberingSeriesUpdate,
    NumberingSeriesResponse, NumberingSeriesListResponse
)


class AsyncNumberingSeriesResource:
    """Resource for interacting with the Numbering Series API asynchronously."""

    def __init__(self, client):
        """Initialize the numbering series resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "/numberingSeries"

    async def list_by_type(self, doc_type: str) -> NumberingSeriesListResponse:
        """Get numbering series by document type asynchronously.

        Args:
            doc_type: The document type (invoice, order, etc.)

        Returns:
            A list of numbering series for the specified document type
        """
        return await self.client.get(f"{self.base_path}/{doc_type}")

    async def create(self, data: Union[Dict[str, Any], NumberingSeriesCreate]) -> NumberingSeriesResponse:
        """Create a new numbering series asynchronously.

        Args:
            data: Numbering series data

        Returns:
            The created numbering series
        """
        return await self.client.post(self.base_path, data=data)

    async def update(self, series_id: str, data: Union[Dict[str, Any], NumberingSeriesUpdate]) -> NumberingSeriesResponse:
        """Update a numbering series asynchronously.

        Args:
            series_id: The numbering series ID
            data: Updated numbering series data

        Returns:
            The updated numbering series
        """
        return await self.client.put(f"{self.base_path}/{series_id}", data=data)

    async def delete(self, series_id: str) -> Dict[str, Any]:
        """Delete a numbering series asynchronously.

        Args:
            series_id: The numbering series ID

        Returns:
            A confirmation message
        """
        return await self.client.delete(f"{self.base_path}/{series_id}") 