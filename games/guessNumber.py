import random


def start():
    while True:
        angka_rahasia = random.randint(1, 20)
        
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

if __name__ == '__main__':
    start()