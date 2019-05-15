from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from typing import List
import requests
import random
import json
import os

IP_ADDRESS = os.environ.get("IP_ADDRESS", "")


class User_Action(Action):
    def name(self):
        return "action_user"

    def run(self, dispatcher, tracker, domain):
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        user_local = tracker.get_slot('user_locale')
        local_user = ', '.join(str(x) for x in user_local)
        user_sport = tracker.get_slot('user_sport')
        sport_user = ', '.join(str(x) for x in user_sport)
        user_day = tracker.get_slot('user_day')
        day_user = ', '.join(str(x) for x in user_day)
        user_hour = tracker.get_slot('user_hour')
        hour_user = ', '.join(str(x) for x in user_hour)
        user_minute = tracker.get_slot('user_minute')
        minute_user = ', '.join(str(x) for x in user_minute)


        dispatcher.utter_message(local_user)
        dispatcher.utter_message(sport_user)
        dispatcher.utter_message(day_user)
        dispatcher.utter_message(hour_user)
        dispatcher.utter_message(minute_user)
        dataJson = {
             "telegramId": sender_id,
             "sport": [sport_user],
             "days": [day_user],
             "times": [ { hour_user, minute_user }],
             "local": [local_user]
             }
        dispatcher.utter_message(dataJson)

        response = requests.post("http://68.183.43.29:30000//createNotification", data = dataJson)
