from ..client import AsyncAgriDataClient
from ..queries import BaseQuery
from ..enums import RICE_SERVICES
from .base import BaseAPI


class RiceAPI(BaseAPI):
    SERVICES = RICE_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

for _service in RiceAPI.SERVICES:
    _name = _service.replace('/', '_')

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('rice', _svc, query.dict())

    setattr(RiceAPI, f"get_{_name}", _async)
