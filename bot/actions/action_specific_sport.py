from rasa_core_sdk import Action
from .utils import localRequest, specificSportRequest
from .environment import configGateway
import requests
import json


class Action_specific_sport(Action):
    def name(self):
        return "action_specific_sport"

    def run(self, dispatcher, tracker, domain):
        locale = tracker.get_slot('locale')
        choice = tracker.get_slot('choice')
        sport = tracker.get_slot('sport')
        URL = configGateway()
        if(choice == '0'):
            payload = {'local': locale}

            response = requests.get(URL+'esporte', params=payload)
            answer = response.content.decode()
            answer_json = json.loads(answer)
            buttons = []

            if(len(answer_json) != 1):
                data_msg = 'Eu possuo vários locais com esse nome, '
                data_msg1 = 'poderia informar qual o número da localidade que'
                data_msg_2 = ' deseja?\n\n'
                data_message = data_msg+data_msg1+data_msg_2
                message = 'Clique no número do local desejado'
            counter = 6
            index = 0

            for local in answer_json:
                index += 1
                if (index >= 6):
                    data_message += str(counter) + '. ' + local['name'] + '\n'
                    title = (str(counter))
                    payload = (str(counter))
                    buttons.append({"title": title, "payload": payload})
                    counter += 1
            dispatcher.utter_message(data_message)
            dispatcher.utter_button_message(message, buttons)

        if (choice != '0'):
            location = localRequest(locale, choice)

            data_message = specificSportRequest(location, sport)

            dispatcher.utter_message(data_message)
