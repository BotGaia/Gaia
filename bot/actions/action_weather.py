from rasa_core_sdk import Action
from .utils import localRequest
import requests
import json


class Action_weather(Action):
    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')

        location = localRequest(locale, choice)
        payload = {'place': location}

        response = requests.get(
            'https://clima.hml.botgaia.ga/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
        temp = answer_json["temperature"]
        windDegrees = answer_json["windyDegrees"]
        windSpd = str(answer_json["windySpeed"])
        data_temp = 'Neste local, minha temperatura é '+temp+'°C,'
        data_humidity = 'com umidade de '+str(answer_json["humidity"])+'%, '
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
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')

        location = localRequest(locale, choice)
        payload = {'place': location}

        response = requests.get(
            'https://clima.hml.botgaia.ga/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
        temp = answer_json["temperature"]
        data = 'Neste local, minha temperatura é '+temp+'°C'
        tempMn = answer_json["temperatureMin"]
        data_max = 'Minha temperatura mínima no dia de hoje é de '+tempMn+'°C'
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
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')

        location = localRequest(locale, choice)
        payload = {'place': location}

        response = requests.get(
            'https://clima.hml.botgaia.ga/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
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
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')

        location = localRequest(locale, choice)
        payload = {'place': location}

        response = requests.get(
            'https://clima.hml.botgaia.ga/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
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
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')

        location = localRequest(locale, choice)
        payload = {'place': location}

        response = requests.get(
            'https://clima.hml.botgaia.ga/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
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
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
        URL = 'https://clima.hml.botgaia.ga/climate'
        location = localRequest(locale, choice)
        payload = {'place': location}

        response = requests.get(URL, params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
        windD = answer_json["windyDegrees"]
        windS = str(answer["windySpeed"])
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
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')

        location = localRequest(locale, choice)
        payload = {'place': location}

        response = requests.get(
            'https://clima.hml.botgaia.ga/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
        sunrise = answer_json["sunrise"]
        sunset = answer["sunset"]
        data = 'Neste local, o sol me ilumina de '+sunrise+' às '+sunset+'.'
        try:
            dispatcher.utter_message(data_loc)
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)
