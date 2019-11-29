from uuid import uuid4

from flask import Flask
from flask import Response
from flask import render_template, redirect, url_for
from flask import request
from http import HTTPStatus

from game import Desk, Hand

app = Flask(__name__)

desks = dict()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        user = Hand(request.form['name'])
        bot = Hand()

        desk = Desk()
        desk.shuffle()
        _id = uuid4()

        desks.update({str(_id): {'user': user, 'bot': bot, 'desk': desk}})

        return redirect(url_for('game', id=_id))


@app.route('/game', methods=['GET'])
def game():
    _game = desks[request.args['id']]
    user: Hand = _game['user']
    bot: Hand = _game['bot']
    desk: Desk = _game['desk']

    for u in [user, bot] * 2:
        u.add_card(desk.get_card())

    if not user:
        return redirect(url_for('get_result', id=desks[request.args['id']]))

    return render_template('game.html', user=user, id=request.args['id'])


@app.route('/getCard', methods=['GET'])
def get_card():
    _game = desks[request.args['id']]
    user: Hand = _game['user']
    bot: Hand = _game['bot']
    desk: Desk = _game['desk']

    user.add_card(desk.get_card())
    if bot:
        bot.add_card(desk.get_card())

    if not user:
        return Response(status=HTTPStatus.FOUND)

    return render_template('cards.html', user=user)


@app.route('/result', methods=['GET'])
def get_result():
    _game = desks[request.args['id']]
    user: Hand = _game['user']
    bot: Hand = _game['bot']
    desk: Desk = _game['desk']

    while bot:
        bot.add_card(desk.get_card())

    if user.count() > 21:
        winner = bot.name
    elif user.count() <= bot.count() <= 21:
        winner = bot.name
    else:
        winner = user.name

    desks.pop(request.args['id'])

    return render_template('result.html', user=user, bot=bot, winner=winner)


if __name__ == '__main__':
    app.run(debug=True)
