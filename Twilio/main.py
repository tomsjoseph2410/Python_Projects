import os
from twilio.rest import Client

#save the account_sid and token as environmental variables

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_AUTH']

client = Client(account_sid, auth_token)

message = client.messages.create(from_= "twilio number",body=" the message ",to='your verified number')

print(message)

