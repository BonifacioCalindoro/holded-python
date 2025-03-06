"""
Exceptions for the Holded API.
"""
from typing import Any, Dict, Optional


class HoldedError(Exception):
    """Base exception for all Holded API errors."""

    def __init__(self, message: str, status_code: Optional[int] = None, error_data: Optional[Dict[str, Any]] = None):
        """Initialize the exception.

        Args:
            message: The error message.
            status_code: The HTTP status code.
            error_data: Additional error data from the API.
        """
        self.message = message
        self.status_code = status_code
        self.error_data = error_data or {}
        super().__init__(self.message)


class HoldedAPIError(HoldedError):
    """Exception for API errors."""
    pass


class HoldedAuthError(HoldedAPIError):
    """Exception for authentication errors."""
    pass


class HoldedNotFoundError(HoldedAPIError):
    """Exception for resource not found errors."""
    pass


class HoldedValidationError(HoldedAPIError):
    """Exception for validation errors."""
    pass


class HoldedRateLimitError(HoldedAPIError):
    """Exception for rate limit errors."""
    pass


class HoldedServerError(HoldedAPIError):
    """Exception for server errors."""
    pass


class HoldedTimeoutError(HoldedError):
    """Exception for request timeout errors."""
    pass


class HoldedConnectionError(HoldedError):
    """Exception for connection errors."""
    pass 