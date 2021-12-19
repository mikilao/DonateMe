from donations_pkg.homepage import show_homepage
from donations_pkg.user import login, register

database = {"admin": "password123"}

donations = []

authorized_user = " "


while True:
    show_homepage()
    if authorized_user == " ":
        print("You must be logged in to donate"),
    elif authorized_user != " ":
        print("Logged in as ", {authorized_user})

    todo = input("Choose an option:")

    if todo == "1":
        username = input("\nusername: ")
        password = input("password: ")
        authorized_user = login(database, username, password)

    elif todo == "2":
        username = input("\n New username: ")
        password = input("New password: ")
        authorized_user = register(database, username)

        if authorized_user != " ":
            database[username] = password

    elif todo == "3":
        print("TODO: Write donate Functionality")
    elif todo == "4":
        print("TODO: Write Show Donations Functionality.")
    else:
        print("Goodbye")
        break
