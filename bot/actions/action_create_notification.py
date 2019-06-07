from rasa_core_sdk import Action
from .environment import configGateway
import requests


class User_Action(Action):
    def name(self):
        return "action_user"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        user_local = tracker.get_slot('user_locale')
        user_sport = tracker.get_slot('user_sport')
        user_day = tracker.get_slot('user_day')
        user_hour = tracker.get_slot('user_hour')
        user_minute = tracker.get_slot('user_minute')
        hours_before = tracker.get_slot('hours_before')
        minutes_before = tracker.get_slot('minutes_before')

        dataJson = {
          "telegramId": sender_id,
          "sport": user_sport,
          "days": user_day,
          "hour": user_hour,
          "minutes": user_minute,
          "locals": user_local,
          "hoursBefore": hours_before,
          "minutesBefore": minutes_before,
        }

        response = requests.post(URL+'esporte', data=dataJson)

        if(response.status_code == 200):
            dispatcher.utter_message('Notificação salva com sucesso!')
        else:
            dispatcher.utter_message('Ocorreu um erro ao salvar')
