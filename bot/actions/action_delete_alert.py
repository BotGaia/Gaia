from rasa_core_sdk import Action
from .environment import configGateway
import requests
import json


class Delete_alert_Action(Action):
    def name(self):
        return "action_delete_alert"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        payload = {"id": sender_id, "intent": 'delete'}
        response = requests.get(URL+'ciclone', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        try:
            dispatcher.utter_message(str(answer_json))
        except ValueError:
            message = 'Ocorreu um erro ao '
            message += 'desativar o alerta de ciclone'
            dispatcher.utter_message(message)
