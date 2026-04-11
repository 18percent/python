import random

welcome_message = "Selamat Datang"
cuypy_posistion = random.randint (1, 4)

print("********************")
print(f"** {welcome_message} **")
print("********************")

nama_player = input("masukkan nama anda: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4 # BENTUK GOA YANG TIDAK BOLEH DI UBAH 

goa = goa_kosong.copy() # variabel copy an yang berisi aray goa kosong 4 biji dan agar dapat di ubah 
goa[cuypy_posistion - 1] = "0_0" # merubah index goa ke posisi cuypy yg sdh random dengan 0_0


while True:
    
    print (f''' 
    halo {nama_player} coba tebak di antara 4 goa ini dimana cuypy berada
    {goa_kosong}
    ''')

    while True:
        pilihan_player = int(input("goa 1/2/3/4: "))

        if pilihan_player < 1 or pilihan_player > 4:
            print("error")
            continue

        konfirmasi_player = input(f"yakin pilih {pilihan_player}? y/n: ")

        if konfirmasi_player == "n":
            print("pilih ulang")
            continue
            
        if konfirmasi_player == "y":
            if pilihan_player == cuypy_posistion:
                print(f" {goa} KAMU MENANG!!!")
                break
            else: 
                print(f" KAMU SALAH tebak lagi: ")
                continue
            
    ulang = input("main lagi ? y/n ")

    if ulang == "n":
        print("logout")
        break