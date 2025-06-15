# python-agridata

Python wrapper for the European Commission AgriData API.

## Installation

Clone the repository and install the dependencies manually (only `requests` is currently required):

```bash
git clone https://github.com/carazzolo/python-agridata.git
cd python-agridata
pip install requests
```

## API key configuration

An API key is required to access the AgriData endpoints. Pass the key when creating a client or service instance:

```python
from python_agridata.service import AgriDataService

service = AgriDataService(api_key="YOUR_API_KEY")
```

## Usage

### Synchronous client

The `AgriDataService` uses a synchronous client under the hood:

```python
from python_agridata.service import AgriDataService

service = AgriDataService(api_key="YOUR_API_KEY")
prices = service.cereals.get_prices(memberStateCodes="IT", marketingYears="2024")
print(prices)
```

### Asynchronous client

An asynchronous interface will be available in future releases. Once implemented you will be able to use it as follows:

```python
import asyncio
from python_agridata.async_service import AgriDataServiceAsync

async def main():
    service = AgriDataServiceAsync(api_key="YOUR_API_KEY")
    prices = await service.cereals.get_prices(memberStateCodes="IT", marketingYears="2024")
    print(prices)

asyncio.run(main())
```

## Available services

Each product category exposes different services. The table below lists the
currently supported products and their services as defined by the official API.

| Product | Services |
|---------|---------|
| cereals | prices, products, stages, markets, production, production/crops |
| meat    | prices |

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

