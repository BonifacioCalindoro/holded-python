"""
Documents resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import BaseResource


class DocumentsResource(BaseResource):
    """
    Resource for interacting with the Documents API.
    """

    def list(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all documents.

        Args:
            params: Optional query parameters (e.g., page, limit, type)

        Returns:
            A list of documents
        """
        return cast(List[Dict[str, Any]], self.client.get("invoicing", "documents", params=params))

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new document.

        Args:
            data: Document data

        Returns:
            The created document
        """
        return cast(Dict[str, Any], self.client.post("invoicing", "documents", data))

    def get(self, document_id: str) -> Dict[str, Any]:
        """
        Get a specific document.

        Args:
            document_id: The document ID

        Returns:
            The document details
        """
        return cast(Dict[str, Any], self.client.get("invoicing", "documents", document_id))

    def update(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a document.

        Args:
            document_id: The document ID
            data: Updated document data

        Returns:
            The updated document
        """
        return cast(Dict[str, Any], self.client.put("invoicing", "documents", document_id, data))

    def delete(self, document_id: str) -> Dict[str, Any]:
        """
        Delete a document.

        Args:
            document_id: The document ID

        Returns:
            The deletion response
        """
        return cast(Dict[str, Any], self.client.delete("invoicing", "documents", document_id))

    def pay(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Pay a document.

        Args:
            document_id: The document ID
            data: Payment data

        Returns:
            The payment response
        """
        return cast(
            Dict[str, Any],
            self.client.post("invoicing", f"documents/{document_id}/pay", data)
        )

    def send(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send a document.

        Args:
            document_id: The document ID
            data: Send data (e.g., email, subject, body)

        Returns:
            The send response
        """
        return cast(
            Dict[str, Any],
            self.client.post("invoicing", f"documents/{document_id}/send", data)
        )

    def get_pdf(self, document_id: str) -> Dict[str, Any]:
        """
        Get the PDF of a document.

        Args:
            document_id: The document ID

        Returns:
            The PDF data
        """
        return cast(
            Dict[str, Any],
            self.client.get("invoicing", f"documents/{document_id}/pdf")
        )

    def ship_all_items(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ship all items in a document.

        Args:
            document_id: The document ID
            data: Shipping data

        Returns:
            The shipping response
        """
        return cast(
            Dict[str, Any],
            self.client.post("invoicing", f"documents/{document_id}/shipall", data)
        )

    def ship_items_by_line(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ship items by line in a document.

        Args:
            document_id: The document ID
            data: Shipping data with line items

        Returns:
            The shipping response
        """
        return cast(
            Dict[str, Any],
            self.client.post("invoicing", f"documents/{document_id}/shipline", data)
        )

    def get_shipped_units(self, document_id: str, item_id: str) -> Dict[str, Any]:
        """
        Get shipped units for a specific item in a document.

        Args:
            document_id: The document ID
            item_id: The item ID

        Returns:
            The shipped units data
        """
        return cast(
            Dict[str, Any],
            self.client.get("invoicing", f"documents/{document_id}/shipped/{item_id}")
        )

    def attach_file(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Attach a file to a document.

        Args:
            document_id: The document ID
            data: Attachment data

        Returns:
            The attachment response
        """
        return cast(
            Dict[str, Any],
            self.client.post("invoicing", f"documents/{document_id}/attach", data)
        )

    def update_tracking(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update tracking information for a document.

        Args:
            document_id: The document ID
            data: Tracking data

        Returns:
            The tracking update response
        """
        return cast(
            Dict[str, Any],
            self.client.post("invoicing", f"documents/{document_id}/tracking", data)
        )

    def update_pipeline(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update pipeline information for a document.

        Args:
            document_id: The document ID
            data: Pipeline data

        Returns:
            The pipeline update response
        """
        return cast(
            Dict[str, Any],
            self.client.post("invoicing", f"documents/{document_id}/pipeline", data)
        )

    def list_payment_methods(self) -> List[Dict[str, Any]]:
        """
        List all payment methods.

        Returns:
            A list of payment methods
        """
        return cast(
            List[Dict[str, Any]],
            self.client.get("invoicing", "paymentmethods")
        ) 