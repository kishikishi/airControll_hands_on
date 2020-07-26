import tweepy
import os 
import datetime
from bluepy.btle import Peripheral, DefaultDelegate, Scanner, BTLEException, UUID
import bluepy.btle
import sys
import struct
import argparse
import requests
import time
import csv

''' twitter settings '''
CK="xxxxx"
CS="xxxxx"
AT="xxxxx"
AS="xxxxx"

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

''' about ble '''
devs = {
    'omron': {'companyID': 'd502'},
    'esp32': {'companyID': 'ffff'}
}
target = 'esp32'

Debugging = False
Verbose = True

def dataInput(*args):
    list = ['item1', 'item2']
    with open('data.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        for data in list:
	        writer.writerow(data)
    with open('data.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        for data in args:
            writer.writerow(data)

def send2ambient(dataRow):
    if companyID == 'ffff':
        (temp, humid, press) = struct.unpack('<hhh', bytes.fromhex(dataRow))
        dataInput(temp / 100, humid / 100, press / 10)

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        self.lastseq = None
        self.lasttime = datetime.fromtimestamp(0)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev or isNewData:
            for (adtype, desc, value) in dev.getScanData():
                # print(adtype, desc, value)
                if target in ('omron', 'esp32'):
                    if desc == 'Manufacturer' and value[0:4] == devs[target]['companyID']:
                        delta = datetime.now() - self.lasttime
                        if value[4:6] != self.lastseq and delta.total_seconds() > 11:
                            self.lastseq = value[4:6]
                            self.lasttime = datetime.now()
                            send2ambient(value[6:])
                            
def main():
    for status in api.home_timeline():
        txt = status.text
        if  txt =='cool':
            os.system('irsend SEND_ONCE aircon coolstart')
            api.destroy_status(status.id)
            scanner = Scanner().withDelegate(ScanDelegate())
            scanner.scan(30.0)
            break
        elif txt == 'warm':
            os.system('irsend SEND_ONCE aircon warmstart')
            api.destroy_status(status.id)
            scanner = Scanner().withDelegate(ScanDelegate())
            scanner.scan(30.0)
            break   
        elif txt == 'off':
	        os.system('irsend SEND_ONCE aircon airoff')
	        api.destroy_status(status.id)
	        break

    weekday = datetime.date.today().weekday()
    dt_now = datetime.datetime.now()
    
    '''  
    if weekday < 5:
        if dt_now.hour == 7 and dt_now.minute <= 1:
            os.system('irsend SEND_ONCE aircon warmstart')
    '''
if __name__ == "__main__":
    main()
 
