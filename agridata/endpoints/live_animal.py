from ..client import AgriDataClient
from ..enums import LIVE_ANIMAL_SERVICES
from .base import BaseAPI


class LiveAnimalAPI(BaseAPI):
    SERVICES = LIVE_ANIMAL_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)


for _service in LiveAnimalAPI.SERVICES:
    _name = _service.replace('/', '_')

    def _sync(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        params = {k: v for k, v in kwargs.items() if v is not None}
        return self.client._get('liveAnimal', _svc, params)

    setattr(LiveAnimalAPI, f"get_{_name}", _sync)
