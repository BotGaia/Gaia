from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import json


class Action_weather(Action):
    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        locale = tracker.get_slot('locale')
        payload = {'place': 'locale'}
        response = requests.get(
            'http://68.183.43.29:30000/request', params=payload)
        answer = response.json()
        print('/n/n/n/n/n')
        print(answer)
        print('/n/n/n/n/n')
        try:
            dispatcher.utter_message(answer["sky"])
        except ValueError:
            dispatcher.utter_message(ValueError)
