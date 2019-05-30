from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from .utils import localRequest
from .environment import configSport
import requests
import random
import json

class Action_weather(Action):
    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        URL = configSport()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        if(choice == '0'):
            payload = {'local': locale}
        
            response = requests.get(URL+'/listLocales', params=payload)
            answer = response.content.decode()
            answer_json = json.loads(answer)
            buttons = []
        
            if(len(answer_json) != 1):
                data_message = 'Eu possuo vários locais com esse nome, poderia informar qual o número da localidade que deseja?\n\n'
                message = 'Clique no número do local desejado'
            counter = 6
            
            for local in answer_json:
                data_message += str(counter) + '. ' + local['name'] + '\n'
                title = (str(counter))
                payload = (str(counter))
                buttons.append({ "title": title, "payload": payload })
                counter += 1
                if counter == 11:
                    break
            dispatcher.utter_message(data_message)
            dispatcher.utter_button_message(message, buttons)

        if (choice != '0'):
            location = localRequest(locale, choice)
            payload = {'place': location}
            response = requests.get(URL+'/climate', params=payload)
            answer = response.content.decode()
            answer_json = json.loads(answer)
            data_loc = locale.capitalize()+':'
            data_temp = 'Neste local, minha temperatura é '+answer_json["temperature"]+'°C,'
            data_humidity = 'com umidade de '+str(answer_json["humidity"])+'%, '
            data_pressure = 'e pressão '+answer_json["pressure"]+' atm. '
            data_direction = 'Meus ventos sopram para '+answer_json["windyDegrees"]+','
            data_speed = ' com velocidade de '+str(answer_json["windySpeed"])+' m/s,'
            data_sky =' e apresento '+answer_json["sky"]+'.'
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
        URL = configSport()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        location = localRequest(locale, choice)
        payload = {'place': location}
		
        response = requests.get(URL+'/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
        data ='Neste local, minha temperatura é '+answer_json["temperature"]+'°C'
        data_max = 'Minha temperatura mínima no dia de hoje é de '+answer_json["temperatureMin"]+'°C'
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
        URL = configSport()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        location = localRequest(locale, choice)
        payload = {'place': location}
		
        response = requests.get(URL+'/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
        data ='Neste local, minha pressão é de '+answer_json["pressure"]+' atm'
        try:
            dispatcher.utter_message(data_loc)
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)

class Action_humidity(Action):
    def name(self):
        return "action_humidity"

    def run(self, dispatcher, tracker, domain):
        URL = configSport()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        location = localRequest(locale, choice)
        payload = {'place': location}
		
        response = requests.get(URL+'/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
        data ='Neste local, minha umidade é de '+str(answer_json["humidity"])+'%'
        try:
            dispatcher.utter_message(data_loc)
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)

class Action_sky(Action):
    def name(self):
        return "action_sky"

    def run(self, dispatcher, tracker, domain):
        URL = configSport()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        location = localRequest(locale, choice)
        payload = {'place': location}
		
        response = requests.get(URL+'/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
        data ='Neste local, apresento '+answer_json["sky"]
        try:
            dispatcher.utter_message(data_loc)
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)

class Action_wind(Action):
    def name(self):
        return "action_wind"

    def run(self, dispatcher, tracker, domain):
        URL = configSport()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        location = localRequest(locale, choice)
        payload = {'place': location}
		
        response = requests.get(URL+'/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
        data ='Neste local, meus ventos sopram para o '+answer_json["windyDegrees"]+' com velocidade de '+str(answer["windySpeed"])+'m/s.'
        try:
            dispatcher.utter_message(data_loc)
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)

class Action_sunrise_sunset(Action):
    def name(self):
        return "action_sunrise_sunset"

    def run(self, dispatcher, tracker, domain):
        URL = configSport()
        choice = tracker.get_slot('choice')
        locale = tracker.get_slot('locale')
		
        location = localRequest(locale, choice)
        payload = {'place': location}
		
        response = requests.get(URL+'/climate', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        data_loc = locale.capitalize()+':'
        data = 'Neste local, o sol me ilumina de '+answer_json["sunrise"]+' às '+answer["sunset"]+'.'
        try:
            dispatcher.utter_message(data_loc)
            dispatcher.utter_message(data)
        except ValueError:
            dispatcher.utter_message(ValueError)

