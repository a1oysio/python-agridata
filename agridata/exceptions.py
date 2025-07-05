class AgriDataError(Exception):
    """Base exception for AgriData errors."""


class AgriDataHTTPError(AgriDataError):
    """Raised when the API returns a non-successful HTTP response."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"{status_code}: {message}")
