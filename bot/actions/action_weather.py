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
        payload = {'place': locale}
        response = requests.get(
            'http://68.183.43.29:30000/request', params=payload)
        answer = response.json()
        data_temp = 'Neste local, minha temperatura é '+answer["temperature"]+'°C'
        data_min = 'Mínima neste dia é de '+answer["temperatureMin"]+'ºC.'
        data_max = 'Máxima de '+answer["temperatureMax"]+'ºC.'
        try:
            dispatcher.utter_message(data_temp)
            dispatcher.utter_message(data_min)
            dispatcher.utter_message(data_max)
        except ValueError:
            dispatcher.utter_message(ValueError)
