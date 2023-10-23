# Rebecca Lee's encoder function
def encoder():
    password = input("Enter a password to be encoded: ")
    encoded_password = ""
    for num in password:
        new_num = (int(num) + 3) % 10
        encoded_password += str(new_num)
    print(f"Encoded password: {encoded_password}")

    encoder()
