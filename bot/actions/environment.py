import os


def configGateway():
    URL = ''
    if (os.environ.get('ENVIRONMENT') == 'dev'):
        URL = 'http://'+os.environ.get('IP_ADDRESS')+':3002/'
    elif(os.environ.get('ENVIRONMENT') == 'homolog'):
        URL = 'https://gateway.hml.botgaia.ga/'
    elif(os.environ.get('ENVIRONMENT') == 'production'):
        URL = 'https://gateway.botgaia.ga/'

    return URL
