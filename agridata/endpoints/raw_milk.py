from ..client import AgriDataClient
from ..enums import MILK_SERVICES
from .base import BaseAPI


class RawMilkAPI(BaseAPI):
    SERVICES = MILK_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)


for _service in RawMilkAPI.SERVICES:
    _name = _service.replace('/', '_')

    def _sync(self, _svc=_service, **kwargs):
        self._validate_service(_svc)
        params = {k: v for k, v in kwargs.items() if v is not None}
        return self.client._get('rawMilk', _svc, params)

    setattr(RawMilkAPI, f"get_{_name}", _sync)
