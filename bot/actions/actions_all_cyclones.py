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
        response = requests.get(URL + 'ciclone', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        counter = 1

        if(len(answer_json) > 0):
            for cyclone in answer_json:
                windspd = 'Velocidade do vento: '
                origin = 'Lugar de origem: '
                ocurrency = 'Ocorrência: '
                startDate = 'Data de início: '
                stormtype = 'Tipo de fenômeno: '
                data_message = str(counter) + '. ' + cyclone["name"] + '\n'
                data_message += origin + cyclone["originBasin"] + '\n'
                data_message += ocurrency + cyclone["currentBasin"] + '\n'
                data_message += startDate + cyclone["startDate"] + '\n'
                data_message += stormtype + cyclone["stormType"] + '\n'
                data_message += windspd + str(cyclone["windSpeed"]) + '\n'
                dispatcher.utter_message(data_message)
                counter += 1

        else:
            message1 = 'Não houve ocorrência de '
            message2 = 'ciclone nas últmas duas horas'
            dispatcher.utter_message(message1 + message2)
