from flask import Flask
from pony import orm
from pony.flask import Pony

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

Pony(app)

db = orm.Database()
