import random

def start():
    while True:
        player1 = 100
        musuh   = 100
        
        print (" HP kamu: ", player1)
        print (" HP musuh: ", musuh)
        
        print ("1. Serang")
        print ("2. Heal")
        print ("0. Kabur")

        aksi = input ("pilih aksi: ")

        if aksi == "0":
            print ("yah kabur takut")
            break
        if aksi not in ["1", "2"]:
            print ("error")
            continue
        if aksi == "1":
            damage = random.randint (10, 20)
            musuh -= damage
            print ("damage ", damage, "HP musuh", musuh)
        if aksi == "2":
            heal = random.randint (5, 15)
            player1 += heal 
            print ("heal sebanyak ", heal, "HP kamu ", player1)
        
        if musuh <= 0 :
            print ("kamu menang")
            break

        damage_musuh = random.randint (10, 20)
        player1 -= damage_musuh
        print ("Damage diterima", damage_musuh, "sisa HP ", player1)
        
        if player1 <= 0:
            print("Kamu Kalah")
            break