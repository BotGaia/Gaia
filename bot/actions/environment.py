import os


def configSport():
    URL = ''
    if (os.environ.get('ENVIRONMENT') == 'dev'):
        URL = 'http://'+os.environ.get('IP_ADDRESS')+':3000'
    elif(os.environ.get('ENVIRONMENT') == 'homolog'):
        URL = 'https://esporte.hml.botgaia.ga'
    elif(os.environ.get('ENVIRONMENT') == 'production'):
        URL = 'https://esporte.botgaia.ga'

    return URL
