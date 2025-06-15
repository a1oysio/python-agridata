from ..client import AsyncAgriDataClient
from ..queries import BaseQuery
from ..enums import OLIVE_OIL_SERVICES
from .base import BaseAPI


class OliveOilAPI(BaseAPI):
    SERVICES = OLIVE_OIL_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

for _service in OliveOilAPI.SERVICES:
    _name = _service.replace('/', '_')

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('oliveOil', _svc, query.dict())

    setattr(OliveOilAPI, f"get_{_name}", _async)
