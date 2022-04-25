import os
from datetime import datetime

import requests

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

today = datetime.now()
app_id = os.environ.get("APP_ID")
api_key = os.environ.get("API_KEY")

SHEETY_URL = os.environ.get("SHEETY_URL")

api_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_header = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}

exercise_parameters = {
    "query": input("What exercises did you do today?"),
    "gender": "male",
    "weight_kg": "75",
    "height_cm": "181",
    "age": "24"
}

response = requests.post(url = api_end_point, json = exercise_parameters, headers = nutritionix_header)
exercise_data = response.json()
print(exercise_data)

for data in exercise_data['exercises']:
    exercise_dict = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": data['name'].title(),
            "duration": data['duration_min'],
            "calories": data['nf_calories'],
        }
    }
    sheety_response = requests.post(SHEETY_URL, json = exercise_dict, auth = (USERNAME, PASSWORD))
    print(sheety_response.text)
