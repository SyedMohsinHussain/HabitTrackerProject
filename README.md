# Habit Tracker

A Python-based Habit Tracking application that helps you monitor and maintain your daily or weekly habits. The application utilizes object-oriented programming (OOP) principles for structure and includes functionalities for tracking streaks, viewing habits, and marking them as complete.

---

## Features

- **Add Habit**: Add new habits with a name and periodicity (`daily` or `weekly`).
- **Complete Habit**: Mark habits as completed, updating their streaks and ensuring consistency.
- **View Habits**: View all habits or filter by periodicity (`daily` or `weekly`).
- **Track Streaks**: Monitor the current and longest streak for each habit.
- **Habit Broken Alert**: Get notified when a habit's streak is broken.
- **Persistent Storage**: Save habit data to a JSON file for future use.
- **Delete Habit**: delete habit from JSON file.

---

## Prerequisites

Make sure you have the following installed:

- Python 3.7 or above
- `pip` (Python package manager)
- `Anaconda` **Recomended** (for creating Enviroment and managing libraries)

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `datetime` for date and time operations.
  - `JSON` for data storage and retrieval.
  - `pytest` for unit testing.
  - `Tabulate`: For displaying data in a structured table format.
  - `datetime` for date and time operations.

---

## Installation && Running the Application

1. Clone the repository amd Navigate to Project directory:
   ```bash
   git clone https://github.com/your-username/habit-tracker.git
   cd habit-tracker
   ```
2. Install dependencies:

   For Anaconda Environment

   ```bash
       conda install -c conda-forge tabulate
   ```

   For Normal Python Environment:

   ```bash
       pip install tabulate
   ```

3. Run the application:
   ```bash
   python main.py
   ```
