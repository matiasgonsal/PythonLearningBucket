import smtplib
import configparser
from email.message import EmailMessage


def gmail_sender(str_to, str_subject, str_content, propertiesFile):
    config = configparser.RawConfigParser()
    config.read(propertiesFile)
    host = config.get('GMAIL_PRODUCER', 'host')
    port = config.get('GMAIL_PRODUCER', 'port')
    account = config.get('GMAIL_PRODUCER', 'account')
    password = config.get('GMAIL_PRODUCER', 'password')

    emailMessage = EmailMessage()
    emailMessage['from'] = account
    emailMessage['to'] = str_to
    emailMessage['subject'] = str_subject
    emailMessage.set_content(str_content)
    send_email(emailMessage, host, port, account, password)


def hotmail_sender(str_to, str_subject, str_content, propertiesFile):
    config = configparser.RawConfigParser()
    config.read(propertiesFile)
    host = config.get('HOTMAIL_PRODUCER', 'host')
    port = config.get('HOTMAIL_PRODUCER', 'port')
    account = config.get('HOTMAIL_PRODUCER', 'account')
    password = config.get('HOTMAIL_PRODUCER', 'password')

    emailMessage = EmailMessage()
    emailMessage['from'] = account
    emailMessage['to'] = str_to
    emailMessage['subject'] = str_subject
    emailMessage.set_content(str_content)
    send_email(emailMessage, host, port, account, password)


def send_email(message, host, port, account, password):
    '''
    As this implementation is taking too much time to run with a list of email messages,
    we should improve it by keeping the SMTP connection opened so we don't need to login to the
    STMP server every time that we send a single message.
    '''
    try:
        with smtplib.SMTP(host=host, port=port) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(account, password)
            smtp.send_message(message)
    except smtplib.SMTPAuthenticationError:
        print("An authentication error occurred. Please review the email producer configuration and try again...")


if __name__ == "__main__":
    gmail_sender("matiasgonsal@hotmail.com", "Testing Messaging Service",
                 "Test Successful", 'EmailServiceProducer.properties')
    hotmail_sender("matiasgonsal@gmail.com", "Testing Messaging Service",
                 "Test Successful", 'EmailServiceProducer.properties')
