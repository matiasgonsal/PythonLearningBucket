'''
This function reads a Json promotions file to send each email with the information fetched.
'''
import json
from emailmessaging.EmailService import gmail_sender

propertiesFile = './emailmessaging/EmailServiceProducer.properties'

with open('promotions.json') as json_file:
    promotions_json = json.load(json_file)
    for message in promotions_json.get('promotionsMessages'):
        gmail_sender(message.get('to'), message.get('subject'), message.get('message'), propertiesFile)
    print('All promotional messages sent!!!')
