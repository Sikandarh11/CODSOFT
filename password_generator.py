import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.ascii_letters
s4 = string.hexdigits
s5 = string.punctuation

#print(s1,"/n",s2, s3 , s4)

s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
s.extend(s5)
len = int(input("enter the length of the password : "))
random.shuffle(s)
print("".join(s[0:len]))
