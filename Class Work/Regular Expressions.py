import re

#re.match
res = re.match(r'[/$@#%^&*()]','&Hello World')
print(res.group() if res else "No match")

#re.search
res = re.search(r'[6-9]','Hello World 5 8 9')
print(res.group() if res else "No match")

res = re.search(r'h.t','hit hat hot')
print(res.group() if res else "No match")

#re.findall
res = re.findall(r'h.t','hit hat hot') #print(res.group() if res else "No match")
print(res)

#findall with digits
res = re.findall(r'[0-9]','hfewnauiweaeiorheundkljfdiufeiruorhuu093u9847092385ufhifiey93t268t28u3903tu4itjfhe90r393ryu3irh373rg3th40940-i3prjo8r73r9u08y5')
#print(res.group() if res else "No match")
print(res)

#findall with lowercase letters
res = re.findall(r'[a-z]','hfewnauiweaeiorheundkljfdiufeiruorhuu093u9847092385ufhifiey93t268t28u3903tu4itjfhe90r393ryu3irh373rg3th40940-i3prjo8r73r9u08y5')
#print(res.group() if res else "No match")
print(res)

#findall with uppercase letters
res = re.finditer(r'[0-9]{2}','Hello World 76 34 90 23')
#print(res.group() if res else "No match")
for i in res:
    print(i.group(),i.start())

#re.fullmatch
res = re.fullmatch(r'[0-9]{10}','9087653546')
print(res.group() if res else "No match")

#re.split
res = re.split(r'[,:/0]','dinesh,sanjay:jashwanth/mohit0tarak')
print(res)

'''
res = re.match(r'[0-9]{2}','Hello world 76 34 90 23')#{number} is used to find number of digits

#print(res.group() if res else "No match")
for i in res:
    print(i.group(),i.match())
'''
#re.sub
text = 'Java Programming language'
res=re.sub('Java','Python',text)
res = re.sub(r'[A-Z]','*',text)

print(res)

# ?=.* #atleast one should be there

# {n} #exactly n times
text = 'Sanjay is a good boy. He lives in KPHB. Heart Hacker sanjay. Lover boy sanjay. Sanjay contact no: 9876459987' 
res = re.findall(r'\b[A-Z][a-zA-Z]*', text)
print(res)

# Validate a name
import re
def validate_name(name):
    pattern = r'^[A-Za-z]{2,40} ( [A-Za-z]{2,40})+$' 
    return bool(re.fullmatch(pattern, name))

name = 'Dasari Rushindra Reddy'
print(validate_name(name))

# Validate an email
import re
def validate_email(email):
    pattern = r'^[a-z0-9._]+@[a-z.-]+\.[a-z]{2,3}$' 
    return bool(re.fullmatch(pattern, email))

email = 'rushindra2004@gmail.com' 
print(validate_email(email))

# Validate a phone number
import re
def validate_phone_no(phone_no):
    pattern = r'^(?:\+91|0)?[6-9]\d{9}$' 
    return bool(re.fullmatch(pattern, phone_no))
phone_no = '9876543210'
print(validate_phone_no(phone_no))

# Validate a password
import re
def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*a-z])(?=.*\d)(?=.*[@$%!*?&_-])[A-Za-z\d@$!%*?&]{8,}$' 
    return bool(re.fullmatch(pattern, password))
password = 'rushindra@2004'
print(validate_password(password))

# Validate a username
import re
def validate_username(username):
    pattern = r'^[a-zA-Z0-9]{5,15}$' 
    return bool(re.fullmatch(pattern, username))
username = 'dasarirushindrareddy'
print(validate_username(username))