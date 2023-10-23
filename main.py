# Rebecca Lee's encoder function
def encoder(password):
    encoded_password = ""
    for num in password:
        new_num = (int(num) + 3) % 10
        encoded_password += str(new_num)
    return encoded_password

def main():
    password = input("Enter a password to be encoded: ")
    print(f"Encoded passwaord: {encoder(password)}")

if __name__ == '__main__':
    main()
