from rasa_core_sdk import Action
from .environment import configGateway
import requests
import json


class Action_edit_notification(Action):
    def name(self):
        return "action_edit_notification"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        choice = tracker.get_slot('choice')
        payload = {"id": sender_id, "number": (int(choice) - 1)}
        response = requests.get(URL+'esporte', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        try:
            if(len(answer_json) > 0):
                if "Notificação excluída" in answer_json:
                    message = 'Entendido. Mande os novos dados'
                    message += ' da seguinte forma: Quero registrar [esporte'
                    message += ' desejado] para [dia(s) da semana] às'
                    message += ' [hora] e [minutos] no [local desejado]'
                    dispatcher.utter_message(message)
                else:
                    dispatcher.utter_message("Não foi possível \
                    editar a notificação.")
            else:
                message1 = 'Você não possui notificação.'
                message1 += ' Para criar: Quero registrar'
                message1 += ' [esporte desejado] para'
                message1 += ' [dia(s) da semana] às [hora]'
                message1 += ' e [minutos] no'
                message1 += ' [local desejado]'
                dispatcher.utter_message(message1)
        except ValueError:
            dispatcher.utter_message("Não foi possível editar a notificação.")
