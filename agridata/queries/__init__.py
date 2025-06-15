
__all__ = []

class BaseQuery:
    VALID_PARAMS = None  # override in subclasses

    def __init__(self, **params):
        if self.VALID_PARAMS is not None:
            unknown = set(params) - set(self.VALID_PARAMS)
            if unknown:
                raise ValueError(f"Invalid parameters: {', '.join(sorted(unknown))}")
        self.params = params

    def dict(self):
        return {k: v for k, v in self.params.items() if v is not None}
