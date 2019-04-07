import requests
import random

buffer = []

def getRandomQuote():
    if(len(buffer) == 0): # get a new set of quotes if none left in buffer
        headers = {"Authorization": 'Token token="9313a2c53feecb17a35185d0b8a1db8c"'}
        response = requests.get("https://favqs.com/api/quotes", headers=headers)
        # print(response.status_code)
        # print(response.content)
        data = response.json()
        allQuotes = data["quotes"]
        for quoteItem in allQuotes:
            # print(quoteItem["body"] + "\n")
            buffer.append(quoteItem["body"])

        # print("Num quotes back: " + str(len(allQuotes)))
        # print("Num quotes written: " + str(len(buffer)))

    return buffer.pop() # returns next quote in buffer

# test the randomquote
# for i in range(0,30):
#     print(i, getRandomQuote())

import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except Exception:
   print("Error: unable to send email")
