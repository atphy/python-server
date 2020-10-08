EMPLOYEES = [
    {
        "id": 1,
        "name": "employee1",
        "species": "employee1",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "employee2",
        "species": "employee2",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "employee3",
        "species": "employee3",
        "locationId": 2,
        "customerId": 1
    }
]

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def get_all_employees():
    return EMPLOYEES