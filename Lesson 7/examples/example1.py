import smtplib
from email.message import EmailMessage

server = smtplib.SMTP()
server.connect('localhost')


if __name__ == '__main__':
    message = EmailMessage()
    message['From'] = input('Email From: ')
    message['To'] = input('Email To: ')
    message['Subject'] = input('Subject: ')
    message.set_content(input('Message: '))

    server.send_message(
        msg=message
    )
    server.close()
