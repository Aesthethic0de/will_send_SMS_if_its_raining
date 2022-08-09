from http import client
from pydoc import cli
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.environ['sid']
auth_token = os.environ['auth_token']

def mess(body):
    

    sms = Client(account_sid,auth_token)

    message = sms.messages.create(to="+919711132879",
    from_="+14052797256", body=body)

    return print("Message send successfully")