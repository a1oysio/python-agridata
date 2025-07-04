from agridata.service import AgriDataService

service = AgriDataService()
# prices = service.cereal.get_prices(memberStateCodes="IT")
prices = service.oilseeds.get_prices(memberStateCodes="IT")
# productions = service.cereals.get_production(memberStateCodes="IT")
products = service.oilseeds.get_products()

print(products)
