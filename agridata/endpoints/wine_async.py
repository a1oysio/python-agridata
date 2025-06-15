from ..client import AsyncAgriDataClient
from ..queries import BaseQuery
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
        query = BaseQuery(**kwargs)
        return await self.client._get('wine', _svc, query.dict())

    setattr(WineAPI, f"get_{_name}", _async)
