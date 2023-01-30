# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from credential import account_sid, auth_token, my_number, twilio_num, my_msg

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=my_msg,
                     from_=twilio_num,
                     to=my_number
                 )

# print(message.sid)