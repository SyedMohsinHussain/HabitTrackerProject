import pytest
from datetime import datetime, timedelta
from habit_tracker import Habit, HabitTracker

# Helper functions for test setup
def create_test_habit():
    return Habit(name="Test Habit", periodicity="daily")

def create_test_habit_tracker():
    tracker = HabitTracker()
    tracker.create_habit("Test Habit", "daily")
    return tracker

@pytest.fixture
def populated_habit_tracker():
    tracker = HabitTracker()
    tracker.create_habit("Test Habit", "daily")
    tracker.create_habit("Weekly Habit", "weekly")
    return tracker

def test_view_habits(populated_habit_tracker, capsys):
    tracker = populated_habit_tracker
    tracker.view_habits()  # Assuming this prints the habit list
    captured = capsys.readouterr()
    assert "Test Habit" in captured.out
    assert "Weekly Habit" in captured.out

def test_create_habit(populated_habit_tracker):
    tracker = populated_habit_tracker
    tracker.create_habit("Another Habit", "daily")
    assert "Another Habit" in tracker.habits

def test_delete_habit(populated_habit_tracker):
    tracker = populated_habit_tracker
    tracker.delete_habit("Test Habit")
    assert "Test Habit" not in tracker.habits

def test_create_duplicate_habit(populated_habit_tracker):
    tracker = populated_habit_tracker
    tracker.create_habit("Test Habit", "daily")  # Should ideally fail or not create a duplicate
    assert len(tracker.habits) == 2  # Assuming duplicate habits are prevented

def test_delete_non_existent_habit(populated_habit_tracker):
    tracker = populated_habit_tracker
    tracker.delete_habit("Non-existent Habit")
    # Assert the habit list is unchanged or handle the error appropriately
    assert "Non-existent Habit" not in tracker.habits

def test_mark_habit_complete(populated_habit_tracker):
    tracker = populated_habit_tracker
    habit = tracker.habits["Test Habit"]
    initial_streak = habit.streak
    tracker.mark_habit_complete("Test Habit")
    assert habit.streak == initial_streak + 1
    assert habit.last_completed == datetime.today().date()  # Assuming last_completed is updated


# Run with: pytest -v habit_tracker_tests.py