#from twilio.rest import TwilioRestClient
# can import this differently
from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC22a849411a1ccaba37c55edaa3f6c6af"
# Your Auth Token from twilio.com/console
auth_token  = "2df9d52645d22985c7f0b5410be2312e"

#client = TwilioRestClient(account_sid, auth_token)
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+17079759427",
    from_="+1707595-9614",
    body="sup player!")

print(message.sid)
