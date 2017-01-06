# tempMail
tempail.com terminal interface

#What is tempMail
<pre>
It's a python library to help you automatize the singup process in web applications, it gives you a temporary e-mail(<a href="https://tempail.com/"/>) to make the singup and returns a python dict when receives an e-mail.
</pre>

#Install
<pre>
git clone https://github.com/mthbernardes/tempMail.git
cd tempMail
pip install -r dependencies.txt
</pre>

#Usage
<pre>
import time
from tempMail import mailer

m = mailer()
email_address = m.getEmail()
print 'E-mail: %s' % email_address

while 1:
    result = m.mailBox()
    if result:
        print result
    time.sleep(2)
</pre>

#Result
<pre>
E-mail: nerdokus@norih.com
{'body': 'TempMail example file', 'Sender': 'Matheus Bernardes', 'Subject': 'Testing TempMail'}
</pre>