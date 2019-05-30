from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from .environment import configSport
import requests
import json


def sportsRequest(locale):
    URL = configSport()
    payload = {'place': locale}

    response = requests.get(URL+'/sports', params=payload)
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
  


def specificSportRequest(locale, sport):
    URL = configSport()
    payload = {'place': locale}
    URL = 'https://clima.hml.botgaia.ga/sports'

    response = requests.get(URL+'/sports', params=payload)
    answer = response.content.decode()

    answer_json = json.loads(answer)

    if(len(answer_json["favorable"]) > 0):
        for favorable in answer_json["favorable"]:
            if favorable["name"].capitalize() == sport.capitalize():
                a = 'Sim, as condições estão favoráveis paza praticar '
                return a + sport + ' em ' + locale + '.'

    elif(len(answer_json["reservation"]) > 0):
        for reservation in answer_json["reservation"]:
            if reservation["name"].capitalize() == sport.capitalize():
                a = 'Algumas condições favorecem a prática de '
                return a + sport + ' em ' + locale + '.'

    elif(len(answer_json["alert"]) > 0):
        for alert in answer_json["alert"]:
            if alert["name"].capitalize() == sport.capitalize():
                a = 'Poucas condições favorecem a prática de '
                return a + sport + ' em ' + locale + '.'
    a = 'Não é recomendada a prática de '
    return a + sport + ' em ' + locale + '. ' + sportsRequest(locale)



def weatherRequest(type_, locale):
    URL = configSport()
    payload = {'place': locale}
    
    response = requests.get(URL+'/climate', params=payload)
    answer = response.content.decode()
    answer_json = json.loads(answer)

    if (type_ == 'vento'):
        sentence1 = True

    if (type_ == 'ventando'):
        sentence2 = True

    if((type_ == 'umidade')or(type_ == 'seco')or(type_ == 'úmido')):
        a = 'Neste local, minha umidade é de '
        return a + str(answer_json['humidity']) + '%'

    elif((type_ == 'ceu')or(type_ == 'chover')or(type_ == 'nebulosidade')):
        a = 'Neste local, apresento '
        return a + answer_json['sky']

    elif(sentence1 or sentence2 or(type_ == 'ventos')or(type_ == 'venta')):
        a = 'Neste local, meus ventos sopram para o '
        b = ' com velocidade de '
        c = "windyDegrees"
        return a + answer_json[c] + b + str(answer_json[c]) + 'm/s.'

    elif((type_ == 'sol')or(type_ == 'amanhece')or(type_ == 'escurece')):
        a = 'Neste local, o sol me ilumina de '
        return + answer_json['sunrise'] + ' às ' + answer_json["sunset"] + '.'

    elif((type_ == 'pressão')or(type_ == 'pressao')):
        a = 'Neste local, minha pressão é de '
        return a + answer_json['pressure'] + ' atm'

    elif((type_ == 'temperatura')or(type_ == 'temp')or(type_ == 'graus')):
        a = 'Neste local, minha temperatura é '
        return a + answer_json["temperature"] + '°C'

    else:
        return answer


def localRequest(locale, choice):
    URL = configSport()

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

    payload = {'local': locale}
    response = requests.get(URL+'/listLocales', params=payload)
    answer = response.content.decode()
    answer_json = json.loads(answer)

    return answer_json[int(choice) - 1]['name']


def convertDay(dayArray):
    answerArray = []
    
    for day in dayArray:
        if((day == 'segunda') or (day == 'segunda-feira')):
            answerArray.append(1)
        elif((day == 'terça') or (day == 'terça-feira')):
            answerArray.append(2)
        elif((day == 'quarta') or (day == 'quarta-feira')):
            answerArray.append(3)
        elif((day == 'quinta') or (day == 'quinta-feira')):
            answerArray.append(4)
        elif((day == 'sexta') or (day == 'sexta-feira')):
            answerArray.append(5)
        elif((day == 'sábado') or (day == 'sabado')):
            answerArray.append(6)
        elif(day == 'domingo'):
            answerArray.append(0)    

    return answerArray   


def convertTimeBefore(timeBefore):
    convertedTime = []
    auxTime = []
    for char in timeBefore:
        if((char == '0') or (char == '1') or (char == '2') or (char == '3')):
            auxTime.append(char)
        if((char == '4') or (char == '5') or (char == '6') or (char == '7')):
            auxTime.append(char)
        if((char == '8') or (char == '9')):
            auxTime.append(char)
    convertedTime = ''.join(auxTime)
    return int(convertedTime)
        
