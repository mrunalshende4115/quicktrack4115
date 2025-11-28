def check_in(vehicle_id, location):
    #Mark a vehicle as available at the specified location
    return {
        "vehicle_id": vehicle_id,
        "status": "available",
        "location": location
    }
