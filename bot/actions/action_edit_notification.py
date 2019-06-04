from rasa_core_sdk import Action
from .environment import configSport
import requests
import json


class Action_edit_notification(Action):
    def name(self):
        return "action_edit_notification"

    def run(self, dispatcher, tracker, domain):
        URL = configSport()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        choice = tracker.get_slot('choice')
        payload = {"id": sender_id, "number": choice}
    
        response = requests.get(URL+'/deleteNotification', params = payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        try: 
            if "Notificação excluída" in answer_json:
                dispatcher.utter_message("Entendido. Mande os novos dados da seguinta forma :Quero registrar [esporte(s) desejado(s)]para\
                [dia(s) da semana] às [hora]:[minutos] no [local(is) desejado(s)]")
            else:
                dispatcher.utter_message("Não foi possível editar a notificação.")
        except ValueError:
            dispatcher.utter_message("Não foi possível editar a notificação.")