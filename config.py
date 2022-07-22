import random
import string
# from OpenSSL import SSL

# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_privatekey_file('server-private-key.pem')
# context.use_certificate_file('server-public-key.pem')  

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key=''.join(random.choice(random_str) for i in range(12))
SECRET_KEY=key
DEBUG=True
# SSL_CONTEXT=context
PORT=5683
# config banco de dados