from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import json

def localRequest(locale, choice):

        if((choice == 'primeiro') or (choice == 'um')):
            choice = 1
        elif((choice == 'segundo') or (choice == 'dois')):
            choice = 2
        elif((choice == 'terceiro') or (choice =='tres') or (choice == 'três')):
            choice = 3
        elif((choice == 'quarto') or (choice == 'quatro')):
            choice = 4
        elif((choice == 'quinto') or (choice == 'cinco')):
            choice = 5

        payload = {'address': locale}
        response = requests.get('http://68.183.43.29:31170/listLocales', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)

        return answer_json[int(choice) - 1]['name']

def sportsRequest(locale):
    payload = {'place': locale}

    response = requests.get('http://68.183.43.29:30000/sports', params=payload)
    answer = response.content.decode()
    answer_json = json.loads(answer)
    
    if(len(answer_json["favorable"]) > 0):
        data_sport = 'Para as condições atuais, recomendo: '
        for favorable in answer_json["favorable"]:
            data_sport += '\n' + favorable["name"].capitalize()
        return data_sport
    elif(len(answer_json["reservation"]) > 0):
        data_reservation = 'Caso queira, algumas condições favorecem: '
        for reservation in answer_json["reservation"]:
            data_reservation += '\n' + reservation["name"].capitalize()
        return data_reservation
    elif(len(answer_json["alert"]) > 0):
        data_alert = 'Poucas condições favorecem: '
        for alert in answer_json["alert"]:
            data_alert += '\n' + alert["name"].capitalize()
        return data_alert

def specifiSportRequest(locale, sport):
    payload = {'place': locale}

    response = requests.get('http://68.183.43.29:30000/sports', params=payload)
    answer = response.content.decode()
  
    answer_json = json.loads(answer)
    
    if(len(answer_json["favorable"]) > 0):
        for favorable in answer_json["favorable"]:
            if favorable["name"].capitalize() == sport.capitalize():
                return 'Sim, as condições estão favoráveis paza praticar ' + sport + ' em ' + locale + '.'
               
    elif(len(answer_json["reservation"]) > 0):
        for reservation in answer_json["reservation"]:
            if reservation["name"].capitalize() == sport.capitalize():
                return 'Algumas condições favorecem a prática de ' + sport + ' em ' + locale + '.'
        
    elif(len(answer_json["alert"]) > 0):
        for alert in answer_json["alert"]:
            if alert["name"].capitalize() == sport.capitalize():
                return 'Poucas condições favorecem a prática de ' + sport + ' em ' + locale + '.'
    
    return 'Não é recomendada a prática de ' + sport + ' em ' + locale + '. ' + sportsRequest(locale)

class Action_specific_sport(Action):
    def name(self):
        return "action_specific_sport"

    def run(self, dispatcher, tracker, domain):
        locale = tracker.get_slot('locale')
        sport = tracker.get_slot('sport')
        choice = tracker.get_slot('choice')

        location = localRequest(locale, choice)

        data_message = specifiSportRequest(location, sport)

        dispatcher.utter_message(data_message)
