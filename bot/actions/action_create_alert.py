from rasa_core_sdk import Action
from .environment import configCyclone
import requests


class Create_alert_Action(Action):
    def name(self):
        return "action_create_alert"

    def run(self, dispatcher, tracker, domain):
        URL = configCyclone()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']

        dataJson = {
          "telegramId": sender_id,
        }

        response = requests.post(URL+'/createCycloneAlert', data=dataJson)

        if(response.status_code == 200):
            dispatcher.utter_message('Alerta de ciclone ativado com sucesso!')
        else:
            dispatcher.utter_message('Ocorreu um erro ao ativar o alerta de ciclone')
