def login(database, username, password):
   ## username = input("Enter Username:")
    ##password = input("Enter Password:")
    if {username: password} == database:
        print("Welcome! ", username)

    elif username != database:
        print("incorrect Username")
        username = input("Enter Username:")
        ##password = input("Enter Password:")
    elif password != database:
        print("incorrect Password")
       ## username = input("Enter Username:")
        password = input("Enter Password:")


def register(database, username):

    if username in database:
        print("Username already registered.")
        return ""
    else:
        print(" ")
        return database.append(username)
