from rasa_core_sdk import Action
from .environment import configGateway
from .utils import localRequest
import requests


class User_Action(Action):
    def name(self):
        return "action_user"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
        sport = tracker.get_slot('sport')
        user_day = tracker.get_slot('user_day')
        user_hour = tracker.get_slot('user_hour')
        user_minute = tracker.get_slot('user_minute')
        hours_before = tracker.get_slot('hours_before')
        minutes_before = tracker.get_slot('minutes_before')
        location = localRequest(locale, choice)

        dataJson = {
          "telegramId": sender_id,
          "sport": sport,
          "days": user_day,
          "hour": user_hour,
          "minutes": user_minute,
          "locals": location,
          "hoursBefore": hours_before,
          "minutesBefore": minutes_before,
        }

        response = requests.post(URL+'esporte', data=dataJson)

        if(response.status_code == 200):
            dispatcher.utter_message('Notificação salva com sucesso!')
        else:
            dispatcher.utter_message('Ocorreu um erro ao salvar')
