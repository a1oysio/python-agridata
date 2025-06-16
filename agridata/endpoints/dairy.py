from ..client import AgriDataClient
from ..enums import DAIRY_SERVICES
from .base import BaseAPI


class DairyAPI(BaseAPI):
    SERVICES = DAIRY_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)


for _service in DairyAPI.SERVICES:
    _name = _service.replace('/', '_')

    def _sync(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        params = {k: v for k, v in kwargs.items() if v is not None}
        return self.client._get('dairy', _svc, params)

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get('dairy', _svc, params)

    setattr(DairyAPI, f"get_{_name}", _sync)
    setattr(DairyAPI, f"get_{_name}_async", _async)
