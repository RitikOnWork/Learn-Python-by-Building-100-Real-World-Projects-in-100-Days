# Random Pasword Generator
import math
import random
import string   
def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Ensure the password has at least one lowercase, one uppercase, one digit, and one special character
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)
    
    # Fill the rest of the password length with a mix of all character types
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_length = length - 4
    remaining_characters = ''.join(random.choices(all_characters, k=remaining_length))
    
    # Combine all characters and shuffle them
    password_list = list(lowercase + uppercase + digit + special + remaining_characters)
    random.shuffle(password_list)
    
    # Join the list to form the final password string
    password = ''.join(password_list)
    return password

# Example usage
if __name__ == "__main__":  
    password_length = 12  # You can change the length as needed
    password = generate_password(password_length)
    print(f"Generated Password: {password}")

