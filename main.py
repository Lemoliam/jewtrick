from time import sleep
from termcolor import colored
import requests

while True:
    sleep(2.5)
    getData = requests.get("https://mcapi.ca/ping/players/2b2t.org").json()

    try:
        print('-------------------------------')
        print('server status: ' + str(getData['status']))
        print('players online: ' + str(getData['players']['online']))
    except KeyError:
        print(colored('error!', 'red') + ' couldn\'t receive online from server')
        continue

    if not getData['status']:
        print(colored('false:', 'red') + ' invalid status')
        continue

    if getData['status']:
        if getData['players']['online'] > 500 or getData['players']['online'] < 10:
            print(colored('false:', 'red') + ' fake online or too late')
            continue

        elif getData['players']['online'] > 10:
            print(colored('true:', 'green') + ' join')

def antiHauseFix():
    pass
    #todo: make a fake-online detector
