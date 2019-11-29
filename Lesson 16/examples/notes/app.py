from flask import Flask
from pony import orm
from pony.flask import Pony

from settings import Config

app = Flask('notes')
app.config.from_object(Config)

db = orm.Database()

Pony(app)
