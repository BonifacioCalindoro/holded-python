"""
Asynchronous documents resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import AsyncBaseResource


class AsyncDocumentsResource(AsyncBaseResource):
    """
    Resource for interacting with the Documents API asynchronously.
    """

    async def list(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all documents asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit, type)

        Returns:
            A list of documents
        """
        result = await self.client.get("invoicing", "documents", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new document asynchronously.

        Args:
            data: Document data

        Returns:
            The created document
        """
        result = await self.client.post("invoicing", "documents", data)
        return cast(Dict[str, Any], result)

    async def get(self, document_id: str) -> Dict[str, Any]:
        """
        Get a specific document asynchronously.

        Args:
            document_id: The document ID

        Returns:
            The document details
        """
        result = await self.client.get("invoicing", "documents", document_id)
        return cast(Dict[str, Any], result)

    async def update(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a document asynchronously.

        Args:
            document_id: The document ID
            data: Updated document data

        Returns:
            The updated document
        """
        result = await self.client.put("invoicing", "documents", document_id, data)
        return cast(Dict[str, Any], result)

    async def delete(self, document_id: str) -> Dict[str, Any]:
        """
        Delete a document asynchronously.

        Args:
            document_id: The document ID

        Returns:
            The deletion response
        """
        result = await self.client.delete("invoicing", "documents", document_id)
        return cast(Dict[str, Any], result)

    async def pay(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Pay a document asynchronously.

        Args:
            document_id: The document ID
            data: Payment data

        Returns:
            The payment response
        """
        result = await self.client.post("invoicing", f"documents/{document_id}/pay", data)
        return cast(Dict[str, Any], result)

    async def send(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send a document asynchronously.

        Args:
            document_id: The document ID
            data: Send data (e.g., email, subject, body)

        Returns:
            The send response
        """
        result = await self.client.post("invoicing", f"documents/{document_id}/send", data)
        return cast(Dict[str, Any], result)

    async def get_pdf(self, document_id: str) -> Dict[str, Any]:
        """
        Get the PDF of a document asynchronously.

        Args:
            document_id: The document ID

        Returns:
            The PDF data
        """
        result = await self.client.get("invoicing", f"documents/{document_id}/pdf")
        return cast(Dict[str, Any], result)

    async def ship_all_items(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ship all items in a document asynchronously.

        Args:
            document_id: The document ID
            data: Shipping data

        Returns:
            The shipping response
        """
        result = await self.client.post("invoicing", f"documents/{document_id}/shipall", data)
        return cast(Dict[str, Any], result)

    async def ship_items_by_line(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ship items by line in a document asynchronously.

        Args:
            document_id: The document ID
            data: Shipping data with line items

        Returns:
            The shipping response
        """
        result = await self.client.post("invoicing", f"documents/{document_id}/shipline", data)
        return cast(Dict[str, Any], result)

    async def get_shipped_units(self, document_id: str, item_id: str) -> Dict[str, Any]:
        """
        Get shipped units for a specific item in a document asynchronously.

        Args:
            document_id: The document ID
            item_id: The item ID

        Returns:
            The shipped units data
        """
        result = await self.client.get("invoicing", f"documents/{document_id}/shipped/{item_id}")
        return cast(Dict[str, Any], result)

    async def attach_file(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Attach a file to a document asynchronously.

        Args:
            document_id: The document ID
            data: Attachment data

        Returns:
            The attachment response
        """
        result = await self.client.post("invoicing", f"documents/{document_id}/attach", data)
        return cast(Dict[str, Any], result)

    async def update_tracking(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update tracking information for a document asynchronously.

        Args:
            document_id: The document ID
            data: Tracking data

        Returns:
            The tracking update response
        """
        result = await self.client.post("invoicing", f"documents/{document_id}/tracking", data)
        return cast(Dict[str, Any], result)

    async def update_pipeline(self, document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update pipeline information for a document asynchronously.

        Args:
            document_id: The document ID
            data: Pipeline data

        Returns:
            The pipeline update response
        """
        result = await self.client.post("invoicing", f"documents/{document_id}/pipeline", data)
        return cast(Dict[str, Any], result)

    async def list_payment_methods(self) -> List[Dict[str, Any]]:
        """
        List all payment methods asynchronously.

        Returns:
            A list of payment methods
        """
        result = await self.client.get("invoicing", "paymentmethods")
        return cast(List[Dict[str, Any]], result) 