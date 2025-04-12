# Import necessary libraries
import random
import string

# Function to generate a random password based on user-defined criteria
def RandomPassword():
    
    # Prompt user for their name and ensure it's not empty 
    while True:
        name = input("Enter your name: ").strip()
        if name:
            break
        else:
            print("Name cannot be empty. Please enter the name.")

    
    # Print welcome message and instructions for the user
    print(f'''\n****************************************************************************************\n
Welcome, {name} to Random Password Generator!

In this program, you can generate a secure password trailored to your needs.

Here's how it works:

-- **Specify the desired length** of your password.
-- **Choose the character types** you want to include: uppercase letters, lowercase letters, digits, and symbols.
-- **Select specific characters** if you want to include only certain ones from each type.

Let's get started with generating your custom password!

****************************************************************************************\n''')


    length=int(input('Enter the Password length:'))
    print(f'Password length is set to {length} characters.')
    print("----------------------------------------------------------------------------------------\n")
    print('You can choose from the following character types:\n')

    # Define the character sets
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    digits=string.digits
    symbol=string.punctuation

    # Choices to include in password
    choice=''

    # Make a list to store required characters to ensure at least one character from each selected type is included
    required_char=[]

    # Uppercase letters
    if input('Include uppercase letters(y/n)?').lower()=='y':
        if input("Do you want to enter specific uppercase letters (y/n)?").lower()=='y':
            user_upper=input('Enter the uppercase letters you want in password: ').strip()
            if all(char in uppercase for char in user_upper):   # check if all characters are valid
                required_char.append(random.choice(user_upper)) # pick one required
                choice+=user_upper # use only selected characters
            else:
                print('Invalid uppercase letter. Please enter only valid uppercase letters (A-Z).')
        else:
            required_char.append(random.choice(uppercase)) # pick one random uppercase letter
            choice+=uppercase # use randomly selected uppercase letters
    print("----------------------------------------------------------------------------------------\n")
    
    # Lowercase letters
    if input('Include lowercase letters(y/n)?').lower()=='y':
        if input("Do you want to enter specific lowercase letters (y/n)?").lower()=='y':
            user_lower=input('Enter the lowercase letters you want in password: ').strip()
            if all(char in lowercase for char in user_lower):   # check if all characters are valid
                required_char.append(random.choice(user_lower)) # pick one required
                choice+=user_lower # use only selected characters
            else:
                print('Invalid lowercase letter. Please enter only valid lowercase letters (a-z).')
        else:
            required_char.append(random.choice(lowercase)) # pick one random lowercase letter
            choice+=lowercase # use randomly selected lowercase letters
    print("----------------------------------------------------------------------------------------\n")

    # Digits
    if input('Include digits(y/n)?').lower()=='y':
        if input("Do you want to enter specific digits (y/n)?").lower()=='y':
            user_digit=input('Enter the digits you want in password: ').strip()
            if all(char in digits for char in user_digit):  # check if all characters are valid
                required_char.append(random.choice(user_digit)) # pick one required
                choice+=user_digit  # use only selected characters
            else:   
                print('Invalid digits. Please enter only valid digits (0-9).')
        else:
            required_char.append(random.choice(digits)) # pick one random digit
            choice+=digits # use randomly selected digits
    print("----------------------------------------------------------------------------------------\n")
                
    # Symbols
    if input('Include any symbol(y/n)?').lower()=='y':
        if input("Do you want to enter specific symbols (y/n)?").lower()=='y':
            user_symbol=input('Enter the symbols you want in password: ').strip()
            if all(char in symbol for char in user_symbol): # check if all characters are valid
                required_char.append(random.choice(user_symbol))  # pick one required
                choice+=user_symbol # use only selected characters
            else:
                print('Invalid symbols. Please enter only valid symbols (e.g., !@#$%^&*()_+).')
        else:
            required_char.append(random.choice(symbol)) # pick one random symbol
            choice+=symbol # use randomly selected symbols
    print("----------------------------------------------------------------------------------------\n")
        
    # Check if any character types were selected
    if not (choice and required_char):
        print('No character types selected.')
        print("----------------------------------------------------------------------------------------\n")
        return
    
    # Check if length is greater than the number of required characters
    if length < len(required_char):
        print(f"Password length must be at least {len(required_char)} to include all selected types.")
        print("----------------------------------------------------------------------------------------\n")
        return
    

    # Fill the remaining length with random characters from the selected character set
    remaining_length = length - len(required_char)
    
    # Randomly pick remaining characters from the choice pool
    temp = required_char + random.choices(choice,k=remaining_length)

    # Shuffle the password to ensure randomness
    random.shuffle(temp)

    # Join the list of characters to form the final password
    password="".join(temp)

    # Print the generated password
    print(f"Here's Your Generated Password: {password}\n")
    print('''****************************************************************************************
Your password has been generated successfully!
Keep it safe and secure. You can now use it with confidence.
Thank You for using the Random Password Generator!
****************************************************************************************''')


# Call the function to generate a random password
RandomPassword()