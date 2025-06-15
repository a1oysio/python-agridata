from ..client import AgriDataClient
from ..queries import BaseQuery
from ..enums import FERTILISER_SERVICES
from .base import BaseAPI


class FertiliserAPI(BaseAPI):
    SERVICES = FERTILISER_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)


for _service in FertiliserAPI.SERVICES:
    _name = _service.replace('/', '_')

    def _sync(self, **kwargs, _svc=_service):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return self.client._get('fertiliser', _svc, query.dict())

    async def _async(self, **kwargs, _svc=_service):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('fertiliser', _svc, query.dict())

    setattr(FertiliserAPI, f"get_{_name}", _sync)
    setattr(FertiliserAPI, f"get_{_name}_async", _async)
