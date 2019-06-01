from rasa_core_sdk import Action
from .utils import convertDay
from .utils import convertTimeBefore
from .environment import configSport
import requests


class User_Action(Action):
    def name(self):
        return "action_show_notification"

    def run(self, dispatcher, tracker, domain):
        URL = configSport()
        tracker_state = tracker.current_state()
        sender_id = tracker_state['sender_id']
        payload = {"id": sender_id}
    
        response = requests.get(URL+'/userNotification', params = payload)
        answer = response.content.decode()
        answerJson = json.loads(answer)

        try: 
            dispatcher.utter_message(answerJson)
        except ValueError:
            dispatcher.utter_message("Não foi possível exibir suas notificações")
