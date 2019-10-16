import json

with open('names.txt') as file:
    names = file.read().replace('"', '').split(',')

result = dict()

for name in names:
    complex_names = []
    for c_name in names:
        if name == c_name:
            continue
        if name in c_name:
            complex_names.append(c_name)

    if complex_names:
        result.update({name: complex_names})


with open('result.json', 'w+') as j_result:
    json.dump(result, j_result, indent=2)


with open('result.csv', 'w+') as csv_file:
    csv_file.write('name|count\n')
    for name, c_names in result.items():
        csv_file.write(f'{name}|{len(c_names)}\n')
