import random
import string

pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)

# print("Your random password is :", password)



#using list cpmrehension [function for i in range(n)]
password = "".join([random.choice(charValues) for i in range(pass_len)])

print("Your random password is :", password)

