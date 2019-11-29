from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from pony.orm import commit
from pony.orm import desc

from app import app
from models import Sheet


@app.route('/', methods=['GET'])
def index():
    sheets = Sheet.select().order_by(
        lambda sheet: desc(sheet.created_at)
    )

    return render_template(
        'index.html',
        sheets=sheets
    )


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        sheet = Sheet(title=request.form['title'])
        for note in request.form['notes'].strip().split('\n'):
            sheet.notes.create(text=note)

        commit()

        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/delete', methods=['POST'])
def delete():
    _idx = int(request.args['id'])
    Sheet[_idx].delete()
    commit()

    return redirect(url_for('index'))
