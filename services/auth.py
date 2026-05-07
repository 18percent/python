def register():
    print("\nregister")
    new_user = input("buat username: ").strip()
    new_pass = input("buat password: ").strip()

    with open ("users.txt", "r") as file:
        for line in file:
            data = line.rstrip()
            data_user, data_pass = data.split("|")
            if data_user == new_user:
                print ("username sudah di pakai")
                auth_start()

    with open ("users.txt", "a") as file:
        file.write(new_user + "|" + new_pass  + "\n")


def login():
    print("\nlogin")
    input_user = input("masukkan username: ").strip()
    input_pass = input("masukkan password: ").strip()

    with open('users.txt', "r") as file:
        for line in file:
            data = line.rstrip()
            data_user, data_pass = data.split("|")
            if data_user == input_user and data_pass == input_pass:
                return
    print ("user atau password salah")
    exit()


def auth_start():
    while True:
        account = input("\nsudah punya akun? [y/n] ")
        if account == "y":
            login()
            break
        elif account == "n":
            register()
        else:
            print("invalid")
            continue

if __name__ == "__main__":
    auth_start()