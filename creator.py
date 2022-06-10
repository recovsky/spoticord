import random
import string
import requests
import names

def randomName(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def randomPassword(size=14, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def randomUsername():
     return names.get_full_name()
def creator():
    s = requests.session()
    email = randomName()
    password = randomPassword()
    username = randomUsername()
    data={
        "displayname": username,
        "creation_point": "https://login.app.spotify.com?utm_source=spotify&utm_medium=desktop-win32&utm_campaign=organic",
        "birth_month": "12",
        "email": email + "@hizli.email",
        "password": password,
        "creation_flow": "desktop",
        "platform": "desktop",
        "birth_year": "1991",
        "iagree": "1",
        "key": "a2d4b979dc624757b4fb47de483f3505",
        "birth_day": "17",
        "gender": "male",
        "password_repeat": password,
        "referrer": ""
    }

    r = s.post("https://spclient.wg.spotify.com/signup/public/v1/account/",data=data)
    account = open("account.txt", "a")
    account.write(email + "@hizli.email:" + password)
    account.write("\n")
    account.close()