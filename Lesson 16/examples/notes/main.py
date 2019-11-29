import views
from app import app
from app import db

if __name__ == '__main__':
    dir(views)

    db.bind(**app.config['PONY'])
    db.generate_mapping(create_tables=True)

    app.run()
