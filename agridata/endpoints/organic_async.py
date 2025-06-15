from ..client import AsyncAgriDataClient
from ..queries import BaseQuery
from ..enums import ORGANIC_SERVICES
from .base import BaseAPI


class OrganicAPI(BaseAPI):
    SERVICES = ORGANIC_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

for _service in OrganicAPI.SERVICES:
    _name = _service.replace('/', '_')

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('organic', _svc, query.dict())

    setattr(OrganicAPI, f"get_{_name}", _async)
