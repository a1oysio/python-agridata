from ..client import AsyncAgriDataClient
from ..enums import SUGAR_SERVICES
from .base import BaseAPI


class SugarAPI(BaseAPI):
    SERVICES = SUGAR_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

for _service in SugarAPI.SERVICES:
    _name = _service.replace('/', '_')

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get('sugar', _svc, params)

    setattr(SugarAPI, f"get_{_name}", _async)
