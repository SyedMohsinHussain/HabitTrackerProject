from habit_tracker import HabitTracker
from datetime import datetime
import os

def clear_terminal():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def print_menu():
    """Print the menu for the Habit Tracker application."""
    print("\n--- Habit Tracker Menu ---")
    print("1. Add a new habit")
    print("2. Mark a habit as completed")
    print("3. View Habits")
    print("4. View longest streak of a habit")
    print("5. View longest streak across all habits")
    print("6. View Daily habits")
    print("7. View weekly habits")
    print("8. Delete a habit")
    print("0. Exit")

def main():
    habitTracker = HabitTracker()
    
    while True:
        
        print_menu()
        user_input = int(input("Enter an option: "))

        if user_input == 1:
            name = input("Enter habit name: ")
            periodicity = input("Enter periodicity (daily/weekly): ")
            habitTracker.add_habit(name, periodicity)
            clear_terminal()
        elif user_input == 2:
            name = input("Enter habit name to complete: ")
            flag = habitTracker.view_habit(name)
            if flag:
                confirmation = input("Are you sure [y/n]: ")
                if confirmation.lower() == "y":
                    habitTracker.complete_habit(name)
                    habitTracker.view_habit(name)
                else:
                    print("Habit completion cancelled.")
            
        elif user_input == 3:
            print("\nYour Habits:")
            habitTracker.view_all_habits()
        
        elif user_input == 4:
            name = input("Enter habit name to view longest streak: ")
            habitTracker.view_longest_streak(name) # TODO
        
        elif user_input == 5:
            habitTracker.view_longest_streak()
        
        elif user_input == 6:
            print("\nYour Daily Habits:")
            habitTracker.view_all_periodicity_habits("daily")
        
        elif user_input == 7:
            print("\nYour Weekly Habits:")
            habitTracker.view_all_periodicity_habits("weekly")
        
        elif user_input == 8:
            name = input("Enter habit name to delete: ")
            habitTracker.delete_habit(name)

        elif user_input == 0:
            print("Exiting the Habit Tracker...")
            break
        
        else:
            print("Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    main()