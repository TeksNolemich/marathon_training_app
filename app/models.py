import random
from typing import Iterator, List

class WeekWorkout:
    def __init__(self, mileage):
        self.mileage = mileage
        
    def get_workout_for_week(self) -> List[int]:
        """return 7 day running workout for the given mileage"""
        """
            Long Run = 25-30% of total weekly mileage
            Medium Long Run = 20-25% of total weekly mileage
            Remaining 3 days = (40%, 30% 30%)
        """
        """Long Runs always on Race Day, default to Sunday, and Medium Long Run default to Wednesday"""
        #group long run and medium long run together
        long_run = round(self.mileage * (random.randrange(25,31)/100))
        medium_long_run = round(self.mileage * (random.randrange(20,25)/100))
        #obtain remaining mileage to divvy up 
        remaining_mileage = self.mileage - long_run - medium_long_run
        #logic to designate miles for rest of the days
        long_short = round(remaining_mileage * (random.randrange(30,40)/100))
        short_one = round((remaining_mileage - long_short) / 2)
        short_two = remaining_mileage - (long_short + short_one)
        short_runs_shuffled = [long_short, short_one, short_two, None, None]
        #shuffle remaining day to sprinkle throughout week
        random.shuffle(short_runs_shuffled)
        week = []
        for d in range(8):
            if (d == 2):
                week.append(medium_long_run)
            elif d == 7:
                week.append(long_run)
            else:
                if len(short_runs_shuffled) > 0:                    
                    run = short_runs_shuffled.pop()
                    week.append(run)
        return week
            

class WeekWorkOutWithQualitySessions(WeekWorkout):
    def __init__(self, mileage, quality_one, quality_two):
        self.mileage = mileage
        self.quality_one = quality_one
        self.quality_two = quality_two
        # self.last_training_week = last_training_week
    
    def get_workout_for_week(self):
        """return 7 day running workout for the given mileage"""
        long_run = self.quality_one if self.quality_one > self.quality_two else self.quality_two
        medium_long_run = self.quality_two if long_run == self.quality_one else self.quality_one
        remaining_mileage = self.mileage - (long_run + medium_long_run)
        
        long_short = round(remaining_mileage * (random.randrange(30,40)/100))
        short_one = round((remaining_mileage - long_short) / 2)
        short_two = remaining_mileage - (long_short + short_one)
        short_runs_shuffled = [long_short, short_one, short_two, None, None]
        random.shuffle(short_runs_shuffled)
        week = []
        for d in range(8):
            if (d == 2):
                week.append(medium_long_run)
            elif d == 7:
                week.append(long_run)
            else:
                if len(short_runs_shuffled) > 0:                    
                    run = short_runs_shuffled.pop()
                    week.append(run)
        return week
        

