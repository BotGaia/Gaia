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
    elif((choice == 'terceiro') or (choice == 'tres') or (choice == 'três')):
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


def convertDay(day):

    if(day == 1):
        return ('Segunda-feira')
    elif(day == 2):
        return ('Terça-feira')
    elif(day == 3):
        return ('Quarta-feira')
    elif(day == 4):
        return ('Quinta-feira')
    elif(day == 5):
        return ('Sexta-feira')
    elif(day == 6):
        return ('Sábado')
    elif(day == 0):
        return ('Domingo')
