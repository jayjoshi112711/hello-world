import random
import string
l=int(input('Enter the size of the password'))
ch=string.ascii_uppercase+string.punctuation+string.digits+string.ascii_lowercase
pw=random.sample(ch,l)
a="".join(pw)
print(pw)
print(a)
