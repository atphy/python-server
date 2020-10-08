CUSTOMERS = [
    {
        "id": 1,
        "name": "customer1",
        "species": "customer1",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "customer2",
        "species": "customer2",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "customer3",
        "species": "customer3",
        "locationId": 2,
        "customerId": 1
    }
]

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
          requested_customer = customer

    return requested_customer

def get_all_customers():
    return CUSTOMERS