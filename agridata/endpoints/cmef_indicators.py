from ..client import AgriDataClient
from ..queries import BaseQuery
from ..enums import CMEF_INDICATORS_SERVICES
from .base import BaseAPI


class CmefIndicatorsAPI(BaseAPI):
    SERVICES = CMEF_INDICATORS_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)


for _service in CmefIndicatorsAPI.SERVICES:
    _name = _service.replace('/', '_')

    def _sync(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return self.client._get('cmefIndicators', _svc, query.dict())

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('cmefIndicators', _svc, query.dict())

    setattr(CmefIndicatorsAPI, f"get_{_name}", _sync)
    setattr(CmefIndicatorsAPI, f"get_{_name}_async", _async)
