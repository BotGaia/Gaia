from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import json
import os

class User_Action(Action):
    def name(self):
        return "action_user"

    def run(self, dispatcher, tracker, domain):
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        user_local = tracker.get_slot('locale')
        user_sport = tracker.get_slot('sport')
        user_day = tracker.get_slot('user_day')
        user_hour = tracker.get_slot('user_hour')
        user_minute = tracker.get.slot('user_minute')

        ip_address = os.environ['IP_ADDRESS']
        dataJson = {	
            "telegramId": sender_id,
            "sport": [user_sport],
            "days": [user_day],
            "times": [ { user_hour, user_minute }],
            "local": [user_local]
            }

        response = requests.post('http://'+ip_address+':3003/createNotification', data = dataJson)


