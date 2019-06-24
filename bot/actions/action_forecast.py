from rasa_core_sdk import Action
from .environment import configGateway
import requests
import json


class Forecast_Action(Action):
    def name(self):
        return "action_forecast"

    def run(self, dispatcher, tracker, domain):
        URL = configGateway()
        locale = tracker.get_slot('locale')
        time = tracker.get_slot('user_hour')
        payload = {
          "hour": time,
          "place": locale,
          "intent": "forecast"
        }
        response = requests.get(URL + 'esporte', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)

        if(len(answer_json) > 0):
            for forecast in answer_json:
                date = 'dia e Hora(mais próxima): '
                sky = 'Nebulosidade: '
                temp = 'Temperatura: '
                tempMax = 'Temperatura Máx: '
                tempMin = 'Temperatura Mín: '
                humidity = 'Umidade: '
                pressure = 'Pressão: '
                windSpeed = 'Velocidade do Vento: '
                windDegrees = 'Direção do Vento: '
                data_message = 'Previsão para ' + date + forecast["date"] + '\n'
                data_message += sky + forecast["sky"] + '\n'
                data_message += temp + forecast["temperature"] + '\n'
                data_message += tempMax + forecast["temperatureMax"] + '\n'
                data_message += tempMin + forecast["temperatureMin"] + '\n'
                data_message += pressure + forecast["pressure"] + '\n'
                data_message += humidity + forecast["humidity"] + '\n'
                data_message += windDegrees + forecast["windDegrees"] + '\n'
                data_message += windSpeed + forecast["windSpeed"] + '\n'
                dispatcher.utter_message(data_message)

        else:
            message = 'Não foi possível fazer a previsão.'
            dispatcher.utter_message(message)
