# Rebecca Lee's encoder function
def encoder(password):
    encoded_password = ""
    for num in password:
        new_num = (int(num) + 3) % 10
        encoded_password += str(new_num)
    return encoded_password

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu_choice = input("Please enter an option: ")

        if menu_choice == "1":
            password = input("Please enter your password to encode: ")
            password = encoder(password)
            print("Your password has been encoded and stored!")
        if menu_choice == "2":
            encoded_password = decode(password)
            print(f"The encoded password is {password}, and the original password is {encoded_password}")
        if menu_choice == "3":
            break

def decode(str_num):
    decoded = ""
    for i in str_num:
        if int(i) > 2:
            decoded += str(int(i) - 3)
        else:
            decoded += str(int(i) + 7)
    return decoded

if __name__ == '__main__':
    main()