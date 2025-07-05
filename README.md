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

## Examples

The following snippets show how to query a few different categories using only
this package:

```python
svc = AgriDataService()

# Beef prices
beef_data = svc.beef.get_prices(year=2023)

# Pigmeat production
pigmeat_data = svc.pigmeat.get_production(year=2023)

# Cereal markets
cereal_markets = svc.cereal.get_markets()

# Raw milk prices
milk_prices = svc.raw_milk.get_prices(year=2023)
```

## Running Tests

Install the package and test dependencies, then execute `pytest`:

```bash
pip install -e .
pip install pytest requests
pytest
```
