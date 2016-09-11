import nexmo
from .secrets import *

def send_text(number, message):
    client = nexmo.Client(key = NEXMO_API_KEY, secret=NEXMO_API_SECRET)
    response = client.send_message({'from':BOWER_PHONE_NUMBER, 'to': number, 'text':message})
    response = response['messages'][0]
    print(response)
    if response['status'] == '0':
        return (True, "")
    else:
        return (False, response['error-text'])

if __name__ == "__main__":
    print(send_text("13108809283", "HEY"))
