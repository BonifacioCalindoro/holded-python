"""
Unit tests for the Holded async client.
"""
import unittest
from unittest.mock import patch, MagicMock

import aiohttp
import asyncio

from holded.async_client import AsyncHoldedClient
from holded.exceptions import (
    HoldedAuthError, HoldedNotFoundError, HoldedValidationError,
    HoldedRateLimitError, HoldedServerError
)


class TestAsyncHoldedClient(unittest.TestCase):
    """Test cases for the AsyncHoldedClient class."""

    def setUp(self):
        """Set up test fixtures."""
        self.api_key = "test_api_key"
        self.client = AsyncHoldedClient(api_key=self.api_key)
        self.loop = asyncio.get_event_loop()

    def tearDown(self):
        """Tear down test fixtures."""
        if self.client.session:
            self.loop.run_until_complete(self.client.close())

    def test_init(self):
        """Test client initialization."""
        self.assertEqual(self.client.api_key, self.api_key)
        self.assertIsNone(self.client.session)  # Session is created on first request
        self.assertEqual(self.client.headers["Key"], self.api_key)

    @patch("aiohttp.ClientSession.request")
    def test_get(self, mock_request):
        """Test GET request."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json = asyncio.coroutine(lambda: {"id": "123", "name": "Test"})
        mock_response.status = 200
        mock_request.return_value.__aenter__.return_value = mock_response

        # Call method
        result = self.loop.run_until_complete(self.client.get("/test"))

        # Assertions
        mock_request.assert_called_once()
        self.assertEqual(mock_request.call_args[1]["method"], "GET")
        self.assertEqual(result, {"id": "123", "name": "Test"})

    @patch("aiohttp.ClientSession.request")
    def test_post(self, mock_request):
        """Test POST request."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json = asyncio.coroutine(lambda: {"id": "123", "name": "Test"})
        mock_response.status = 200
        mock_request.return_value.__aenter__.return_value = mock_response

        # Call method
        data = {"name": "Test"}
        result = self.loop.run_until_complete(self.client.post("/test", data=data))

        # Assertions
        mock_request.assert_called_once()
        self.assertEqual(mock_request.call_args[1]["method"], "POST")
        self.assertEqual(result, {"id": "123", "name": "Test"})

    @patch("aiohttp.ClientSession.request")
    def test_put(self, mock_request):
        """Test PUT request."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json = asyncio.coroutine(lambda: {"id": "123", "name": "Updated"})
        mock_response.status = 200
        mock_request.return_value.__aenter__.return_value = mock_response

        # Call method
        data = {"name": "Updated"}
        result = self.loop.run_until_complete(self.client.put("/test/123", data=data))

        # Assertions
        mock_request.assert_called_once()
        self.assertEqual(mock_request.call_args[1]["method"], "PUT")
        self.assertEqual(result, {"id": "123", "name": "Updated"})

    @patch("aiohttp.ClientSession.request")
    def test_delete(self, mock_request):
        """Test DELETE request."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json = asyncio.coroutine(lambda: {"success": True})
        mock_response.status = 200
        mock_request.return_value.__aenter__.return_value = mock_response

        # Call method
        result = self.loop.run_until_complete(self.client.delete("/test/123"))

        # Assertions
        mock_request.assert_called_once()
        self.assertEqual(mock_request.call_args[1]["method"], "DELETE")
        self.assertEqual(result, {"success": True})

    @patch("aiohttp.ClientSession.request")
    def test_auth_error(self, mock_request):
        """Test authentication error."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json = asyncio.coroutine(lambda: {"error": "Invalid API key"})
        mock_response.status = 401
        mock_request.return_value.__aenter__.return_value = mock_response

        # Call method and assert exception
        with self.assertRaises(HoldedAuthError):
            self.loop.run_until_complete(self.client.get("/test"))

    @patch("aiohttp.ClientSession.request")
    def test_not_found_error(self, mock_request):
        """Test not found error."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json = asyncio.coroutine(lambda: {"error": "Resource not found"})
        mock_response.status = 404
        mock_request.return_value.__aenter__.return_value = mock_response

        # Call method and assert exception
        with self.assertRaises(HoldedNotFoundError):
            self.loop.run_until_complete(self.client.get("/test/123"))

    @patch("aiohttp.ClientSession.request")
    def test_validation_error(self, mock_request):
        """Test validation error."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json = asyncio.coroutine(lambda: {"error": "Validation failed"})
        mock_response.status = 422
        mock_request.return_value.__aenter__.return_value = mock_response

        # Call method and assert exception
        with self.assertRaises(HoldedValidationError):
            self.loop.run_until_complete(self.client.post("/test", data={}))

    @patch("aiohttp.ClientSession.request")
    def test_rate_limit_error(self, mock_request):
        """Test rate limit error."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json = asyncio.coroutine(lambda: {"error": "Rate limit exceeded"})
        mock_response.status = 429
        mock_request.return_value.__aenter__.return_value = mock_response

        # Call method and assert exception
        with self.assertRaises(HoldedRateLimitError):
            self.loop.run_until_complete(self.client.get("/test"))

    @patch("aiohttp.ClientSession.request")
    def test_server_error(self, mock_request):
        """Test server error."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json = asyncio.coroutine(lambda: {"error": "Internal server error"})
        mock_response.status = 500
        mock_request.return_value.__aenter__.return_value = mock_response

        # Call method and assert exception
        with self.assertRaises(HoldedServerError):
            self.loop.run_until_complete(self.client.get("/test"))


if __name__ == "__main__":
    unittest.main() 