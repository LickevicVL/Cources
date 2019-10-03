import example3
from example1 import reverse
from example2 import *
from package import functions
from package.functions import say_bye as bye_func


functions.say_hello('Bob')

print(reverse([1, 2, 3]))
print(round(8.634643, 3))
print(example3.max(1, 10, -4, 42, -100))

bye_func('Bob')
