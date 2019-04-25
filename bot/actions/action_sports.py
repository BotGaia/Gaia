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
        try:
            data_sport = 'Para as condições atuais, recomendo: '
            for favorable in answer["favorable"]:
                data_sport += '\n' + favorable["name"]
            dispatcher.utter_message(data_sport)
        except ValueError:
            dispatcher.utter_message(ValueError)
