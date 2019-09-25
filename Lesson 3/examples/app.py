import ftplib
import logging
from base64 import b64decode
from io import BytesIO
from os import environ
from time import sleep, time

from pythonjsonlogger import jsonlogger

logging.basicConfig(
    level=logging.INFO
)
logger = logging.getLogger('APPLICATION')

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

ftp = ftplib.FTP()

if __name__ == '__main__':
    username = environ.get('USERNAME', 'admin')
    password = environ.get('PASSWORD', 'admin')
    host = environ.get('HOST', '0.0.0.0')
    port = int(environ.get('FTP_PORT', 2121))

    while True:
        logger.info(
            'Hi %s!',
            username,
            extra={'username': username, 'host': host, 'port': port}
        )

        ftp.connect(host, port)
        ftp.login(user=username, passwd=password)
        with open('file.txt', 'rb') as file:
            data = BytesIO(b64decode(file.read()))
            ftp.storbinary(f'STOR {int(time())}.png', data)

        ftp.close()
        logger.info('File was saved')

        sleep(10)
