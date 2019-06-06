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
        payload = {"id": sender_id, "number": (int(choice) - 1)}
        response = requests.get(URL+'/deleteNotification', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        try:
            if(len(answer_json) > 0):
                if "Notificação excluída" in answer_json:
                    message = 'Entendido. Mande os novos dados'
                    message1 = ' da seguinte forma: Quero registrar [esporte'
                    message2 = ' desejado] para [dia(s) da semana] às'
                    message3 = ' [hora] e [minutos] no [local(is) desejado(s)]'
                    dispatcher.utter_message(message + message1)
                    dispatcher.utter_message(message2 + message3)
                else:
                    dispatcher.utter_message("Não foi possível \
                    editar a notificação.")
            else:
                message4 = 'Você não possui notificação.'
                message5 = ' Para criar: Quero registrar'
                message6 = ' [esporte desejado] para'
                message7 = ' [dia(s) da semana] às [hora]'
                message8 = ' e [minutos] no'
                message9 = ' [local(is) desejado(s)]'
                dispatcher.utter_message(message4 + message5)
                dispatcher.utter_message(message6 + message7)
                dispatcher.utter_message(message8 + message9)
        except ValueError:
            dispatcher.utter_message("Não foi possível editar a notificação.")
