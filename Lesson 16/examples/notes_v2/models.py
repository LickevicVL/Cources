from datetime import datetime

from pony.orm import Required, Set

from app import db


class Sheet(db.Entity):
    title = Required(str)
    created_at = Required(
        datetime, default=datetime.now
    )
    notes = Set(lambda: Note)


class Note(db.Entity):
    text = Required(str)
    is_done = Required(bool, default=False)
    sheet = Required(Sheet)


if __name__ == '__main__':
    from app import app, db

    from pony.orm import db_session

    db.bind(**app.config['PONY'])
    db.generate_mapping(create_tables=True)

    with db_session:
        sheet = Sheet(title='MySheet2')
        sheet.notes.create(text='MyNote2.1', is_done=True)
        sheet.notes.create(text='MyNote2.2')
