from rasa_core_sdk import Action
from .environment import configGateway
import requests


class Create_alert_Action(Action):
    def name(self):
        return "action_create_alert"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        dataJson = {
          "telegramId": sender_id,
        }
        response = requests.post(URL+'ciclone', data=dataJson)
        if(response.status_code == 200):
            dispatcher.utter_message('Alerta de ciclone ativado com sucesso!')
        else:
            message = 'Ocorreu um erro ao ativar '
            message += 'o alerta de ciclone'
            dispatcher.utter_message(message)
