import pandas as pd
from lxml import etree
from tqdm import tqdm
from datetime import datetime

def parse_workout(elem):
    """Parses a workout element into a dict."""
    workout_data = {
        "workoutActivityType": elem.get("workoutActivityType"),
        "duration": float(elem.get("duration")),
        "durationUnit": elem.get("durationUnit"),
        "caloriesBurned": 0,  # Default value
        "startDate": elem.get("startDate"),
        "endDate": elem.get("endDate"),
        "sourceName": elem.get("sourceName")
    }
    for child in elem:
        if child.tag == "WorkoutStatistics" and child.get("type") == "HKQuantityTypeIdentifierActiveEnergyBurned":
            workout_data["caloriesBurned"] = float(child.get("sum"))
    return workout_data

def parse_exercise_time(elem):
    """Parses an exercise time record into a dict."""
    return {
        "startDate": elem.get("startDate"),
        "endDate": elem.get("endDate"),
        "exerciseTime": float(elem.get("value")),  # Exercise time in minutes
        "unit": elem.get("unit")
    }

def parse_sleep_record(elem):
    """Parses a sleep analysis record into a dict."""
    sleep_data = {
        "sourceName": elem.get("sourceName"),
        "startDate": elem.get("startDate"),
        "endDate": elem.get("endDate"),
        "value": elem.get("value"),  # Indicates InBed or Asleep
    }
    for child in elem:
        if child.tag == "MetadataEntry":
            sleep_data[child.get("key")] = child.get("value")
    return sleep_data

def xml_to_csv(xml_file_path):
    tree = etree.parse(xml_file_path)
    root = tree.getroot()

    # Process workouts
    workouts = [parse_workout(workout) for workout in tqdm(root.findall('.//Workout'), desc="Extracting Workouts")]
    workouts_df = pd.DataFrame(workouts)
    workouts_df["startDate"] = pd.to_datetime(workouts_df["startDate"])
    workouts_df["endDate"] = pd.to_datetime(workouts_df["endDate"])
    workouts_df["date"] = workouts_df["startDate"].dt.date

    # Process exercise time
    exercise_times = [parse_exercise_time(record) for record in tqdm(root.findall('.//Record[@type="HKQuantityTypeIdentifierAppleExerciseTime"]'), desc="Extracting Exercise Time")]
    exercise_time_df = pd.DataFrame(exercise_times)
    exercise_time_df["startDate"] = pd.to_datetime(exercise_time_df["startDate"])
    exercise_time_df["endDate"] = pd.to_datetime(exercise_time_df["endDate"])
    exercise_time_df["date"] = exercise_time_df["startDate"].dt.date

    # Process sleep data
    sleep_records = [parse_sleep_record(record) for record in tqdm(root.findall('.//Record[@type="HKCategoryTypeIdentifierSleepAnalysis"]'), desc="Extracting Sleep Data")]
    sleep_df = pd.DataFrame(sleep_records)
    sleep_df["startDate"] = pd.to_datetime(sleep_df["startDate"])
    sleep_df["endDate"] = pd.to_datetime(sleep_df["endDate"])
    sleep_df["date"] = sleep_df["startDate"].dt.date

    # Save to CSVs
    workouts_csv_path = xml_file_path.replace('.xml', '_workouts.csv')
    exercise_time_csv_path = xml_file_path.replace('.xml', '_exercise_time.csv')
    sleep_csv_path = xml_file_path.replace('.xml', '_sleep.csv')

    workouts_df.to_csv(workouts_csv_path, index=False)
    exercise_time_df.groupby("date")["exerciseTime"].sum().reset_index(name="totalExerciseTime").to_csv(exercise_time_csv_path, index=False)
    sleep_df.to_csv(sleep_csv_path, index=False)
    
    print(f"Workouts data saved to {workouts_csv_path}")
    print(f"Exercise time data saved to {exercise_time_csv_path}")
    print(f"Sleep data saved to {sleep_csv_path}")

# Example usage
xml_file_path = 'export.xml'
xml_to_csv(xml_file_path)
