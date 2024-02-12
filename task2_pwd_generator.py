import random
import string


def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    characters = ''

    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Please include at least one category of characters.")
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    print('*** PASSWORD GENERATOR ***')
    length = int(input("Enter the desired length of the password: "))

    if length >= 6:
        include_letters = input("Is password include letters? (y/n): ").lower() == 'y'
        include_numbers = input("Is password include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Is password include symbols? (y/n): ").lower() == 'y'
    else:
        print("Password length must be atleast 6. Please choose a valid length.")
        return  # Add a return statement to exit the function if length is less than 6

    password = generate_password(length, include_letters, include_numbers, include_symbols)

    if password:
        print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()
