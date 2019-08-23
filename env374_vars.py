import os

# to access these variables we use the dictionary 'os.envrion'
# and the get() method to access the two keys!
db_mail = os.environ.get('EMAIL_USER')
db_email_password = os.environ.get('EMAIL_PASS')

print(db_mail)
print(db_email_password)

# see my word documentation about how to do this!
