from geopy.distance import geodesic
from Config import DB


async def get_couriers():
    async with DB() as conn:
        couriers = await conn.fetch('SELECT ID, latitude, longitude FROM courier')

    couriers_list = []
    for courier in couriers:
        courier_dict = {'ID': courier['id'], 'latitude': courier['latitude'], 'longitude': courier['longitude']}
        couriers_list.append(courier_dict)

    valid_couriers = [courier for courier in couriers_list if courier['latitude'] is not None and courier['longitude'] is not None]

    return valid_couriers if valid_couriers else None


async def filter_couriers(couriers, address, radius_km=1.5):
    filtered_couriers = []
    for courier in couriers:
        courier_coords = (courier['latitude'], courier['longitude'])
        distance = geodesic(address, courier_coords).kilometers
        if distance <= radius_km:
            filtered_couriers.append(courier)
    return filtered_couriers if filtered_couriers else None


async def choose_courier(filtered_couriers, address):
    valid_couriers = await get_couriers()

    if not valid_couriers or not address:
        return None

    closest_courier = None
    shortest_distance = float('inf')

    for courier in filtered_couriers:
        courier_coords = (courier['latitude'], courier['longitude'])
        distance = geodesic(address, courier_coords).kilometers
        if distance < shortest_distance:
            shortest_distance = distance
            closest_courier = courier

    if closest_courier:
        closest_courier_id = closest_courier['ID']
        return closest_courier_id
    else:
        return None