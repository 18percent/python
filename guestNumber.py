import random

angka_rahasia = random.randint(1, 20)


while True:
    tebak = int (input("tebak angkanya: "))

    if tebak <1 or tebak >20:
        print ("error")
        continue

    elif tebak == angka_rahasia:
        print ("benar")
        break

    elif tebak < angka_rahasia:
        print ("diatas")
    
    else:
        print ("dibawah")