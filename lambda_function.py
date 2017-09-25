import boto3
from twilio.rest import TwilioRestClient
import json


def lambda_handler(event, context):
    account_sid = "PUT YOUR SID HERE"
    auth_token  = "PUT YOUR AUTH TOKEN HERE"
    client = TwilioRestClient(account_sid, auth_token)
    

    call = client.calls.create(url=".xml",
        to="18005551212",
        from_="18005551212",
        method="GET")