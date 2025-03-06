"""
Resource for interacting with the Contacts API.
"""
from typing import Any, Dict, Optional, Union

from ..models.contacts import (
    ContactCreate, ContactUpdate, ContactListParams,
    ContactResponse, ContactListResponse, ContactAttachmentResponse,
    ContactAttachmentListResponse
)


class ContactsResource:
    """Resource for interacting with the Contacts API."""

    def __init__(self, client):
        """Initialize the contacts resource.

        Args:
            client: The Holded client instance.
        """
        self.client = client
        self.base_path = "invoicing/contacts"

    def list(self, params: Optional[Union[Dict[str, Any], ContactListParams]] = None) -> ContactListResponse:
        """List all contacts.

        Args:
            params: Optional query parameters.
                - page: Page number.
                - limit: Number of results per page.
                - type: Filter by contact type.
                - query: Search query.

        Returns:
            A list of contacts.
        """
        return self.client.get(self.base_path, params=params)

    def create(self, data: Union[Dict[str, Any], ContactCreate]) -> ContactResponse:
        """Create a new contact.

        Args:
            data: Contact data.

        Returns:
            The created contact.
        """
        return self.client.post(self.base_path, data=data)

    def get(self, contact_id: str) -> ContactResponse:
        """Get a specific contact.

        Args:
            contact_id: The contact ID.

        Returns:
            The contact.
        """
        print(f"{self.base_path}/{contact_id}")
        return self.client.get(f"{self.base_path}/{contact_id}")

    def update(self, contact_id: str, data: Union[Dict[str, Any], ContactUpdate]) -> ContactResponse:
        """Update a contact.

        Args:
            contact_id: The contact ID.
            data: Updated contact data.

        Returns:
            The updated contact.
        """
        return self.client.put(f"{self.base_path}/{contact_id}", data=data)

    def delete(self, contact_id: str) -> Dict[str, Any]:
        """Delete a contact.

        Args:
            contact_id: The contact ID.

        Returns:
            A confirmation message.
        """
        return self.client.delete(f"{self.base_path}/{contact_id}")

    def get_attachments(self, contact_id: str) -> ContactAttachmentListResponse:
        """Get attachments for a contact.

        Args:
            contact_id: The contact ID.

        Returns:
            A list of attachments.
        """
        return self.client.get(f"{self.base_path}/{contact_id}/attachments")

    def get_attachment(self, contact_id: str, attachment_id: str) -> ContactAttachmentResponse:
        """Get a specific attachment for a contact.

        Args:
            contact_id: The contact ID.
            attachment_id: The attachment ID.

        Returns:
            The attachment.
        """
        return self.client.get(f"{self.base_path}/{contact_id}/attachments/{attachment_id}") 