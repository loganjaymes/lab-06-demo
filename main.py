# Author: Logan Bjork

def printMenu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(password):
    newPassword = ""
    newNumToAdd = 0

    for x in str(password):
        newNumToAdd = (int(x) + 3)
        # encodes the password by adding 3 to each number inside the password string
        if newNumToAdd >= 10:
            newNumToAdd = newNumToAdd % 10
            # removes the tens place for the new number, so it's not over two digits
            newPassword += str(newNumToAdd) 
        else:
            newPassword += str(newNumToAdd)

    return newPassword

def decode(password):
    oldPassword = ''
    for i in range(len(password)):
        # decode by subtracting 3 from each int
        new = int(password[i]) - 3
        # checks if new is within range, else adds ten
        if new < 0:
            new += 10
        oldPassword += str(new)
    return oldPassword

def main():
    option = 0
    newPass = ''
    while True:
        printMenu()
        option = int(input("\nPlease enter an option: "))


        if option == 1:
            password = str(input("Please enter your password to encode: "))
            newPass = encode(password)
            print("Your password has been encoded and stored!")
        if option == 2:
            oldPass = decode(newPass)
            print(f'The encoded password is {newPass}, and the original password is {oldPass}.')
        if option == 3:
            break

if __name__ == "__main__":
    main()