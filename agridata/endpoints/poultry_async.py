from ..client import AsyncAgriDataClient
from ..queries import BaseQuery
from ..enums import EGGS_POULTRY_SERVICES
from .base import BaseAPI


class PoultryAPI(BaseAPI):
    SERVICES = EGGS_POULTRY_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

for _service in PoultryAPI.SERVICES:
    _name = _service.replace('/', '_')

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('poultry', _svc, query.dict())

    setattr(PoultryAPI, f"get_{_name}", _async)
