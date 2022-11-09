import string
from random import choice, randint

def login_and_password_generator():
    letters_uppers_and_digits = string.ascii_letters + string.digits
    letters_and_digits = string.ascii_lowercase + string.digits
    password = ''.join(choice(letters_uppers_and_digits) for _ in range(randint(8, 15)))
    email = ''.join(choice(letters_uppers_and_digits) for _ in range(randint(4, 6))) + '@' + \
            ''.join(choice(letters_and_digits) for _ in range(randint(4, 6))) + '.' + \
            ''.join(choice(string.ascii_lowercase) for _ in range(randint(2, 3)))
    return password, email



print(*login_and_password_generator())