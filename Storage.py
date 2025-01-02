import json

class HabitDataStore:
    def __init__(self, file_name="habits.json"):
        self.file_name = file_name

    def load_data(self):
        """Load habit data from the JSON file."""
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            with open(self.file_name, 'w') as file:
                json.dump({"habits": {}}, file, indent=4)  # Create a new JSON object if file does not exist
            return {"habits": {}}
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding the JSON data in the file {self.file_name}.")

    def save_data(self, data):
        """Save habit data to the JSON file."""
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)