import random
from libs import welcome_message

welcome_message("Selamat Datang BROK")

nama_player = input("masukkan nama anda: ")
while nama_player == "":
    nama_player = input("eh nama jangan kosong taik: ")

bentuk_goa = "|_|"
goa_kosong_list = [bentuk_goa] * 4 # BENTUK GOA YANG TIDAK BOLEH DI UBAH 

while True:
    cuypy_posistion = random.randint (1, 4)

    goa_temp = goa_kosong_list.copy()
    goa_temp [cuypy_posistion - 1] = "0_0" # merubah index goa ke posisi cuypy yg sdh random dengan 0_0
    
    goa_kosong_final = "". join(goa_kosong_list)
    goa_final = "". join(goa_temp)

    print (f''' 
halo {nama_player} coba tebak di antara 4 goa ini dimana cuypy berada
{goa_final}
''')
    pilihan_player = int(input("goa 1/2/3/4: "))
        
    if pilihan_player < 1 or pilihan_player > 4:
        pilihan_player = (int(input("buto kau antara 1 smo 4 lolo : ")))

    konfirmasi_player = input(f"yakin pilih {pilihan_player}? y/n: ")

    if konfirmasi_player == "n":
       print("pilih ulang")
       continue
            
    if konfirmasi_player == "y":
        if pilihan_player == cuypy_posistion:
            print(f" {goa_final} KAMU MENANG!!!")
            break
        else: 
            print(f" {goa_final} KAMU SALAH tebak lagi: ")
            continue
    else:
        exit()   

ulang = input("main lagi ? y/n ")

if ulang == "n":
    print("logout")
    exit()