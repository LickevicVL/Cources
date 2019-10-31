from random import choices, uniform


class Person:
    persons = []
    _adulthood = 18
    _old_age = 50

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age

        self._weight = weight
        self._height = height

        self._history = {}

        self.__class__.persons.append(self)

    def __str__(self):
        name = 'Unknown'
        if getattr(self, 'name', None):
            name = self.name

        return f'{name}: {self.age} age'

    def __repr__(self):
        name = 'Unknown'
        if getattr(self, 'name', None):
            name = self.name
        return f'{self.__class__.__name__}: {self.name}'

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
        if isinstance(self, Woman):
            return self.give_birth(other)

        return other.give_birth(self)

    def _increase_weight(self):
        if self.age <= self._adulthood:
            self._weight += self._weight * 0.18

    def _increase_height(self):
        if self.age <= self._adulthood:
            self._height += self._height * 0.09
        elif self.age > self._old_age:
            self._height -= self._height * 0.001

    def weigh(self):
        return round(self._weight, 2)

    def measure(self):
        return round(self._height, 2)

    def celebrate_hb(self):
        self._history.update(
            {
                self.age: {
                    'weight': self.weigh(),
                    'height': self.measure()
                }
            }
        )
        self.age += 1
        self._increase_weight()
        self._increase_height()

    def get_age(self, age):
        if age == self.age:
            return {'weight': self.weigh(), 'height': self.measure()}

        return self._history.get(age)


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

        setattr(child, 'parents', [self, father])

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
    for i in range(10):
        bob.celebrate_hb()
        kate.celebrate_hb()
    print(bob[30])
    print(kate[30])

    first_child = bob + kate
    print(first_child)
    first_child.name = 'Nick' if first_child.sex == 'male' else 'Nichol'
    print(first_child)
    print(first_child.parents)

    for i in range(20):
        first_child.celebrate_hb()

    print(first_child[18])
    print(first_child)

    print(Person.persons)
