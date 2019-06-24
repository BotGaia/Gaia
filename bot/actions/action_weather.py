from rasa_core_sdk import Action
from .utils import localRequest
from .environment import configGateway
import requests
import json


class Action_weather(Action):
    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')

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
            payload = {'place': location, 'intent': 'climate'}
            response = requests.get(URL+'esporte', params=payload)
            answer = response.content.decode()
            answer_json = json.loads(answer)
            data_loc = location.title()+':'
            temp = answer_json["temperature"]
            windDegrees = answer_json["windyDegrees"]
            windSpd = str(answer_json["windySpeed"])
            humidity = str(answer_json["humidity"])
            data_temp = 'Neste local, minha temperatura é '+temp+'°C,'
            data_humidity = 'com umidade de '+humidity+'%, '
            data_pressure = 'e pressão '+answer_json["pressure"]+' atm. '
            data_direction = 'Meus ventos sopram para '+windDegrees+','
            data_speed = ' com velocidade de '+windSpd+' m/s,'
            data_sky = ' e apresento '+answer_json["sky"]+'.'
            data_sunrise = 'O sol me ilumina de '+answer_json["sunrise"]
            data_sunset = 'às '+answer_json["sunset"]+'.'
            try:
                dispatcher.utter_message(data_loc)
                dispatcher.utter_message(data_temp)
                dispatcher.utter_message(data_humidity)
                dispatcher.utter_message(data_pressure)
                dispatcher.utter_message(data_direction)
                dispatcher.utter_message(data_speed)
                dispatcher.utter_message(data_sky)
                dispatcher.utter_message(data_sunrise)
                dispatcher.utter_message(data_sunset)
            except ValueError:
                dispatcher.utter_message(ValueError)


class Action_temperature(Action):
    def name(self):
        return "action_temperature"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')

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
            payload = {'place': location, 'intent': 'climate'}

            response = requests.get(URL+'esporte', params=payload)
            answer = response.content.decode()
            answer_json = json.loads(answer)
            data_loc = location.title()+':'
            temp = answer_json["temperature"]
            data = 'Neste local, minha temperatura é '+temp+'°C'
            tempMn = answer_json["temperatureMin"]
            data_max = 'Minha temperatura mínima no dia de hoje é de '
            data_max += tempMn+'°C'
            data_min = 'E máxima de '+answer_json["temperatureMax"]+'°C.'
            try:
                dispatcher.utter_message(data_loc)
                dispatcher.utter_message(data)
                dispatcher.utter_message(data_max)
                dispatcher.utter_message(data_min)
            except ValueError:
                dispatcher.utter_message(ValueError)


class Action_pressure(Action):
    def name(self):
        return "action_pressure"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')

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
            payload = {'place': location, 'intent': 'climate'}

            response = requests.get(URL+'esporte', params=payload)
            answer = response.content.decode()
            answer_json = json.loads(answer)
            data_loc = location.title()+':'
            pressure = answer_json["pressure"]
            data = 'Neste local, minha pressão é de '+pressure+' atm'
            try:
                dispatcher.utter_message(data_loc)
                dispatcher.utter_message(data)
            except ValueError:
                dispatcher.utter_message(ValueError)


class Action_humidity(Action):
    def name(self):
        return "action_humidity"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
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
            payload = {'place': location, 'intent': 'climate'}

            response = requests.get(URL+'esporte', params=payload)
            answer = response.content.decode()
            answer_json = json.loads(answer)
            data_loc = location.title()+':'
            humidity = str(answer_json["humidity"])
            data = 'Neste local, minha umidade é de '+humidity+'%'
            try:
                dispatcher.utter_message(data_loc)
                dispatcher.utter_message(data)
            except ValueError:
                dispatcher.utter_message(ValueError)


class Action_sky(Action):
    def name(self):
        return "action_sky"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
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
            payload = {'place': location, 'intent': 'climate'}

            response = requests.get(URL+'esporte', params=payload)
            answer = response.content.decode()
            answer_json = json.loads(answer)
            data_loc = location.title()+':'
            data = 'Neste local, apresento '+answer_json["sky"]
            try:
                dispatcher.utter_message(data_loc)
                dispatcher.utter_message(data)
            except ValueError:
                dispatcher.utter_message(ValueError)


class Action_wind(Action):
    def name(self):
        return "action_wind"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
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
            payload = {'place': location, 'intent': 'climate'}

            response = requests.get(URL+'esporte', params=payload)
            answer = response.content.decode()
            answer_json = json.loads(answer)
            data_loc = location.title()+':'
            windD = answer_json["windyDegrees"]
            windS = str(answer_json["windySpeed"])
            data_answer = 'Neste local, meus ventos sopram para o '
            data = data_answer+windD+' com velocidade de '+windS+'m/s.'
            try:
                dispatcher.utter_message(data_loc)
                dispatcher.utter_message(data)
            except ValueError:
                dispatcher.utter_message(ValueError)


class Action_sunrise_sunset(Action):
    def name(self):
        return "action_sunrise_sunset"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
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
            payload = {'place': location, 'intent': 'climate'}

            response = requests.get(URL+'esporte', params=payload)
            answer = response.content.decode()
            answer_json = json.loads(answer)
            data_loc = location.title()+':'
            sunrise = str(answer_json["sunrise"])
            sunset = str(answer_json["sunset"])
            data = 'Neste local, o sol me ilumina de '+sunrise
            data += ' às '+sunset+'.'
            try:
                dispatcher.utter_message(data_loc)
                dispatcher.utter_message(data)
            except ValueError:
                dispatcher.utter_message(ValueError)
