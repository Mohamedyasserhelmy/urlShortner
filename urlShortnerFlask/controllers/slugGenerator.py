import secrets
import string
import random

def generate_code():
    alphabet = string.ascii_letters + string.digits
    code = ''.join(random.choice(alphabet) for i in range(6))
    return code

