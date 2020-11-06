# random password generator
import string
import random

all = []

SpecialSym = list(string.punctuation)
digits = list(string.digits)
capital_letters = list(string.ascii_uppercase)
lower_letters = list(string.ascii_lowercase)

length = int(input('enter length of password you want to generate'))
all.extend(SpecialSym)
all.extend(digits)
all.extend(capital_letters)
all.extend(lower_letters)
random.shuffle(all)

random_pass = all[:length]
print('random passowrd is: ',''.join(random_pass))