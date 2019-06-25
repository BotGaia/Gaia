from rasa_core_sdk import Action
from .environment import configGateway
import requests
import json


class All_sports_Action(Action):
    def name(self):
        return "action_all_sports"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        payload = {
          "intent": "allSports"
        }
        response = requests.get(URL + 'esporte', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        counter = 1

        if(len(answer_json) > 0):
            for sports in answer_json:
                if (counter == 15):
                    break
                data_message = str(counter) + '. ' + sports["name"] + '\n'
                dispatcher.utter_message(data_message)
                counter += 1

        else:
            message = 'Não foi possível listar os esportes.'
            dispatcher.utter_message(message)
