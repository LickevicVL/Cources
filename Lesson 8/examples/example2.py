import yaml
import re


with open('example1.yaml') as reg:
    data = yaml.load(reg, yaml.BaseLoader)
    password_pattern = data['password']
    email_pattern = data['email']
    ip_pattern = data['ip_address']
    name_pattern = data['name_group']


if __name__ == '__main__':
    res1 = re.search(password_pattern, '123PasswordAfsdf')
    print(res1)

    p2 = re.compile(email_pattern)
    print(p2.search('I need to find email: Test.email333@mail.net'))
    print(p2.fullmatch('Test.email333@mail.net'))

    res3 = re.findall(ip_pattern, '192.168.11.0')
    print(res3)

    res4 = re.match(ip_pattern, '192.168.11.0').group(1)
    print(res4)

    res5 = re.match(name_pattern, 'Bob Jablonski')
    print(res5.group('name'), res5.groups())
