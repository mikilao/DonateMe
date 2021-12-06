from donations_pkg.homepage import show_homepage
from donations_pkg.user import login, register

database = {"admin": "password123"}

donations = []

authorized_user = " "


while True:
    show_homepage()
    if authorized_user == " ":
        print("You must be logged in to donate"),
    elif authorized_user != "":
        print("Logged in as ", authorized_user)

    todo = input("Choose an option:")

    if todo == "1":
        username = input("Enter username: ")
        password = input("Enter your password: ")
        login(database, username, password)

        if username != database:
            print("username not recognized")
    elif todo == "2":
        username = input("Enter New Username:")
        password = input("Enter Password:")
        authorized_user = register(database, username)
        if authorized_user != " ":
            database.update(username)
        print("TODO: Write Register Functionality")
    elif todo == "3":
        print("TODO: Write donate Functionality")
    elif todo == "4":
        print("TODO: Write Show Donations Functionality.")
    else:
        print("Goodbye")
        break
