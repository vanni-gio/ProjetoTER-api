pw = '12345'

from werkzeug.security import check_password_hash,generate_password_hash

pw_hsh = generate_password_hash(pw)
print(pw_hsh)
print(check_password_hash(pw_hsh, '12345'))