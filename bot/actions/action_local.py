from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import json

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

def weatherRequest(type_, locale):
    payload = {'place': locale}
    
    response = requests.get('http://68.183.43.29:30000/climate', params=payload)
    answer = response.content.decode()
    answer_json = json.loads(answer)
    
    if((type_ == 'umidade')or(type_ == 'seco')or(type_ == 'úmido')):
        return 'Neste local, minha umidade é de ' + str(answer_json['humidity']) + '%'
    
    elif((type_ == 'ceu')or(type_ == 'chover')or(type_ == 'nebulosidade')):
        return 'Neste local, apresento ' + answer_json['sky']
    
    elif((type_ == 'vento')or(type_ == 'ventando')or(type_ == 'ventos')or(type_ == 'venta')):
        return 'Neste local, meus ventos sopram para o ' + answer_json["windyDegrees"]+ ' com velocidade de ' +str(answer_json["windySpeed"]) + 'm/s.'
    
    elif((type_ == 'sol')or(type_ == 'amanhece')or(type_ == 'escurece')):
        return 'Neste local, o sol me ilumina de ' + answer_json['sunrise'] + ' às ' + answer_json["sunset"] + '.'
    
    elif((type_ == 'pressão')or(type_ == 'pressao')):
        return 'Neste local, minha pressão é de ' + answer_json['pressure'] + ' atm'
    
    elif((type_ == 'temperatura')or(type_ == 'temp')or(type_ == 'graus')):
        return 'Neste local, minha temperatura é ' + answer_json["temperature"] + '°C'
    
    else:
        return answer


class Action_local(Action):
    def name(self):
        return "action_local"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')
        locale = tracker.get_slot('locale')
        type_ = tracker.get_slot('type')
        
        payload = {'address': locale}
        
        response = requests.get('http://68.183.43.29:31170/listLocales', params=payload)
        answer = response.content.decode()
        answer_json = json.loads(answer)
        
        if(len(answer_json) != 1):
            data_message = 'Eu possuo vários locais com esse nome, poderia informar qual o número da localidade que deseja?\n\n'
            
            counter = 1
            
            for local in answer_json:
                data_message += str(counter) + '. ' + local['name'] + '\n'
                counter += 1
                if counter == 6:
                    break
            
        else:
            if(answer_json[0]['name'] == 'error'):
                data_message = 'Desculpe-me, mas não me recordo de ter criado esse lugar. Talvez me informou erroneamente?'
                
            else:
                if(intent == 'sports'):
                    data_message = sportsRequest(locale)
                else:
                    data_message = weatherRequest(type_, locale)
                
        try:
            if(data_message[:1] != '{'):
                dispatcher.utter_message(data_message)
                
            else:
                data_message_json = json.loads(data_message)
                
                dispatcher.utter_message(locale.capitalize() + ':')
                dispatcher.utter_message('Neste local, minha temperatura é ' + data_message_json["temperature"]+'°C,')
                dispatcher.utter_message('com umidade de ' + str(data_message_json["humidity"])+'%, ')
                dispatcher.utter_message('e pressão ' + data_message_json["pressure"]+' atm. ')
                dispatcher.utter_message('Meus ventos sopram para ' + data_message_json["windyDegrees"]+',')
                dispatcher.utter_message(' com velocidade de ' + str(data_message_json["windySpeed"])+' m/s,')
                dispatcher.utter_message(' e apresento ' + data_message_json["sky"]+'.')
                dispatcher.utter_message('O sol me ilumina de ' + data_message_json["sunrise"])
                dispatcher.utter_message('às ' + data_message_json["sunset"] + '.')
            
        except ValueError:
            dispatcher.utter_message(ValueError)
    
        return [SlotSet('type', None)]