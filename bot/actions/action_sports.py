from rasa_core_sdk import Action
from .utils import localRequest
from .environment import configGateway
import requests
import json


class Action_sports(Action):
    def name(self):
        return "action_sports"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        locale = tracker.get_slot('locale')
        choice = tracker.get_slot('choice')
        if(choice == '0'):
            payload = {'local': locale}

            response = requests.get(URL+'esporte', params=payload)
            answer = response.content.decode()
            answer_json = json.loads(answer)
            buttons = []

            if(len(answer_json) != 1):
                data_msg = 'Eu possuo vários locais com esse nome, '
                data_msg1 = 'poderia informar qual o número da localidade que'
                data_msg_2 = 'deseja?\n\n'
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
            payload = {'place': location, 'intent': 'sports'}
            response = requests.get(URL+'esporte', params=payload)
            content = response.content.decode()
            answer = json.loads(content)
            data_loc = location.capitalize()+':'
            try:
                dispatcher.utter_message(data_loc)
                if(len(answer["favorable"]) > 0):
                    data_sport = 'Para as condições atuais, recomendo: '
                    for favorable in answer["favorable"]:
                        data_sport += '\n' + favorable["name"].capitalize()
                    dispatcher.utter_message(data_sport)
                elif(len(answer["reservation"]) > 0):
                    data_reservation = 'Caso queira, algumas condições favorecem: '
                    for reservation in answer["reservation"]:
                        data_reservation += '\n' + reservation["name"].capitalize()
                    dispatcher.utter_message(data_reservation)
                elif(len(answer["alert"]) > 0):
                    data_alert = 'Poucas condições favorecem: '
                    for alert in answer["alert"]:
                        data_alert += '\n' + alert["name"].capitalize()
                    dispatcher.utter_message(data_alert)
            except ValueError:
                dispatcher.utter_message(ValueError)
