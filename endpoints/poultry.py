from ..client import AgriDataClient
from ..queries import BaseQuery
from ..enums import EGGS_POULTRY_SERVICES
from .base import BaseAPI


class PoultryAPI(BaseAPI):
    SERVICES = EGGS_POULTRY_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)


for _service in PoultryAPI.SERVICES:
    _name = _service.replace('/', '_')

    def _sync(self, **kwargs, _svc=_service):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return self.client._get('poultry', _svc, query.dict())

    async def _async(self, **kwargs, _svc=_service):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('poultry', _svc, query.dict())

    setattr(PoultryAPI, f"get_{_name}", _sync)
    setattr(PoultryAPI, f"get_{_name}_async", _async)
