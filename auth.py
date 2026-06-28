import os

FILE_NAME = "users.txt"

def register():

    print("\n========== USER REGISTRATION ==========")

    username = input("Enter Username : ").strip()
    password = input("Enter Password : ").strip()

    if username == "" or password == "":
        print("Username and Password cannot be empty.")
        return

    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

    with open(FILE_NAME, "r") as file:
        users = file.readlines()

    for user in users:
        data = user.strip().split(",")

        if data[0] == username:
            print("Username already exists.")
            return

    with open(FILE_NAME, "a") as file:
        file.write(username + "," + password + "\n")

    print("Registration Successful!")


def login():

    print("\n========== USER LOGIN ==========")

    username = input("Enter Username : ").strip()
    password = input("Enter Password : ").strip()

    if not os.path.exists(FILE_NAME):
        print("No registered users found.")
        return

    with open(FILE_NAME, "r") as file:
        users = file.readlines()

    for user in users:
        data = user.strip().split(",")

        if data[0] == username and data[1] == password:
            print("Login Successful!")
            return

    print("Invalid Username or Password.")