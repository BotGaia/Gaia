from rasa_core_sdk import Action
from .environment import configGateway
import requests
import json


class All_cyclones_Action(Action):
    def name(self):
        return "action_all_cyclones"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        payload = {
          "intent": "allCyclones"
        }
        response = requests.get(URL + 'ciclone',params = payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        counter = 1

        if(len(answer_json) > 0):
         for cyclone in answer_json:
            data_message = str(counter) + '. ' + cyclone["name"] + '\n'
            data_message += 'Lugar de origem: ' + cyclone["originBasin"] + '\n'
            data_message += 'Ocorrência: ' + cyclone["currentBasin"] + '\n'
            data_message += 'Data de início: ' + cyclone["startDate"] + '\n'
            data_message += 'Tipo de fenômeno: ' + cyclone["stormType"] + '\n'
            data_message += 'Velocidade do vento: ' + str(cyclone["windSpeed"]) + '\n'
            dispatcher.utter_message(data_message)
            counter += 1

        else:
            message1 = 'Não houve ocorrência de '
            message2= 'ciclone nas últmas duas horas'
            dispatcher.utter_message(message1 + message2)