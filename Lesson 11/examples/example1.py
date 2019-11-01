try:
    print('Ошибки ещё нет')
    a = 1 / 0
    print('Я не вывебудсь')
except:
    print('На ноль делить нельзя. Наверное')

print('=' * 100)

try:
    a = 1 / 0
except ZeroDivisionError as err:
    print('Ловим только нужные ошибки')
    print(err)


print('=' * 100)
d = {1: 1}

print('Лучше попросить прощение, чем спросить')
try:
    d.append((2, 2))
except AttributeError:
    d.update({2: 2})

print('=' * 100)

try:
    a = 1
except (ZeroDivisionError, ValueError, FileNotFoundError):
    print('Я буду здесь, если встречу ошибку')
else:
    print('Я буду здесь, если не встречу ошибку')
finally:
    print('Я буду здесь всегда')
