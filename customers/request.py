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

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer