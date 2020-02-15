'''This Program sends a mass text to all numbers in txt file'''
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

from db_connection import Database_Connection

class Server():

    def __init__(self):
        db_connection = Database_Connection('config.ini')
        auth_sid, auth_token = db_connection.get_auth_keys()
        self.twilio_number = db_connection.get_twilio_phone_number()
        self.messaging_service_sid = db_connection.get_msg_service_id()
        self.client = Client(auth_sid, auth_token)

    def is_valid_number(self, number):
        '''check if number is a valid phone number'''
        try:
            self.client.lookups.phone_numbers(number).fetch(type="carrier")
            return True
        except:
            return False

    def send_sms(self, number):
        '''send sms message'''
        try:
            self.client.messages.create(
                to=number,
                messaging_service_sid=self.messaging_service_sid,
                body="MESSAGE"
                )
        except:
            print('bad number = '+number)

    def send_mms(self, number, img_url):
        '''send mms message'''
        try:
            self.client.messages.create(
                to=number,
                messaging_service_sid=self.messaging_service_sid,
                body="MESSAGE",
                media_url=img_url
                )
        except:
            print('bad number = '+number)
