from ..client import AsyncAgriDataClient
from ..enums import ORGANIC_SERVICES
from .base import BaseAPI


class OrganicAPI(BaseAPI):
    SERVICES = ORGANIC_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

for _service in OrganicAPI.SERVICES:
    _name = _service.replace('/', '_')

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get('organic', _svc, params)

    setattr(OrganicAPI, f"get_{_name}", _async)
