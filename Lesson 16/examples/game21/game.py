from dataclasses import dataclass, field
from json import JSONEncoder
from random import shuffle
from typing import List

VALUES = {
    11: 'T',
    2: 'V',
    3: 'Q',
    4: 'K',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10'
}
SUITES = ['\u2660', '\u2663', '\u2666', '\u2665']


class Card:
    _special_value = 11

    def __init__(self, name, value):
        self.name = name
        self._value = value

    @property
    def value(self):
        return self._value

    def set_value(self, value):
        if self._value == self._special_value:
            self._value = value

    def __repr__(self):
        return f'{self.name}'


@dataclass
class Desk:
    cards: List[Card] = field(
        default_factory=lambda: [
            Card(f'{name}{suit}', value)
            for suit in SUITES for value, name in VALUES.items()
        ]
    )

    def shuffle(self):
        shuffle(self.cards)

    def get_card(self):
        return self.cards.pop()


class Hand:
    _bot_barrier = 17
    _user_barrier = 21

    def __init__(self, name='Bot'):
        self.name = name
        if name == 'Bot':
            self._barrier = self._bot_barrier
        else:
            self._barrier = self._user_barrier

        self.cards = list()

    def __contains__(self, item):
        names: List[Card] = [card.name[0] for card in self.cards]
        if item in names:
            return True

        return False

    def add_card(self, card):
        if 'T' in self and card.name[0] == 'T':
            card.set_value(1)

        self.cards.append(card)

    def count(self):
        return sum([card.value for card in self.cards])

    def __bool__(self):
        if self.count() >= self._barrier:
            return False

        return True

    def __str__(self):
        return f'{self.name}: {self.count()}'


class GameJsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Hand):
            return {o.name: o.cards}

        if isinstance(o, Card):
            return {'name': o.name, 'value': o.value}

        if isinstance(o, Desk):
            return o.cards
