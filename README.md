# AgriData

`agridata` is a lightweight Python wrapper for the European Commission's AgriData API.
It exposes the various API categories as Python classes with convenient methods for
each available service.

## Installation

Clone this repository and install it using pip:

```bash
pip install .
```

## Usage

```python
from agridata import AgriDataService

svc = AgriDataService()

# call the API, for example beef prices
data = svc.beef.get_prices(year=2023)
```

The `AgriDataService` object contains attributes for every API category
(e.g. `beef`, `pigmeat`, `dairy`, ...). Each attribute exposes `get_*`
methods corresponding to the services listed in the official API.
