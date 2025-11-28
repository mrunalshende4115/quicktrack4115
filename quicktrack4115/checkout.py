def check_out(vehicle_id, location):
    # Mark a vehicle as in use at the specified location
    return {
        "vehicle_id": vehicle_id,
        "status": "in_use",
        "location": location
    }
