from ..client import AsyncAgriDataClient
from ..enums import PIGMEAT_SERVICES
from .base import BaseAPI


class PigmeatAPI(BaseAPI):
    SERVICES = PIGMEAT_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

for _service in PigmeatAPI.SERVICES:
    _name = _service.replace('/', '_')

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get('pigmeat', _svc, params)

    setattr(PigmeatAPI, f"get_{_name}", _async)
