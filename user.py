from twilio.rest import Client

from db_connection import Database_Connection

class User():

    def __init__(self, config_file):
        self.db_connection = Database_Connection(config_file)
        auth_sid, auth_token = self.db_connection.get_auth_keys()
        self.client = Client(auth_sid, auth_token)

    def get_unique_numbers(self, file_name):
        '''
        Opens txt file and goes line by line extract digits
        and formatting them to the twilio standardself.
        '''
        unique_numbers = set()
        with open(file_name) as file:
            for line in file:
                unique_number = ''.join([c for c in line if c.isdigit()])
                unique_number = '+1'+unique_number[0:10]
                unique_numbers.add(unique_number)
        return unique_numbers
