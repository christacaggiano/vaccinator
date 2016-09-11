import nexmo
import os

NEXMO_API_KEY = str(os.environ.get('NEXMO_API_KEY', 'fail'))
NEXMO_API_SECRET = str(os.environ.get('NEXMO_API_SECRET', 'fail'))
BOWER_PHONE_NUMBER = str(os.environ.get('BOWER_PHONE_NUMBER', 'fail'))
ARYA_PHONE_NUMBER = str(os.environ.get('ARYA_PHONE_NUMBER', 'fail'))


if __name__ == "__main__":

    client = nexmo.Client(key = NEXMO_API_KEY, secret=NEXMO_API_SECRET)
    response = client.send_message({'from': BOWER_PHONE_NUMBER, 'to': ARYA_PHONE_NUMBER, 'text': "HELLO"})
    print(response)
