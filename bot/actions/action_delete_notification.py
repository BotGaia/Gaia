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
        payload = {"id": sender_id, "number": choice}
        response = requests.get(URL+'/deleteNotification', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        try:
            if "Notificação excluída" in answer_json:
                dispatcher.utter_message("Notificação excluída.")
            else:
                dispatcher.utter_message("Não foi possível deletar \
                a notificação.")
        except ValueError:
            dispatcher.utter_message("Não foi possível deletar \
            a notificação.")
