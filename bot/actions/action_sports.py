from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import json

class Action_sports(Action):
    def name(self):
        return "action_sports"

    def run(self, dispatcher, tracker, domain):

        locale = tracker.get_slot('locale')
        payload = {'place': locale}
        response = requests.get('http://68.183.43.29:30000/sports', params=payload)
        content = response.content.decode()
        answer = json.loads(content)
        try:
            data_sport = 'Para as condições atuais, recomendo: '
            for favorable in answer["favorable"]:
                data_sport += '\n' + favorable["name"].capitalize()
            dispatcher.utter_message(data_sport)
            data_reservation = 'Caso queira, algumas condições favorecem: '
            for reservation in answer["reservation"]:
                data_reservation += '\n' + reservation["name"].capitalize()
            dispatcher.utter_message(data_reservation)
        except ValueError:
            dispatcher.utter_message(ValueError)
        
        
