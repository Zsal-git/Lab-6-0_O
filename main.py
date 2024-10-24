# Initialize a variable to store the encoded password
encoded_password = ""

def encode(password):
    """Encodes the password by adding 3 to each digit."""
    encoded = ""
    for char in password:
        encoded += str((int(char) + 3) % 10)
    return encoded

def decode(encoded_password):
    """Decodes the password by subtracting 3 from each digit."""
    decoded = ""
    for char in encoded_password:
        decoded += str((int(char) - 3) % 10)
    return decoded

def main():
    global encoded_password

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            if encoded_password:
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                print("No encoded password found. Please encode a password first.")

        elif option == "3":
            print("Quitting...")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
