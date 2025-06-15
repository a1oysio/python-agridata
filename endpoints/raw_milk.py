from ..client import AgriDataClient
from ..queries import BaseQuery
from ..enums import MILK_SERVICES
from .base import BaseAPI


class RawMilkAPI(BaseAPI):
    SERVICES = MILK_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)


for _service in RawMilkAPI.SERVICES:
    _name = _service.replace('/', '_')

    def _sync(self, **kwargs, _svc=_service):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return self.client._get('rawMilk', _svc, query.dict())

    async def _async(self, **kwargs, _svc=_service):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('rawMilk', _svc, query.dict())

    setattr(RawMilkAPI, f"get_{_name}", _sync)
    setattr(RawMilkAPI, f"get_{_name}_async", _async)
