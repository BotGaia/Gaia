from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random

class Action_search_locale(Action):
   def name(self):
      return "action_search_locale"

   def run(self, dispatcher, tracker, domain):
    #  locale = tracker.get_slot('locale')
    #  payload = {'place':'locale'}
    #  response = requests.get(http://68.183.43.29:30000/request?place=brasilia)
        try:
          dispatcher.utter_message('fon')
        except ValueError:
          dispatcher.utter_message(ValueError)

