class BaseAPI:
    SERVICES = None

    def __init__(self, client):
        self.client = client

    def _validate_service(self, service: str):
        if self.SERVICES is not None and service not in self.SERVICES:
            raise ValueError(f"Service '{service}' not supported")
