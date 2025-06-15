
__all__ = []

from datetime import datetime

DATE_FIELDS = {"beginDate", "endDate"}
DATE_FORMAT = "%d/%m/%Y"

class BaseQuery:
    VALID_PARAMS = None  # override in subclasses

    def __init__(self, **params):
        if self.VALID_PARAMS is not None:
            unknown = set(params) - set(self.VALID_PARAMS)
            if unknown:
                raise ValueError(f"Invalid parameters: {', '.join(sorted(unknown))}")

        processed = {}
        for name, value in params.items():
            if name in DATE_FIELDS and value is not None:
                if isinstance(value, datetime):
                    value = value.strftime(DATE_FORMAT)
                elif isinstance(value, str):
                    try:
                        datetime.strptime(value, DATE_FORMAT)
                    except ValueError as exc:
                        raise ValueError(f"{name} must be in dd/mm/yyyy format") from exc
                else:
                    raise TypeError(f"{name} must be a datetime or dd/mm/yyyy string")
            processed[name] = value

        self.params = processed

    def dict(self):
        return {k: v for k, v in self.params.items() if v is not None}
