from ..client import AsyncAgriDataClient
from ..queries import BaseQuery
from ..enums import LIVE_ANIMAL_SERVICES
from .base import BaseAPI


class LiveAnimalAPI(BaseAPI):
    SERVICES = LIVE_ANIMAL_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

for _service in LiveAnimalAPI.SERVICES:
    _name = _service.replace('/', '_')

    async def _async(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        query = BaseQuery(**kwargs)
        return await self.client._get('liveAnimal', _svc, query.dict())

    setattr(LiveAnimalAPI, f"get_{_name}", _async)
