# tempMail
tempail.com terminal interface

# What is tempMail
<pre>
It's a python library to help you automatize the singup process in web applications,
it gives you a temporary e-mail(<a href="https://tempail.com/">tempail.com</a>) 
to make the singup and returns a python dict when receives an e-mail.
</pre>

# Install
```
pip install tempMail
```

# Usage
```python
import time
from tempMail import tempMail

m = tempMail.mailer()
email_address = m.getEmail()
print 'E-mail: %s' % email_address

while 1:
    result = m.mailBox()
    if result:
        print result
    time.sleep(2)
```

# Result
```
E-mail: nerdokus@norih.com
{'body': 'TempMail example file', 'Sender': 'Matheus Bernardes', 'Subject': 'Testing TempMail'}
```
