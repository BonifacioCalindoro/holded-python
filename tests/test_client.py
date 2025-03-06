"""
Unit tests for the Holded client.
"""
import unittest
from unittest.mock import patch, MagicMock

from holded.client import HoldedClient
from holded.exceptions import (
    HoldedAuthError, HoldedNotFoundError, HoldedValidationError,
    HoldedRateLimitError, HoldedServerError
)


class TestHoldedClient(unittest.TestCase):
    """Test cases for the HoldedClient class."""

    def setUp(self):
        """Set up test fixtures."""
        self.api_key = "test_api_key"
        self.client = HoldedClient(api_key=self.api_key)

    def tearDown(self):
        """Tear down test fixtures."""
        self.client.close()

    def test_init(self):
        """Test client initialization."""
        self.assertEqual(self.client.api_key, self.api_key)
        self.assertIsNotNone(self.client.session)
        self.assertEqual(self.client.session.headers["Key"], self.api_key)

    @patch("requests.Session.request")
    def test_get(self, mock_request):
        """Test GET request."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "123", "name": "Test"}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        # Call method
        result = self.client.get("/test")

        # Assertions
        mock_request.assert_called_once()
        self.assertEqual(mock_request.call_args[1]["method"], "GET")
        self.assertEqual(result, {"id": "123", "name": "Test"})

    @patch("requests.Session.request")
    def test_post(self, mock_request):
        """Test POST request."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "123", "name": "Test"}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        # Call method
        data = {"name": "Test"}
        result = self.client.post("/test", data=data)

        # Assertions
        mock_request.assert_called_once()
        self.assertEqual(mock_request.call_args[1]["method"], "POST")
        self.assertEqual(result, {"id": "123", "name": "Test"})

    @patch("requests.Session.request")
    def test_put(self, mock_request):
        """Test PUT request."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "123", "name": "Updated"}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        # Call method
        data = {"name": "Updated"}
        result = self.client.put("/test/123", data=data)

        # Assertions
        mock_request.assert_called_once()
        self.assertEqual(mock_request.call_args[1]["method"], "PUT")
        self.assertEqual(result, {"id": "123", "name": "Updated"})

    @patch("requests.Session.request")
    def test_delete(self, mock_request):
        """Test DELETE request."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        # Call method
        result = self.client.delete("/test/123")

        # Assertions
        mock_request.assert_called_once()
        self.assertEqual(mock_request.call_args[1]["method"], "DELETE")
        self.assertEqual(result, {"success": True})

    @patch("requests.Session.request")
    def test_auth_error(self, mock_request):
        """Test authentication error."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"error": "Invalid API key"}
        mock_response.status_code = 401
        mock_response.raise_for_status.side_effect = Exception("401 Client Error")
        mock_request.return_value = mock_response

        # Call method and assert exception
        with self.assertRaises(HoldedAuthError):
            self.client.get("/test")

    @patch("requests.Session.request")
    def test_not_found_error(self, mock_request):
        """Test not found error."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"error": "Resource not found"}
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = Exception("404 Client Error")
        mock_request.return_value = mock_response

        # Call method and assert exception
        with self.assertRaises(HoldedNotFoundError):
            self.client.get("/test/123")

    @patch("requests.Session.request")
    def test_validation_error(self, mock_request):
        """Test validation error."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"error": "Validation failed"}
        mock_response.status_code = 422
        mock_response.raise_for_status.side_effect = Exception("422 Client Error")
        mock_request.return_value = mock_response

        # Call method and assert exception
        with self.assertRaises(HoldedValidationError):
            self.client.post("/test", data={})

    @patch("requests.Session.request")
    def test_rate_limit_error(self, mock_request):
        """Test rate limit error."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"error": "Rate limit exceeded"}
        mock_response.status_code = 429
        mock_response.raise_for_status.side_effect = Exception("429 Client Error")
        mock_request.return_value = mock_response

        # Call method and assert exception
        with self.assertRaises(HoldedRateLimitError):
            self.client.get("/test")

    @patch("requests.Session.request")
    def test_server_error(self, mock_request):
        """Test server error."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {"error": "Internal server error"}
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = Exception("500 Server Error")
        mock_request.return_value = mock_response

        # Call method and assert exception
        with self.assertRaises(HoldedServerError):
            self.client.get("/test")


if __name__ == "__main__":
    unittest.main() 