from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from pony.orm import commit
from pony.orm import desc

from app import app
from models import Note
from models import Sheet
from flask import Response
from http import HTTPStatus


@app.route('/', methods=['GET'])
def index():
    sheets = Sheet.select().order_by(lambda sheet: desc(sheet.date))

    return render_template('index.html', sheets=sheets)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        sheet = Sheet(title=request.form['title'])
        for note in request.form['notes'].rstrip().split('\n'):
            sheet.notes.create(text=note)

        commit()

        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/done/<int:idx>', methods=['POST'])
def make_done(idx):
    note = Note[idx]
    note.is_done = not note.is_done
    commit()

    return Response(status=HTTPStatus.ACCEPTED)
