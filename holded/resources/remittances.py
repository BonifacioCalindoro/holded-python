"""
Resource for interacting with the Remittances API.
"""
from typing import Any, Dict, Optional, Union

from ..models.remittances import (
    RemittanceListParams, RemittanceResponse, RemittanceListResponse
)


class RemittancesResource:
    """Resource for interacting with the Remittances API."""

    def __init__(self, client):
        """Initialize the remittances resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "/remittances"

    def list(self, params: Optional[Union[Dict[str, Any], RemittanceListParams]] = None) -> RemittanceListResponse:
        """List all remittances.

        Args:
            params: Optional query parameters (e.g., page, limit, from, to)

        Returns:
            A list of remittances
        """
        return self.client.get(self.base_path, params=params)

    def get(self, remittance_id: str) -> RemittanceResponse:
        """Get a specific remittance.

        Args:
            remittance_id: The remittance ID

        Returns:
            The remittance
        """
        return self.client.get(f"{self.base_path}/{remittance_id}") 