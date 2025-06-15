from ..client import AgriDataClient
from ..queries import BaseQuery
from ..enums import PIGMEAT_SERVICES
from .base import BaseAPI


class PigmeatAPI(BaseAPI):
    SERVICES = PIGMEAT_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)


for _service in PigmeatAPI.SERVICES:
    _name = _service.replace('/', '_')

    def _sync(self, **kwargs, _svc=_service):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return self.client._get('pigmeat', _svc, query.dict())

    async def _async(self, **kwargs, _svc=_service):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('pigmeat', _svc, query.dict())

    setattr(PigmeatAPI, f"get_{_name}", _sync)
    setattr(PigmeatAPI, f"get_{_name}_async", _async)
