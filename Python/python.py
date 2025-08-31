import random
import string

def generate_password(length=12):
    small = string.ascii_lowercase
    capital = string.ascii_uppercase
    numbers = string.digits
    special = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"

    password = [
        random.choice(small),
        random.choice(capital),
        random.choice(numbers),
        random.choice(special)
    ]

    all_chars = small + capital + numbers + special
    password += [random.choice(all_chars) for _ in range(length - 4)]

    return "".join(password)

print("Generated Password:", generate_password(12))