from random import choices, uniform
from time import time


class SameSexError(Exception):
    pass


class Parents:
    def __get__(self, instance, owner):
        if instance and getattr(instance, '_parents', None):
            return {
                'mother': instance.mother,
                'father': instance.father
            }

        return None

    def __set__(self, instance, value):
        if not value:
            return

        setattr(instance, '_parents', value)
        instance.mother, instance.father = value
        for parent in value:
            parent.set_child(instance)


class Person:
    _persons = []
    _adulthood = 18
    _old_age = 50

    parents = Parents()  # Дескриптор

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.birthday = time()

        self._weight = weight
        self._height = height

        self._history = {}

        self._children = []
        self.parents = ()

        self.__class__._persons.append(self)

    def __str__(self):
        name = 'Unknown'
        if getattr(self, 'name', None):
            name = self.name

        return f'{name}: {self.age} age'

    def __repr__(self):
        name = 'Unknown'
        if getattr(self, 'name', None):
            name = self.name
        return f'{self.__class__.__name__} - {name}'

    def __getitem__(self, item):
        return self.get_age(item)

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self._height < other
        elif isinstance(other, Person):
            return self._height < other._height

        return False

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self._height >= other
        elif isinstance(other, Person):
            return self._height >= other._height

        return False

    def __eq__(self, other):
        return self._height == getattr(other, '_height', other)

    def __add__(self, other):
        if type(self) is type(other):
            raise SameSexError('Child can be born by the same sex persons')

        func = getattr(self, 'give_birth', None)
        if func:
            return func(other)

        return other.give_birth(self)

    def __hash__(self):
        name = 'Unknown'
        if getattr(self, 'name', None):
            name = self.name
        return hash(f'{name}{self.birthday}')

    def _increase_weight(self):
        if self.age <= self._adulthood:
            self._weight += self._weight * 0.18

    def _increase_height(self):
        if self.age <= self._adulthood:
            self._height += self._height * 0.09
        elif self.age > self._old_age:
            self._height -= self._height * 0.001

    @property
    def weight(self):
        return round(self._weight, 2)

    @weight.setter
    def weight(self, weight):
        self._weight = round(weight, 2)

    @property
    def height(self):
        return round(self._height, 2)

    @weight.setter
    def weight(self, weight):
        self._weight = round(weight, 2)

    def celebrate_hb(self):
        self._history.update(
            {
                self.age: {
                    'weight': self._weight,
                    'height': self._height
                }
            }
        )
        self.age += 1
        self._increase_weight()
        self._increase_height()

    def get_age(self, age):
        if age == self.age:
            return {'weight': self.weight, 'height': self.height}

        return self._history.get(age)

    def set_child(self, child):
        self._children.append(child)

    @property
    def children(self):
        return self._children

    @classmethod
    def get_persons(cls):
        return {person: person.parents for person in cls._persons}


class NotAllowedWeight:
    def __init__(self, person_class):
        self._p_cls = person_class

    def __call__(self, *args, **kwargs):
        def get_weight(instanse):
            return 'Не скажу'

        def set_weght(instance, value):
            pass

        self._p_cls.weight = property(get_weight, set_weght)

        person = self._p_cls(*args, **kwargs)

        return person

    def __getattr__(self, item):
        return getattr(self._p_cls, item)


@NotAllowedWeight
class Woman(Person):
    _old_age = 60
    sex = 'female'

    def give_birth(self, father):
        sex = choices([type(self), type(father)])[0]

        child = sex(
            None,
            age=0,
            weight=round(uniform(3, 5), 2),
            height=round(uniform(30, 50), 2)
        )

        del child.name

        child.parents = [self, father]

        return child


class Man(Person):
    _old_age = 55
    sex = 'male'

    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)

        self.has_beard = choices([True, False])[0]

    def get_force(self):
        k = 0.1 if self.age < self._old_age else -0.05
        age_force = k * (self.age * k + self.age)

        return round(age_force + 0.01 * self._height + 0.005 * self._weight, 2)

    def celebrate_hb(self):
        force = self.get_force()
        super().celebrate_hb()
        self._history[self.age - 1].update({'force': force})


if __name__ == '__main__':
    bob = Man('Bob', 25, 75, 180)
    kate = Woman('Kate', 21, 60, 175)
    alex = Man('Alex', 18, 74, 189)

    try:
        f_child = bob + alex
    except SameSexError as err:
        print(err)
        f_child = alex + kate
    finally:
        f_child.name = 'Nichol' if f_child.sex == 'female' else 'Nick'
        print(f_child)
        print(f_child.parents)

    for i in range(20):
        f_child.celebrate_hb()

    print(f_child[18])
    print(f_child.weight)
    f_child.weight = 100
    print(f_child.weight)

    print(kate.children)

    s_child = kate + bob
    print(kate.children)
    print(alex.children)

    print(Person.get_persons())

    for i in range(10):
        kate.celebrate_hb()

    print(kate[21], kate.weight)
