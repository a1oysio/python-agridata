from ..client import AsyncAgriDataClient
from ..enums import WINE_SERVICES
from .base import BaseAPI


class WineAPI(BaseAPI):
    SERVICES = WINE_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

for _service in WineAPI.SERVICES:
    _name = _service.replace('/', '_')

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get('wine', _svc, params)

    setattr(WineAPI, f"get_{_name}", _async)
