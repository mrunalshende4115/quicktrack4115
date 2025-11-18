def check_out(vehicle_id, location):
    return {
        "vehicle_id": vehicle_id,
        "status": "in_use",
        "location": location
    }