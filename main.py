import random
import string

def generate_password(length):
    # Combine letters, numbers, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters based on the length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Ask user for length
print("--- Password Generator ---")
size = int(input("Enter password length: "))
print(f"Your new password is: {generate_password(size)}")
