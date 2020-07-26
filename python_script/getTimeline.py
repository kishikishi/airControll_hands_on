import tweepy
import os 
import datetime
import sys
import struct
import argparse
import requests
import time
import csv

''' twitter settings '''
''' 発行されたコードを記入 '''
CK="xxxxx"
CS="xxxxx"
AT="xxxxx"
AS="xxxxx"

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

'''ツイート内容に応じて信号送信 '''                            
def watchTweet():
    for status in api.home_timeline(): #status:タイムラインの情報
        txt = status.text　#statusのうち、tweetを取得
        if  txt =='cool':
            os.system('irsend SEND_ONCE aircon coolstart') #shell commandを実行
            api.destroy_status(status.id) #tweetを削除
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

		
'''スケジュール予約'''
def dailyEvent
    weekday = datetime.date.today().weekday()
    dt_now = datetime.datetime.now()
    
    '''  
    if weekday < 5:
        if dt_now.hour == 7 and dt_now.minute <= 1:
            os.system('irsend SEND_ONCE aircon warmstart')
    '''
if __name__ == "__main__":
    watchTweet()
 
