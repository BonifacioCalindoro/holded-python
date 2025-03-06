"""
Asynchronous contacts resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import AsyncBaseResource


class AsyncContactsResource(AsyncBaseResource):
    """
    Resource for interacting with the Contacts API asynchronously.
    """

    async def list(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all contacts asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of contacts
        """
        result = await self.client.get("invoicing", "contacts", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new contact asynchronously.

        Args:
            data: Contact data

        Returns:
            The created contact
        """
        result = await self.client.post("invoicing", "contacts", data)
        return cast(Dict[str, Any], result)

    async def get(self, contact_id: str) -> Dict[str, Any]:
        """
        Get a specific contact asynchronously.

        Args:
            contact_id: The contact ID

        Returns:
            The contact details
        """
        result = await self.client.get("invoicing", "contacts", contact_id)
        return cast(Dict[str, Any], result)

    async def update(self, contact_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a contact asynchronously.

        Args:
            contact_id: The contact ID
            data: Updated contact data

        Returns:
            The updated contact
        """
        result = await self.client.put("invoicing", "contacts", contact_id, data)
        return cast(Dict[str, Any], result)

    async def delete(self, contact_id: str) -> Dict[str, Any]:
        """
        Delete a contact asynchronously.

        Args:
            contact_id: The contact ID

        Returns:
            The deletion response
        """
        result = await self.client.delete("invoicing", "contacts", contact_id)
        return cast(Dict[str, Any], result)

    async def get_attachments(self, contact_id: str) -> List[Dict[str, Any]]:
        """
        Get a list of contact attachments asynchronously.

        Args:
            contact_id: The contact ID

        Returns:
            A list of attachments
        """
        result = await self.client.get("invoicing", f"contacts/{contact_id}/attachments")
        return cast(List[Dict[str, Any]], result)

    async def get_attachment(self, contact_id: str, attachment_id: str) -> Dict[str, Any]:
        """
        Get a specific contact attachment asynchronously.

        Args:
            contact_id: The contact ID
            attachment_id: The attachment ID

        Returns:
            The attachment details
        """
        result = await self.client.get("invoicing", f"contacts/{contact_id}/attachments/{attachment_id}")
        return cast(Dict[str, Any], result) 