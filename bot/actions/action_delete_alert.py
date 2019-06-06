from rasa_core_sdk import Action
from .environment import configCyclone
import requests
import json


class Delete_alert_Action(Action):
    def name(self):
        return "action_delete_alert"

    def run(self, dispatcher, tracker, domain):
        URL = configCyclone()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        payload = {"id": sender_id}
        response = requests.get(URL+'/deleteCycloneAlert', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        try:
            dispatcher.utter_message(str(answer_json))
        except ValueError:
            message1 = 'Ocorreu um erro ao '
            message2 = 'desativar o alerta de ciclone'
            dispatcher.utter_message(message1 + message2)
