import json
from datetime import datetime
import copy 
class Habit:
    def __init__(self, name, periodicity, created_At=None):
        self.name = name
        self.periodicity = periodicity
        self.created_At = created_At or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_streak = 0
        self.longest_streak = 0
        self.completed_dates = []
        self.isBroken = False
    # Method to create a shallow copy of the habit object
    @classmethod
    def from_existing_habit(cls, name, periodicity, habit_details):
        """Create a new Habit instance using an existing Habit object."""
        # Create a new instance of the Habit class using the class method
        habit = cls(
            name=name,
            periodicity=periodicity
        )
        # Populate other attributes from the passed habit_details
        habit.current_streak = habit_details["current_streak"]
        habit.longest_streak = habit_details["longest_streak"]
        habit.completed_dates = habit_details["completed_dates"]
        habit.isBroken = habit_details["isBroken"]
        return habit

    def complete(self):
        """Mark this habit as completed at a specific time."""
        completion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Check if the habit has already been completed today
        if self.periodicity == "daily":
            today = datetime.now().date()
            if any(datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date() == today for date in self.completed_dates):
                print("This habit has already been completed today.")
                return False
        
        elif self.periodicity == "weekly":
            current_week = datetime.now().isocalendar()[1]  # ISO week number
            if any(datetime.strptime(date, "%Y-%m-%d %H:%M:%S").isocalendar()[1] == current_week for date in self.completed_dates):
                print("This habit has already been completed this week.")
                return False
            
        # check using minutes instead of day and week for testing purposes    
        # if self.periodicity == "daily":
        # # Get the most recent completed date
        #     if self.completed_dates:
        #         last_completion_time = datetime.strptime(self.completed_dates[-1], "%Y-%m-%d %H:%M:%S")
        #         time_difference = (datetime.now() - last_completion_time).total_seconds()

        #         # Allow completion only if the time difference is greater than 60 seconds (1 minute)
        #         if time_difference <= 60:
        #             print("This habit has already been completed within the last minute.")
        #             return False
        #     else:
        #         print("No previous completion to check.")
            
        self.completed_dates.append(completion_time)
        self.update_streak(completion_time)
        return True


    def update_streak(self,completion_time):
        """Update the streak of the habit based on completion."""

        # Add logic here to update streak based on the periodicity and previous completion dates.
        flag = self.is_consecutive(self.completed_dates[-2:], completion_time, self.periodicity)
        if flag:
            self.current_streak += 1
            self.isBroken=False
        else:
            print("Habit Broken !")
            self.isBroken = True
            self.current_streak = 1  # Reset the streak

        # Update the longest streak
        if self.current_streak > self.longest_streak:
            self.longest_streak = self.current_streak

    def is_consecutive(self, last_dates, current_date,periodicity):
        """Check if the last two completion dates are consecutive (for daily habits)."""
        if len(last_dates) < 2:
            return True  # Assume consecutive if there is only one prior date

        last_date = datetime.strptime(last_dates[-2], "%Y-%m-%d %H:%M:%S")
        current_date = datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S")
        time_difference = (current_date - last_date).total_seconds()

        if periodicity == "daily":
            # 2 day in seconds for streak validity since first 24hrs habit catn be repeatedly completed due to redundancy
            # therefore to maintain the streak complete it within next 24hrs
            return time_difference <= 48 * 60 * 60  
            # return time_difference <= 3*60  # 3 minute in seconds
        elif periodicity == "weekly":
            # 14 days using the same understanding as before
            return time_difference <= 14 * 24 * 60 * 60  # 2 weeks in seconds
        