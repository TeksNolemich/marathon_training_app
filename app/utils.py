def round_weekly_mileage(mileage: int)-> int:
    """round weekly mileage for running schedule creation"""
    if mileage <= 40:
        return 40
    elif mileage > 41 and mileage <= 55:
        return 55
    elif mileage > 55 and mileage <= 70:
        return 70
    elif mileage > 71 and mileage <= 85:
        return 85
    elif mileage > 85 and mileage <= 100:
        return 100
    elif mileage > 100 and mileage <= 120:
        return 120
    elif mileage > 120:
        return 121
    