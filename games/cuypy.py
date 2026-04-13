import random

def start():
    while True:
        cuypy_posistion = random.randint (1, 4)

        bentuk_goa = " |_| "
        goa_kosong_list = [bentuk_goa] * 4 # BENTUK GOA YANG TIDAK BOLEH DI UBAH 
        
        goa_temp = goa_kosong_list.copy()
        goa_temp [cuypy_posistion - 1] = "0_0" # merubah index goa ke posisi cuypy yg sdh random dengan 0_0
        
        goa_kosong_final = "". join(goa_kosong_list)
        goa_final = "". join(goa_temp)

        print (f"coba tebak di antara 4 goa ini dimana cuypy berada\n{goa_kosong_final}")
        pilihan_player = int(input("goa 1/2/3/4: "))
            
        if pilihan_player < 1 or pilihan_player > 4:
            pilihan_player = (int(input("buto kau antara 1 smo 4 lolo : ")))

        if pilihan_player == cuypy_posistion:
            print(f" {goa_final} KAMU MENANG!!!")
        else: 
            print("KAMU SALAH tebak lagi: ")
            continue

        play_again = input("mau main lagi gak? [y/n]" )
        if play_again == "n":
            break
        

        
if __name__ == '__main__':
      start()