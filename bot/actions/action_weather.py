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
        data_locale = locale+'-'
        data_temp = 'Neste local, minha temperatura é '+answer["temperature"]+'°C,'
        data_humidity = 'com umidade de '+answer["humidity"]+'%, '
        data_pressure = 'e pressão '+answer["pressure"]+'atm. '
        data_direction = 'Meus ventos sopram para '+answer[windyDegrees]+','
        data_speed = ' com velocidade de '+answer[windySpeed]+'m/s'
        data_weather = 'e apresento '+answer[sky]+'.'
        data_sunrise = 'O sol me ilumina de '+answer[sunrise] 
        data_sunset = 'às '+answer[sunset]'.'
        try:
            dispatcher.utter_message(data_locale)
            dispatcher.utter_message(data_temp)
            dispatcher.utter_message(data_humidity)
            dispatcher.utter_message(data_pressure)
            dispatcher.utter_message(data_direction)
            dispatcher.utter_message(data_speed)
            dispatcher.utter_message(data_weather)
            dispatcher.utter_message(data_sunrise)
            dispatcher.utter_message(data_sunset)
        except ValueError:
            dispatcher.utter_message(ValueError)

    def name(self)
        return "action_temperature"

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
