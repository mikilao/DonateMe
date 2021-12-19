def login(database, username, password):

    if username in database and database[username] == password:
        print(f"\nWelcome back {username}!")
        return username
    elif username in database and database[username] != password:
        print(f"\nIncorrect password for {username}!")
        return ""
    else:
        print("incorrect Password")
        ## username = input("Enter Username:")
        password = input("Enter Password:")
        return ""


def register(database, username):
    if username in database:
        print("\nUsername already registered.")
        return ""
    else:
        print(f"New Username {username} registered!")
        return ""
