import string
import random

def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(char) for _ in range(length))
    return password

length = int(input('Password Length?\n'))
print(f'Password: {generate_password(length)}\n')