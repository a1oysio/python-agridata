from ..client import AgriDataClient
from ..queries import BaseQuery
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
        query = BaseQuery(**kwargs)
        return self.client._get('dairy', _svc, query.dict())

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('dairy', _svc, query.dict())

    setattr(DairyAPI, f"get_{_name}", _sync)
    setattr(DairyAPI, f"get_{_name}_async", _async)
