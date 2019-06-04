from rasa_core_sdk import Action
from .environment import configSport
import requests
import json


class Action_show_button(Action):
    def name(self):
        return "action_show_button"

    def run(self, dispatcher, tracker, domain):
        URL = configSport()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        payload = {"id": sender_id}
        message = ""
        response = requests.get(URL+'/userNotification', params = payload)
        answer = response.content.decode()
        answerJson = json.loads(answer)
        buttons = []
        json_counter = 0
        if(len(answerJson) > 0):
            while json_counter < len(answerJson):
                json_counter+=1
                title = (str(json_counter))
                payload = (str(json_counter))
                buttons.append({"title": title, "payload": payload})
        try:
            dispatcher.utter_button_message(message, buttons)
        except ValueError:
            dispatcher.utter_message(ValueError)