# python-agridata

Python wrapper for the European Commission AgriData API.

## Installation

Clone the repository and install the package:

```bash
git clone https://github.com/carazzolo/python-agridata.git
cd python-agridata
pip install .
```

The package depends only on `requests`, which is installed automatically.

## Usage

The API is synchronous. Create a service instance and call the available endpoints:

```python
from agridata.service import AgriDataService

service = AgriDataService()
prices = service.cereal.get_prices(memberStateCodes="IT", marketingYears="2024")
print(prices)
```

## Available services

Each product category exposes different services. The table below lists the
currently supported products and their services as defined by the official API.

| Product | Services |
|---------|---------|
| beef | prices, categories, productCodes, production, production/categories |
| liveAnimal | prices, categories |
| pigmeat | prices, cuts/prices, cuts/categories, cuts/priceTypes, cuts/prices/month, cuts/prices/month/categories, cuts/prices/month/priceTypes, production |
| poultry | prices, priceTypes, prices/month, prices/month/priceTypes, egg/prices, egg/farmingMethods, production, production/animals |
| sheepAndGoat | prices, categories, markets, production, production/meats, production/items |
| rawMilk | prices, products |
| dairy | prices, products, production, production/categories |
| cereal | prices, products, stages, markets, production, production/crops |
| rice | prices, stages, types, varieties, memberStates, production, production/types, production/products |
| oilseeds | prices, products, productTypes, markets, marketStages, production, production/crops, crops/prices, crops/products, crops/productTypes, crops/marketStages |
| sugar | prices, regions, production, production/regions |
| oliveOil | prices, products, markets, memberStates, production |
| wine | prices, descriptions |
| taxud | weeklyData/import, weeklyData/sectors, weeklyData/importCategories, weeklyData/import/cn8ProductCodes, weeklyData/import/taric10ProductCodes, weeklyData/import/products, weeklyData/export, weeklyData/export/cn8ProductCodes, weeklyData/export/taric10ProductCodes, weeklyData/export/products |
| cmefIndicators | values, types, categories, indicators, subIndicators, parameters, units, codes, sources |
| fertiliser | prices, prices/products |
| organic | prices, sectors, organicProducts, overallProducts |
All query classes accept a common set of parameters used when calling the API:
`memberStateCodes`, `categories`, `productCodes`, `marketingYears`, `weeks`, `months`,
`beginDate` and `endDate`.

## Examples and tests

Example scripts live in the `examples/` folder and are intentionally minimal.
They rely only on Python's standard library and this package. Any previous
demonstrations that used third–party tools like pandas or matplotlib have been
removed to keep the examples lightweight. After cloning the repository you can
run a script with:

```bash
python examples/<example_name>.py
```

For a quick demonstration run the `basic_usage.py` script:

```bash
python examples/basic_usage.py
```

### Running tests

The project uses `pytest` for its test suite. From the repository root simply
run:

```bash
pytest
```

