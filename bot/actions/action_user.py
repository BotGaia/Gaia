from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from typing import List
from .utils import convertDay
import requests
import random
import json
import os


IP_ADDRESS = os.environ.get("IP_ADDRESS", "")


class User_Action(Action):
    def name(self):
        return "action_user"

    def run(self, dispatcher, tracker, domain):
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        user_local = tracker.get_slot('user_locale')
        local_user = ', '.join(str(x) for x in user_local)
        user_sport = tracker.get_slot('user_sport')
        user_day = tracker.get_slot('user_day')
        day_user = ', '.join(str(x) for x in user_day)
        user_hour = tracker.get_slot('user_hour')
        user_minute = tracker.get_slot('user_minute')
        hours_before = tracker.get_slot('hours_before')
        minutes_before = tracker.get_slot('minutes_before')

        convertDay(day_user)

        dataJson = {
             "telegramId": sender_id,
             "sport": [user_sport],
             "days": [day_user],
             "hours": int(user_hour),
             "minutes": int(user_minute),
             "local": [local_user],
             "hoursBefore": int(hours_before),
             "minutesBefore": int(minutes_before),
             }
        dispatcher.utter_message(dataJson)

        response = requests.post("http://notifica.hml.botgaia.ga/createNotification", data = dataJson)

        if(response.status_code == 200):
            dispatcher.utter_message('Notificação salva com sucesso!')
        else:
            dispatcher.utter_message('Ocorreu um erro ao salvar sua notificação')
