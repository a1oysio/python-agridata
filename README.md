# AgriData

`agridata` is an unofficial lightweight Python wrapper for the [European Commission's AgriData API](https://agridata.ec.europa.eu/extensions/DataPortal/API_Documentation.html).
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

# Increase the request timeout to 30 seconds
svc = AgriDataService(timeout=30)

# call the API, for example beef prices
data = svc.beef.get_prices(years=2023)
```

The `AgriDataService` object contains attributes for every API category
(e.g. `beef`, `pigmeat`, `dairy`, ...). Each attribute exposes `get_*`
methods corresponding to the services listed in the [official API](https://agridata.ec.europa.eu/extensions/DataPortal/API_Documentation.html).

## Examples

The following snippets show how to query a few different categories using only
this package:

```python
# The timeout can be adjusted if needed
svc = AgriDataService(timeout=30)

# Beef prices
beef_data = svc.beef.get_prices(years=2023)

# Pigmeat production
pigmeat_data = svc.pigmeat.get_production(years=2023)

# Cereal markets
cereal_markets = svc.cereal.get_markets()

# Raw milk prices
milk_prices = svc.raw_milk.get_prices(years=2023)
```

## Running Tests

Install the package and test dependencies, then execute `pytest`:

```bash
pip install -e .
pip install pytest requests
pytest
```
