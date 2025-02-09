vehicle_data = {
    "MH12AB1234": {"owner": "Rahul Sharma", "model": "Hyundai i20", "year": "2019"},
    "CG17KK2369": {"owner": "Amit Verma", "model": "Honda City", "year": "2021"},
    "CG17KT6706": {"owner": "Tushar Sahu", "model": "Hero Super Splendor", "year": "2022"},
}

def get_vehicle_details(plate_number):
    """Retrieve vehicle details based on the number plate."""
    return vehicle_data.get(plate_number, None)

def add_vehicle_details(plate_number, owner, model, year):
    """Add a new vehicle entry to the database."""
    vehicle_data[plate_number] = {"owner": owner, "model": model, "year": year}
    print(f"Vehicle {plate_number} added successfully!")
