import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special=True, exclude_similar=True):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special = string.punctuation if include_special else ''
    
    
    all_characters = lowercase + uppercase + digits + special

    
    if exclude_similar:
        all_characters = all_characters.translate({ord(c): None for c in 'Il1O0'})

    if not all_characters:
        raise ValueError("No characters available to generate a password. Adjust your settings.")
    
    
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_digits:
        password.append(random.choice(digits))
    if include_special:
        password.append(random.choice(special))
    

    while len(password) < length:
        password.append(random.choice(all_characters))
    
    
    random.shuffle(password)
    
    return ''.join(password)


password = generate_password(length=16, include_uppercase=True, include_digits=True, include_special=True, exclude_similar=True)
print("Generated Password:", password)
