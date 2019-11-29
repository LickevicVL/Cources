from datetime import datetime

from pony.orm import Required, Set

from app import db


class Sheet(db.Entity):
    title = Required(str)
    date = Required(datetime, default=datetime.now)
    notes = Set(lambda: Note)


class Note(db.Entity):
    text = Required(str)
    shit_id = Required(Sheet)
    is_done = Required(bool, default=False)
