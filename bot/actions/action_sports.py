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
        response = requests.get(
            'https://my-json-server.typicode.com/sofiapatrocinio/sports/sports')
        content = response.content.decode()
        answer = json.loads(content)
        data_sport = 'Para as condições atuais, recomendo: '+answer["favorable"][0]["name"]+'.'
        try:
            dispatcher.utter_message(data_sport)
        except ValueError:
            dispatcher.utter_message(ValueError)