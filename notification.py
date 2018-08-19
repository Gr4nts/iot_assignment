#!/usr/bin/env python3
from sense_hat import SenseHat
import requests
import json
import os

ACCESS_TOKEN="o.6sbKQW77lMj9a9ezmLSzbyhuqgbG7htV"

sense = SenseHat()
temp = sense.get_temperature()

def send_notification_via_pushbullet(title):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title}

    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(d$
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

def getSenseHatData():
    sense = SenseHat()
    temp = sense.get_temperature()

    if temp is not None:
        temp = round(temp, 1)

def main():
   getSenseHatData()
   if temp <= 20:
        send_notification_via_pushbullet("Time to put on a sweater bro!")
   else:
        send_notification_via_pushbullet("Its a nice day today")
main()