def control():
    username = input("Username: ").lower()
    password = input("Password: ").lower()

    if username == "admin":
        if password == "admin":
            print("Success")
        else:
            print("Password Sehvdir")
            control()
    else:
        print("Username Sehvdir")
        control()


