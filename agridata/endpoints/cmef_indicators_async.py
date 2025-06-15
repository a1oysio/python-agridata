from ..client import AsyncAgriDataClient
from ..queries import BaseQuery
from ..enums import CMEF_INDICATORS_SERVICES
from .base import BaseAPI


class CmefIndicatorsAPI(BaseAPI):
    SERVICES = CMEF_INDICATORS_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

for _service in CmefIndicatorsAPI.SERVICES:
    _name = _service.replace('/', '_')

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('cmefIndicators', _svc, query.dict())

    setattr(CmefIndicatorsAPI, f"get_{_name}", _async)
