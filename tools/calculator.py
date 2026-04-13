# print ("hello world")

def start():
    while True:
        print ("pilih operasi")
        print ("1. tambah ")
        print ("2. kurang ")
        print ("3. bagi ")
        print ("4. kali ")
        print ("0. keluar")

        pilihan = input("masukkan pilihan anda 1/2/3/4/0 ")
        if pilihan == "0":
            print ("logout")
            break
        
        a = int (input ("masukkan angka pertama: "))
        b = int (input ("masukkan angka kedua: "))

        if pilihan == "1":
            hasil = (a + b)
        elif pilihan == "2":
            hasil = (a - b)
        elif pilihan == "3":
            if b == 0:
                print ("error")
                continue
            hasil = (a / b)
        elif pilihan == "4":
            hasil = (a * b)
        else:
            hasil = ("tidak memilih")

        print (hasil)
        break