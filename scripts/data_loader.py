import json
import os

def load_student_database(file_path):
    """
    Simulates fetching student data from a backend database (JSON file).
    Essential for Student Information Systems (SIS).
    """
    # Check if file exists to prevent errors
    if not os.path.exists(file_path):
        print(f"Error: Database file not found at {file_path}")
        return []

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"✅ Successfully loaded {len(data)} student records.")
            return data
    except Exception as e:
        print(f"System Error: {e}")
        return []

# --- Execution ---
# Connect to the data layer created in the previous step
database_path = '../data/class_roster.json' 
students = load_student_database(database_path)

# Display loaded data for verification
for student in students:
    print(f"Loaded Profile: {student['name']} ({student['status']})")
