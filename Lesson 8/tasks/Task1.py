from re import findall
from collections import Counter

with open('text.txt', 'r') as file:
    mytext = file.read().lower()

reg_expression = r"[a-zA-Z]+(?<!'\w)"

results = findall(reg_expression, mytext)
print(f'The number of words in the text: {len(results)}')

word_counter = Counter(results)

common_words = word_counter.most_common(100)

counter = 0
for i in common_words:
    print(f"{counter + 1}. {i}")
    counter += 1
