LOCATIONS = [
    {
        "id": 1,
        "name": "location1",
        "species": "location1",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "location2",
        "species": "location2",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "location3",
        "species": "location3",
        "locationId": 2,
        "customerId": 1
    }
]

def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    
    return requested_location

def get_all_locations():
    return LOCATIONS

def create_location(location):
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location

def delete_location(id):
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break