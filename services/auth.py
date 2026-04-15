

def register():
    print("\nregister")
    new_user = input("buat username: ")
    new_pass = input("buat password: ")

    with open ("users.txt", "a") as file:
        file.write(new_user + "|" + new_pass)


def login():
    print("\nlogin")
    input_user = input("masukkan username: ")
    input_pass = input("masukkan password: ")

    with open('users.txt', "r") as file:
        for line in file:
            data = line.rstrip()
            data_user, data_pass = data.split("|")
            if input_user == data_user and input_pass == data_pass:
                print("user ada")
            else:
                print("user tidak ada")


while True:
    account = input("sudah punya akun? [y/n] ")
    if account == "y":
        login()
    elif account == "n":
        register()
    else:
        print("invalid")
        continue