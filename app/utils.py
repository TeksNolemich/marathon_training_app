from typing import List


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

def get_week_workout_as_dict(runs: List[int]):
    """return Dict Object of the Week -> {Day: Miles To Run}"""
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    week_as_dict = {}
    for i, d in enumerate(days):
        week_as_dict[d] = runs[i]
        
    return week_as_dict