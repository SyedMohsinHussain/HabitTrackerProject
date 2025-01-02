# habit_tracker.py
import json
from habit import Habit  # Import the Habit class from habit.py
from tabulate import tabulate # type: ignore
from utils import format_completed_dates
from Storage import HabitDataStore
class HabitTracker:
    def __init__(self, file_name="habits.json"):
        self.file_name = file_name
        self.storage = HabitDataStore(file_name)  # Initialize Storage object
        self.habits = self.storage.load_data()  # Load habit data {} using Storage


    def appendToDictionary(self,habit):
        try:
            # Ensure that habit.name and other attributes are accessible
            self.habits["habits"][habit.name] = {
                "periodicity": habit.periodicity,
                "current_streak": habit.current_streak,
                "longest_streak": habit.longest_streak,
                "createdAt": habit.created_At,
                "completed_dates": habit.completed_dates,
                "isBroken": habit.isBroken
            }
            self.storage.save_data(self.habits)  # save to JSON file
            print(f"Successfully added Habit {habit.name}")
        except Exception as e:
            print(f"An error occurred while appending habit: {e}")


    def add_habit(self, name, periodicity):
        """Add a new habit to the tracker."""
        if name.lower() in [habit.lower() for habit in self.habits["habits"]]:
            print(f"Habit '{name}' already exists.")
            return
        #new habit Instance
        habit = Habit(name, periodicity)
        self.appendToDictionary(habit)

    def view_all_habits(self):
        habit_data = []
        # Iterate through the habits in the dictionary (key,value) pairs
        for habit_name, habit_info in self.habits["habits"].items():
            habit_data.append([
                habit_name,  # Habit name
                habit_info["periodicity"],  # Habit periodicity (e.g., daily, weekly)
                habit_info["current_streak"],  # Current streak count
                habit_info["longest_streak"],  # Longest streak count
                habit_info["createdAt"],  # Created date
                format_completed_dates(habit_info["completed_dates"]),  # Completed dates (as a string)
                "Yes" if habit_info["isBroken"] else "No"  # If the habit is broken
            ])
        
        # Define the headers for the table
        headers = ["Habit Name", "Periodicity", "Current Streak", "Longest Streak", "Created At", "Completed Dates", "Is Broken"]
        print(tabulate(habit_data, headers=headers, tablefmt="grid"))

    def view_all_periodicity_habits(self,periodicity):
        """View all habits with a specific periodicity."""
        habit_data = []
        # Iterate through the habits in the dictionary (key,value) pairs
        for habit_name, habit_info in self.habits["habits"].items():
            if habit_info["periodicity"] == periodicity:
                habit_data.append([
                    habit_name,  # Habit name
                    habit_info["periodicity"],  # Habit periodicity (e.g., daily, weekly)
                    habit_info["current_streak"],  # Current streak count
                    habit_info["longest_streak"],  # Longest streak count
                    habit_info["createdAt"],  # Created date
                    format_completed_dates(habit_info["completed_dates"]),
                    "Yes" if habit_info["isBroken"] else "No"  # If the habit is broken
                ])
        # Define the headers for the table
        headers = ["Habit Name", "Periodicity", "Current Streak", "Longest Streak", "Created At", "Completed Dates", "Is Broken"]
        print(tabulate(habit_data, headers=headers, tablefmt="grid"))        

    def view_habit(self,habit_name):
        """View details of a specific habit."""
        habit = self.find_habit(habit_name)
        if habit == False:
            return habit
        
        # Retrieve habit details from the tracker
        habit_data = self.habits["habits"][habit]
        headers = ["Habit Name", "Periodicity", "Current Streak", "Longest Streak", "Created At", "Completed Dates", "Is Broken"]
        print(tabulate([[habit_name, habit_data["periodicity"], habit_data["current_streak"], habit_data["longest_streak"], habit_data["createdAt"], ", ".join(habit_data["completed_dates"]), habit_data["isBroken"]]], headers=headers, tablefmt="grid"))
        return True
    def find_habit(self,habit_name):
        """Find a habit by its name."""
        matching_habits = [key for key in self.habits["habits"] if key.lower() == habit_name.lower()]
        if not matching_habits:
            print("\n-----------------------------------------------------------------------------------------")
            print(f"Habit '{habit_name}' not found.")
            print("-----------------------------------------------------------------------------------------\n")
            return False
        
        # Return the correct Habit key from dictionary
        habit_key=matching_habits[0]
        return habit_key

    def complete_habit(self, habit_name):
        """Mark a habit as completed."""

        habit_key = self.find_habit(habit_name)
        if habit_key == False:
            return
        
        # Retrieve habit details from the tracker
        habit_data = self.habits["habits"][habit_key]

        # Create a shallow copy of Habit instance using the from_existing_habit class method
        habit = Habit.from_existing_habit(habit_key, habit_data["periodicity"], habit_data)

        # Mark the habit as completed
        if habit.complete():
            # Update habit data in the tracker since it was a shallow copy therefore non nested attributes needs to be manually updated
            self.habits["habits"][habit_key]["current_streak"] = habit.current_streak
            self.habits["habits"][habit_key]["longest_streak"] = habit.longest_streak
            self.habits["habits"][habit_key]["completed_dates"] = habit.completed_dates
            self.habits["habits"][habit_key]["isBroken"] = habit.isBroken
            # Save the updated data back to the tracker (or database, file, etc.)
            self.storage.save_data(self.habits)
            print(f"Habit '{habit_key}' completed.")


    def view_longest_streak(self, habit_name=None):
        """Get the longest streak for a specific habit."""
        if habit_name:
        
            habit_key = self.find_habit(habit_name)
            if habit_key == False:
                return
            
            habit_data = self.habits["habits"][habit_key]
            print("\n-----------------------------------------------------------------------------------------")
            print(f"Longest Streak for {habit_key} is {habit_data["longest_streak"]}")
            print("-----------------------------------------------------------------------------------------\n")
            return habit_data["longest_streak"]
        
        else:

            longest_streak = 0
            longestStreak_habit_name = None
            habits=self.__dict__["habits"]["habits"]
            for habit_name, habit_details in habits.items():
                if habit_details["longest_streak"] > longest_streak:
                    longest_streak = habit_details["longest_streak"]
                    longestStreak_habit_name = habit_name
            print("\n-----------------------------------------------------------------------------------------")
            print(f"Longest Streak across all habits is {longest_streak} of Habit '{longestStreak_habit_name}' !")
            print("-----------------------------------------------------------------------------------------\n")
            return (longestStreak_habit_name,longest_streak)
        
    def delete_habit(self, habit_name):
        habit_key = self.find_habit(habit_name)
        if habit_key is False:
            return
        
        try:
            habit_data = self.habits["habits"].pop(habit_key)
            self.storage.save_data(self.habits)
            print("\n-----------------------------------------------------------------------------------------")
            print(f"Habit '{habit_name}' deleted.")
            print("-----------------------------------------------------------------------------------------\n")
        except KeyError as e:
            print(f"Error deleting habit '{habit_name}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_current_streak(self, habit_name):
        """Get the current streak for a specific habit."""
        if habit_name not in self.habits["habits"]:
            raise ValueError(f"Habit {habit_name} not found.")
        
        habit_data = self.habits["habits"][habit_name]
        return habit_data["current_streak"]