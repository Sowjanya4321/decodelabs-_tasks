import random
import string

saved_passwords = []

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


while True:

    print("\n========== PASSWORD GENERATOR ==========")
    print("1. Generate Password")
    print("2. View Saved Passwords")
    print("3. Save Passwords To File")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        try:

            length = int(input("Enter password length: "))

            if length < 4:
                print("Password length should be at least 4")
                continue

            upper = input("Include Uppercase? (y/n): ").lower() == "y"
            lower = input("Include Lowercase? (y/n): ").lower() == "y"
            digits = input("Include Digits? (y/n): ").lower() == "y"
            symbols = input("Include Symbols? (y/n): ").lower() == "y"

            password = generate_password(
                length,
                upper,
                lower,
                digits,
                symbols
            )

            if password is None:
                print("Select at least one character type.")
                continue

            strength = check_strength(password)

            print("\nGenerated Password:")
            print(password)
            print("Strength:", strength)

            saved_passwords.append(password)

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":

        if not saved_passwords:
            print("No passwords generated yet.")

        else:
            print("\n----- SAVED PASSWORDS -----")

            for i, pwd in enumerate(saved_passwords, start=1):
                print(f"{i}. {pwd}")

    elif choice == "3":

        if not saved_passwords:
            print("No passwords to save.")

        else:

            with open("passwords.txt", "w") as file:

                for pwd in saved_passwords:
                    file.write(pwd + "\n")

            print("Passwords saved to passwords.txt")

    elif choice == "4":

        print("Thank you for using Password Generator!")
        break

    else:
        print("Invalid choice.")