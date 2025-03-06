"""
Asynchronous resource for interacting with the Remittances API.
"""
from typing import Any, Dict, Optional, Union

from ..models.remittances import (
    RemittanceListParams, RemittanceResponse, RemittanceListResponse
)


class AsyncRemittancesResource:
    """Resource for interacting with the Remittances API asynchronously."""

    def __init__(self, client):
        """Initialize the remittances resource.

        Args:
            client: The Holded async client instance.
        """
        self.client = client
        self.base_path = "/remittances"

    async def list(self, params: Optional[Union[Dict[str, Any], RemittanceListParams]] = None) -> RemittanceListResponse:
        """List all remittances asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit, from, to)

        Returns:
            A list of remittances
        """
        return await self.client.get(self.base_path, params=params)

    async def get(self, remittance_id: str) -> RemittanceResponse:
        """Get a specific remittance asynchronously.

        Args:
            remittance_id: The remittance ID

        Returns:
            The remittance
        """
        return await self.client.get(f"{self.base_path}/{remittance_id}") 