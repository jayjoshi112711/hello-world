import random
import string
pw=''
l=int(input('Enter the size of the password'))
while(l>0):
    ch=string.ascii_uppercase+string.punctuation+string.digits+string.ascii_lowercase
    pw+=random.choice(ch)
    l-=1

print(pw)