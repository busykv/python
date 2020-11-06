# password validator
import string


SpecialSym = list(string.punctuation)
passwd = input('enter password: ')
val = True

if len(passwd) < 6:
    print('length should be at least 6')
    val = False

if len(passwd) >8:
    print('length should be not be greater than 8')
    val = False

if not any(char.isdigit() for char in passwd):
    print('Password should have at least one numeral')
    val = False

if not any(char.isupper() for char in passwd):
    print('Password should have at least one uppercase letter')
    val = False

if not any(char.islower() for char in passwd):
    print('Password should have at least one lowercase letter')
    val = False

if not any(char in SpecialSym for char in passwd):
    print('Password should have at least one of the symbols','(',string.punctuation,')')
    val = False
if val:
    print(val)