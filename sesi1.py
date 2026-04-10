import random

welcome_message = "Selamat Datang"

print("********************")
print(f"** {welcome_message} **")
print("********************")

nama_player = input("masukkan nama anda: ")
while True:
    cuypy_posistion = random.randint (1, 4)

    print (f''' 
    halo {nama_player} coba tebak di antara 4 goa ini dimana cuypy berada
    |_| |_| |_| |_| 
    ''')

    while True:
        pilihan_player = int(input("goa 1/2/3/4: "))

        if pilihan_player < 1 or pilihan_player > 4:
            print("error")
            continue

        konfirmasi_player = input(f"yakin pilih {pilihan_player}? yes/no: ")

        if konfirmasi_player == "no":
            print("pilih ulang")
            continue
            
        if konfirmasi_player == "yes":
            if pilihan_player == cuypy_posistion:
                print("KAMU MENANG!!!")
                break
            else: 
                print(f"KAMU SALAH tebak lagi: ")
                continue
            
    ulang = input("main lagi ? yes/no ")

    if ulang == "no":
        print("logout")
        break