from geopy.distance import geodesic
from Config import DB

async def get_couriers():
    async with DB() as conn:
        couriers = await conn.fetch('SELECT ID, latitude, longitude FROM courier')

    couriers_list = [{'ID': courier['id'], 'latitude': courier['latitude'], 'longitude': courier['longitude']} for courier in couriers]

    valid_couriers = [courier for courier in couriers_list if courier['latitude'] is not None and courier['longitude'] is not None]

    return valid_couriers if valid_couriers else None


async def filter_couriers(couriers, address, radius_km=1):
    filtered_couriers = []
    for courier in couriers:
        courier_coords = (courier['latitude'], courier['longitude'])
        distance = geodesic(address, courier_coords).kilometers
        if distance <= radius_km:
            filtered_couriers.append(courier)
    return filtered_couriers if filtered_couriers else None


async def main_function():
    couriers = await get_couriers()
    if couriers:
        address = (43.229375, 76.948258)
        filtered_couriers = await filter_couriers(couriers, address)
        print(filtered_couriers)


# Запуск основной функции
import asyncio

asyncio.run(main_function())
