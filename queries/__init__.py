class BaseQuery:
    def __init__(self, **params):
        self.params = params

    def dict(self):
        return {k: v for k, v in self.params.items() if v is not None}
