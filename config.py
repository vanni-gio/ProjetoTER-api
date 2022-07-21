import random
import string
from OpenSSL import SSL

context = SSL.Context(SSL.TLSv1_2_METHOD)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')  

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key=''.join(random.choice(random_str) for i in range(12))
SECRET_KEY=key
DEBUG=True
# config banco de dados