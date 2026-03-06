import random
import string

def generate_custom_password(length, use_symbols):
    # Base characters: letters and numbers
    characters = string.ascii_letters + string.digits
    
    # Add symbols only if the user says 'yes'
    if use_symbols.lower() == 'y':
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("--- 🔐 Advanced Password Generator ---")
size = int(input("Enter password length (e.g., 12): "))
symbols = input("Include symbols? (y/n): ")

result = generate_custom_password(size, symbols)
print(f"\n✅ Your custom password is: {result}")
