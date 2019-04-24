from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import json


class Action_weather(Action):
    def name(self)
        return "action_temperature"

    def run(self, dispatcher, tracker, domain):

        locale = tracker.get_slot('locale')
        payload = {'place': locale}
        response = requests.get(
            'http://68.183.43.29:30000/request', params=payload)
        answer = response.json()
        data ='Neste local, meu estado é '+answer["sky"]
        try:
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)

class Action_temperature(Action):
    def name(self):
        return "action_temperature"

    def run(self, dispatcher, tracker, domain):
        locale = tracker.get_slot('locale')
        payload = {'place': locale}
        response = requests.get(
            'http://68.183.43.29:30000/request', params=payload)
        answer = response.json()
        data ='Neste local, minha temperatura é '+answer["temperature"]+'°C'
        try:
            dispatcher.utter_message(data_temp)
            dispatcher.utter_message(data_min)
            dispatcher.utter_message(data_max)
        except ValueError:
            dispatcher.utter_message(ValueError)
