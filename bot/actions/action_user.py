from rasa_core_sdk import Action
from .utils import convertDay
from .utils import convertTimeBefore
from .environment import configSport
import requests
import json


class User_Action(Action):
    def name(self):
        return "action_user"

    def run(self, dispatcher, tracker, domain):
        URL = configSport()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        user_local = tracker.get_slot('user_locale')
        user_sport = tracker.get_slot('user_sport')
        user_day = tracker.get_slot('user_day')
        user_hour = tracker.get_slot('user_hour')
        user_minute = tracker.get_slot('user_minute')
        hours_before = tracker.get_slot('hours_before')
        minutes_before = tracker.get_slot('minutes_before')

        notificationDays = convertDay(user_day)
        hours_before = convertTimeBefore(hours_before)
        minutes_before = convertTimeBefore(minutes_before)

        dataJson = {
          "telegramId": sender_id,
          "sport": user_sport,
          "days": notificationDays,
          "hour": int(user_hour),
          "minutes": int(user_minute),
          "locals": user_local,
          "hoursBefore": hours_before,
          "minutesBefore": minutes_before,
        }


        response = requests.post(URL+'/createNotification', data=dataJson)

        if(response.status_code == 200):
            dispatcher.utter_message('Notificação salva com sucesso!')
        else:
            dispatcher.utter_message('Ocorreu um erro ao salvar')
