'''
Creates a connection to the database for further use.
Currently the database is a configuration file.
'''
import configparser

class Database_Connection():

    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_twilio_phone_number(self):
        '''Returns twilio phone number from config file'''
        return self.config['DEFAULT']['TWILIO_PHONE_NUMBER']

    def get_msg_service_id(self):
        '''Returns messaging service id from config file'''
        return self.config['DEFAULT']['MESSAGING_SERVICE_SID']

    def get_auth_keys(self):
        '''Get auth keys from config file'''
        return self.config['DEFAULT']['AUTH_SID'], self.config['DEFAULT']['AUTH_TOKEN']
