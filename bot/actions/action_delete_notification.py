from rasa_core_sdk import Action
from .environment import configSport
import requests
import json


class Action_delete_notification(Action):
    def name(self):
        return "action_delete_notification"

    def run(self, dispatcher, tracker, domain):
        URL = configSport()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        choice = tracker.get_slot('choice')
        payload = {"id": sender_id, "number": (int(choice) - 1)}
        response = requests.get(URL+'/deleteNotification', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        try:
            dispatcher.utter_message(str(answer_json))
        except ValueError:
            dispatcher.utter_message("Não foi possível deletar \
            a notificação.")
