# STRETCH IDEAS:
#
# Make it run through Tor
# Use a JSON file with real names
# Use a JSON file of emails
# Use a JSON file of zip codes
# JSON cities, JSON addresses...
# Let's JSON the shit out of this code!

import requests
import random
import string
import threading
import json

from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller

url = 'https://www.topdealsthisyear.com/nup2/checkout.php?affId=894BBF62&c1=d6t8v5tadf1aotkd26p4cc0q&c2=&c3=e1b74dcb6fce451fa1939733e50aae88'

# Loads in all necessary JSON files.

name_data = json.load(open('names.json','r'))
USgeo_data = json.load(open('USCities.json','r'))
USgeo_data_index = random.randrange(len(USgeo_data))


# FOR HANDLING TOR

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050', 
            'https': 'socks5://127.0.0.1:9050'}
    return session

session = get_tor_session()
print(session.get("http://httpbin.org/ip").text)

# HANDLING DATA TO POST TO SCAM SITE

ua = UserAgent()

data = {
    'User-Agent': ua,
    'product': '2782',
    'shippingFirstName': name_data[random.randrange(len(name_data))],
    'shippingLastName': name_data[random.randrange(len(name_data))],
    'email': 'qwqas@ichstet.com',
    'phone': '3945867373',
    'shippingAddress': '134',
    'shippingCity': USgeo_data[USgeo_data_index]['city'],
    'shippingState': USgeo_data[USgeo_data_index]['state'],
    'shippingZip': USgeo_data[USgeo_data_index]['zip_code'],
    'shippingCountry': 'US',
    'billingSameAsShipping': '1',
    'billingFirstName': '',
    'billingLastName': '',
    'billingAddress': '',
    'billingCity': '',
    'billingCountry': 'US',
    'billingZip': '',
    'newPaymentType': 'on',
    'creditCardNumber': '4007000000027',
    'expMonth': '01',
    'expYear': '2026',
    'CVV': '314',
}
# def do_request():
#     while True: 

data['User-Agent'] = ua.random
data['shippingFirstName'] = name_data[random.randrange(len(name_data))] 
data['shippingLastName'] = name_data[random.randrange(len(name_data))]

USgeo_data_index = random.randrange(len(USgeo_data))
data['shippingState'] = USgeo_data[USgeo_data_index]['state']
data['shippingZip'] = USgeo_data[USgeo_data_index]['zip_code']
data['shippingCity'] = USgeo_data[USgeo_data_index]['city']
print(data['User-Agent'])
print(data['shippingFirstName'] + ' ' + data['shippingLastName']) 
print(data['shippingState'])
print(data['shippingZip'])
print(data['shippingCity'])

# response = requests.post(url, data=data).text
        #print(response)
        #print(data['shippingFirstName'] + ' ' + data['shippingLastName'])
'''
threads = []
for i in range(100):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(100):
    threads[i].start()

for i in range(100):
    threads[i].join() '''
