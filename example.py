import time
from tempMail import mailer

m = mailer()
email_address = m.getEmail()

print("E-mail: {}".format(email_address)

while 1:
    result=m.mailBox()
    if result:
        print(result)
    time.sleep(2)
