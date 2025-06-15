from ..client import AgriDataClient
from ..queries import BaseQuery
from ..enums import WINE_SERVICES
from .base import BaseAPI


class WineAPI(BaseAPI):
    SERVICES = WINE_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)


for _service in WineAPI.SERVICES:
    _name = _service.replace('/', '_')

    def _sync(self, **kwargs, _svc=_service):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return self.client._get('wine', _svc, query.dict())

    async def _async(self, **kwargs, _svc=_service):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('wine', _svc, query.dict())

    setattr(WineAPI, f"get_{_name}", _sync)
    setattr(WineAPI, f"get_{_name}_async", _async)
