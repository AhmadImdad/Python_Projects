import requests
import datetime
import os

NUTRITIONIX_ID = os.environ["nut_id"]
NUTRITIONIX_KEY = os.environ["nut_key"]
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_POST_ENDPOINT = "https://api.sheety.co/5b76d09a20bd625d88943bad5d69f77c/myWorkouts/workouts"
exercise_info = input("Enter details about your workout :")


workout_json = {
    "query": exercise_info,
    "weight_kg": 74,
    "height_cm": 180.0,
    "age": 21
}
workout_header = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY
}
workout_response = requests.post(url=NUTRITIONIX_ENDPOINT,
                                 json=workout_json,
                                 headers=workout_header)
workout_response.raise_for_status()
for exercises in workout_response.json()["exercises"]:
    exercise = exercises["name"].title()
    duration = str(exercises["duration_min"])
    calories = exercises["nf_calories"]
    date = datetime.datetime.now()
    today = date.strftime("%d/%m/%Y")
    today_time = date.strftime("%X")
    id = os.environ["sheety"]

    sheety_header = {
        "Authorization": id
    }
    sheety_json = {
        "workout": {
            "date": today,
            "time": today_time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    sheety_response = requests.post(url=SHEETY_POST_ENDPOINT, headers=sheety_header,
                                    json=sheety_json)
    print(sheety_response.text)
