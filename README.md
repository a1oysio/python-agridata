# python-agridata

Python wrapper for the European Commission AgriData API.

## Installation

Clone the repository and install the dependencies manually (only `requests` is currently required):

```bash
git clone https://github.com/carazzolo/python-agridata.git
cd python-agridata
pip install requests
```

## Usage

The API is synchronous. Create a service instance and call the available endpoints:

```python
from agridata.service import AgriDataService

service = AgriDataService()
prices = service.cereals.get_prices(memberStateCodes="IT", marketingYears="2024")
print(prices)
```

## Available services

Each product category exposes different services. The table below lists the
currently supported products and their services as defined by the official API.

| Product | Services |
|---------|---------|
| cereals | prices, products, stages, markets, production, production/crops |
All query classes accept a common set of parameters used when calling the API:
`memberStateCodes`, `categories`, `productCodes`, `marketingYears`, `weeks`, `months`,
`beginDate` and `endDate`.

## Examples and tests

Example scripts will be placed in the `examples/` folder. After cloning the repository you will be able to run them with:

```bash
python examples/<example_name>.py
```

Tests will be runnable with `pytest` once they are added:

```bash
pytest
```

