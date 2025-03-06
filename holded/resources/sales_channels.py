"""
Resource for interacting with the Sales Channels API.
"""
from typing import Any, Dict, Optional, Union

from ..models.sales_channels import (
    SalesChannelCreate, SalesChannelUpdate, SalesChannelListParams,
    SalesChannelResponse, SalesChannelListResponse
)


class SalesChannelsResource:
    """Resource for interacting with the Sales Channels API."""

    def __init__(self, client):
        """Initialize the sales channels resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "/salesChannels"

    def list(self, params: Optional[Union[Dict[str, Any], SalesChannelListParams]] = None) -> SalesChannelListResponse:
        """List all sales channels.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of sales channels
        """
        return self.client.get(self.base_path, params=params)

    def create(self, data: Union[Dict[str, Any], SalesChannelCreate]) -> SalesChannelResponse:
        """Create a new sales channel.

        Args:
            data: Sales channel data

        Returns:
            The created sales channel
        """
        return self.client.post(self.base_path, data=data)

    def get(self, channel_id: str) -> SalesChannelResponse:
        """Get a specific sales channel.

        Args:
            channel_id: The sales channel ID

        Returns:
            The sales channel
        """
        return self.client.get(f"{self.base_path}/{channel_id}")

    def update(self, channel_id: str, data: Union[Dict[str, Any], SalesChannelUpdate]) -> SalesChannelResponse:
        """Update a sales channel.

        Args:
            channel_id: The sales channel ID
            data: Updated sales channel data

        Returns:
            The updated sales channel
        """
        return self.client.put(f"{self.base_path}/{channel_id}", data=data)

    def delete(self, channel_id: str) -> Dict[str, Any]:
        """Delete a sales channel.

        Args:
            channel_id: The sales channel ID

        Returns:
            A confirmation message
        """
        return self.client.delete(f"{self.base_path}/{channel_id}") 