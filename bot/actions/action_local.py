from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from .utils import sportsRequest, specificSportRequest, weatherRequest
from .environment import configGateway
import requests
import json


class Action_local(Action):
    def name(self):
        return "action_local"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        intent = tracker.latest_message['intent'].get('name')
        locale = tracker.get_slot('locale')
        sport = tracker.get_slot('sport')
        type_ = tracker.get_slot('type')

        payload = {'local': locale}

        response = requests.get(URL+'esporte', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)

        buttons = []

        if(len(answer_json) != 1):
            data_message_1 = 'Eu possuo vários locais com esse nome, '
            data_message_2 = 'poderia informar qual o número '
            data_message_3 = 'da localidade que deseja?\n\n'
            data_message = data_message_1 + data_message_2 + data_message_3
            message = 'Clique no número do local desejado'
            counter = 1

            if (len(answer_json) > 5):
                data_message += '0. ' + 'Exibir mais opções' + '\n'
                title = 0
                payload = 0
                buttons.append({"title": title, "payload": payload})
            for local in answer_json:
                data_message += str(counter) + '. ' + local["name"] + '\n'
                title = (str(counter))
                payload = (str(counter))
                buttons.append({"title": title, "payload": payload})
                counter += 1
                if counter == 6:
                    break

        else:
            if(answer_json[0]['name'] == 'error'):
                data_msg_1 = 'Desculpe-me, mas não me recordo de ter criado'
                data_msg_2 = ' esse lugar. Talvez me informou erroneamente?'
                data_message = data_msg_1 + data_msg_2

            else:
                if(intent == 'sports'):
                    data_message = sportsRequest(locale)
                elif(intent == 'specific_sport'):
                    data_message = specificSportRequest(locale, sport)
                else:
                    data_message = weatherRequest(type_, locale)

        try:
            if(data_message[:1] != '{'):
                dispatcher.utter_message(data_message)
                dispatcher.utter_button_message(message, buttons)

            else:
                dataMsgJson = json.loads(data_message)
                ans = 'Neste local, minha temperatura é '
                humidity = str(dataMsgJson["humidity"])
                pressure = dataMsgJson["pressure"]
                windD = dataMsgJson["windyDegrees"]
                windS = str(dataMsgJson["windySpeed"])
                sky = dataMsgJson["sky"]
                sun = dataMsgJson["sunrise"]
                dispatcher.utter_message(locale.capitalize() + ':')
                dispatcher.utter_message(ans+dataMsgJson["temperature"]+'°C,')
                dispatcher.utter_message('com umidade de '+humidity+'%, ')
                dispatcher.utter_message('e pressão '+pressure+' atm. ')
                dispatcher.utter_message('Meus ventos sopram para '+windD+',')
                dispatcher.utter_message(' com velocidade de '+windS+' m/s,')
                dispatcher.utter_message(' e apresento '+sky+'.')
                dispatcher.utter_message('O sol me ilumina de '+sun)
                dispatcher.utter_message('às '+dataMsgJson["sunset"] + '.')

        except ValueError:
            dispatcher.utter_message(ValueError)

        return [SlotSet('type', None)]
