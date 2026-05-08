import socket
from games import battleGame, cuypy, guessNumber
from tools import calculator, currencyConverter
from time import sleep

PC_NAME = socket.gethostname()

def welcome_message():
    style = "*" * (len(PC_NAME) + 6)
    print(f"{style}")
    print(f"** {PC_NAME} **")
    print(f"{style}")


def menu(): 
    while True:
        try:
            user_options = int(input("pilih menu: \n1. Games \n2. Tools \n3. Keluar Program \n\nsilahkan pilih: "))
            if user_options == 1:
                games_menu()
            elif user_options == 2:
                tools_menu()
            elif user_options == 3:
                exit_program()
            else:
                print("pilih 1 smpe 3 lolo")
                continue
        except ValueError:
            print ("masukken angka !")


def games_menu(): 
    try:
        user_options = int(input("pilih menu: \n1. Battle Game \n2. Cuypy \n3. Guess Number \n\nsilahkan pilih: "))
        if user_options == 1:
            battleGame.start()
        elif user_options == 2:
            cuypy.start()
        elif user_options == 3:
            guessNumber.start()
    except ValueError:
        print ("masukken angkan !")    


def tools_menu(): 
    try:
        user_options = int(input("pilih menu: \n1. Calculator \n2. Currency Converter \n\nsilahkan pilih: "))
        if user_options == 1:
            calculator.start()
        elif user_options == 2:
            currencyConverter.start()
    except ValueError:
        print ("masukken angka !")


def back_to_menu():
    while True:
        back = input("mau kembali ke menu [y/n] ").lower() 
        if back == "y":
            break
        elif back == "n":
            exit_program()
        else:
            print("pilih y or n aja")
         

def exit_program():
    print("program dihentikan")
    sleep(1)
    exit()
      

if __name__ == '__main__':
    pass