
import asyncio
from agridata.service import AgriDataAsyncService

async def main():
    service = AgriDataAsyncService()
    prices = await service.cereals.get_prices(memberStateCodes="IT")
    print(prices)

asyncio.run(main())
