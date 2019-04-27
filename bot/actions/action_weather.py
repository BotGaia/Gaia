from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import json

def localRequest(locale, choice):
	payload = {'address': locale}

	response = requests.get('http://68.183.43.29:31170/listLocales', params=payload)
	answer = response.content.decode()
	answer_json = json.loads(answer)

	return answer_json[int(choice) - 1]['name']

class Action_weather(Action):
    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        location = localRequest(locale, choice)
        dispatcher.utter_message(location)
        payload = {'place': locale}
		
        response = requests.get(
            'http://68.183.43.29:30000/climate', params=payload)
        answer = response.json()
        data_loc = locale.capitalize()+':'
        data_temp = 'Neste local, minha temperatura é '+answer["temperature"]+'°C,'
        data_humidity = 'com umidade de '+str(answer["humidity"])+'%, '
        data_pressure = 'e pressão '+answer["pressure"]+' atm. '
        data_direction = 'Meus ventos sopram para '+answer["windyDegrees"]+','
        data_speed = ' com velocidade de '+str(answer["windySpeed"])+' m/s,'
        data_sky =' e apresento '+answer["sky"]+'.'
        data_sunrise = 'O sol me ilumina de '+answer["sunrise"] 
        data_sunset = 'às '+answer["sunset"]+'.'
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
		
		# location = localRequest(locale, choice)
        payload = {'place': locale}
		
        response = requests.get(
            'http://68.183.43.29:30000/climate', params=payload)
        answer = response.json()
        data ='Neste local, minha temperatura é '+answer["temperature"]+'°C'
        data_max = 'Minha temperatura mínima no dia de hoje é de '+answer["temperatureMin"]+'°C'
        data_min = 'E máxima de '+answer["temperatureMax"]+'°C.' 
        try:
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
		
        # location = localRequest(locale, choice)
        payload = {'place': locale}
		
        response = requests.get(
            'http://68.183.43.29:30000/climate', params=payload)
        answer = response.json()
        data ='Neste local, minha pressão é de '+answer["pressure"]+' atm'
        try:
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)

class Action_humidity(Action):
    def name(self):
        return "action_humidity"

    def run(self, dispatcher, tracker, domain):
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        # location = localRequest(locale, choice)
        payload = {'place': locale}
		
        response = requests.get(
            'http://68.183.43.29:30000/climate', params=payload)
        answer = response.json()
        data ='Neste local, minha umidade é de '+str(answer["humidity"])+'%'
        try:
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)

class Action_sky(Action):
    def name(self):
        return "action_sky"

    def run(self, dispatcher, tracker, domain):
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        # location = localRequest(locale, choice)
        payload = {'place': locale}
		
        response = requests.get(
            'http://68.183.43.29:30000/climate', params=payload)
        answer = response.json()
        data ='Neste local, apresento '+answer["sky"]
        try:
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)

class Action_wind(Action):
    def name(self):
        return "action_wind"

    def run(self, dispatcher, tracker, domain):
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        # location = localRequest(locale, choice)
        payload = {'place': locale}
		
        response = requests.get(
            'http://68.183.43.29:30000/climate', params=payload)
        answer = response.json()
        data ='Neste local, meus ventos sopram para o '+answer["windyDegrees"]+' com velocidade de '+str(answer["windySpeed"])+'m/s.'
        try:
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)

class Action_sunrise_sunset(Action):
    def name(self):
        return "action_sunrise_sunset"

    def run(self, dispatcher, tracker, domain):
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        # location = localRequest(locale, choice)
        payload = {'place': locale}
		
        response = requests.get(
            'http://68.183.43.29:30000/climate', params=payload)
        answer = response.json()
        data = 'Neste local, o sol me ilumina de '+answer["sunrise"]+' às '+answer["sunset"]+'.'
        try:
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)

