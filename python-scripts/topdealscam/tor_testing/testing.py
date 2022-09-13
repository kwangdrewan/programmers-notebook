import requests
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
from pprint import pprint
import json
import os

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050', 
            'https': 'socks5://127.0.0.1:9050'}

    return session

def new_tor_id():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="password")
        controller.signal(Signal.NEWNYM)

 
# session = requests.session()
# session.proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
# session.params = {'q':'toronto', 'key':os.environ['WEATHER_API'], 'days': '1'}

session = get_tor_session()
print(session.get("http://httpbin.org/ip").text)

new_tor_id()
#session = get_tor_session()
#print(session.get("http://httpbin.org/ip").text)
