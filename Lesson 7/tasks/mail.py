import smtplib
from email.message import EmailMessage
from funcs import rjson
import json

addr_from = 'mr.frog.com'
password = 'froggyfrog'
addr_to = 'mrs.frog@gmail.com'
subject = 'From frog.'
mess = json.dumps(rjson(), indent=2)


if __name__ == '__main__':
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()       
	server.starttls()
	server.ehlo()
	print(f'Logging in {addr_from} ...')
	server.login(addr_from, password)
	
	print('Creating a message ...')
	message = EmailMessage()
	message['From'] = addr_from
	message['To'] = addr_to
	message['Subject'] = subject
	message.set_content(mess)
	
	print(f'Sending message to {addr_to} ...')
	server.send_message(msg=message)
	
	print('Shutting down...')
	server.close()
