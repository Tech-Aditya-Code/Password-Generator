import random
import string

def myPass():
    
    length = int(input("Enter length of password: "))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    symbol = string.punctuation

    combine = lower + upper + number + symbol

    # sample will always return new value
    x = random.sample(combine, length)

    # convert list into string
    password = "".join(x)

    print(password)
    
    myPass()
myPass()
