def is_valid_password(password):
    if len(password) < 8:
        return False

    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_uppercase and has_digit

def main():
    user_password = input("Create your password: ")

    if is_valid_password(user_password):
        print("Password is valid. You can use it for your bank account.")
    else:
        print("Weak password. Please make sure it is at least 8 characters long, contains at least one uppercase letter, and one digit.")

if __name__ == "__main__":
    main()
