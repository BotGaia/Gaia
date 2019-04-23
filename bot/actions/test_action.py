from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import json 

class Action_test(Action):
   def name(self):
      return "action_test"

   def run(self, dispatcher, tracker, domain):
      locale = tracker.get_slot('locale')
      payload = {'place':'locale'}
      response = requests.get(http://68.183.43.29:30000/request, params=payload)
      answer = json.loads(response)
        try:
          dispatcher.utter_message(answer["sky"])
        except ValueError:
          dispatcher.utter_message(ValueError)

