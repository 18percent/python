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
    user_options = int(input("pilih menu: \n1. Games \n2. Tools \n3. Keluar Program \n\nsilahkan pilih: "))
    if user_options == 1:
        games_menu()
    elif user_options == 2:
        tools_menu()
    elif user_options == 3:
        exit_program()
    else:
        print("pilih 1 smpe 3 lolo")
        menu()


def games_menu(): 
    user_options = int(input("pilih menu: \n1. Battle Game \n2. Cuypy \n3. Guess Number \n\nsilahkan pilih: "))
    if user_options == 1:
        battleGame.start()
    elif user_options == 2:
        cuypy.start()
    elif user_options == 3:
        guessNumber.start()


def tools_menu(): 
    user_options = int(input("pilih menu: \n1. Calculator \n2. Currency Converter \n\nsilahkan pilih: "))
    if user_options == 1:
        calculator.start()
    elif user_options == 2:
        currencyConverter.start()


def back_to_menu():
    back = input("mau kembali ke menu [y/n] ")
    if back == "y":
        menu()
         

def exit_program():
    print("program akan dihentikan")
    sleep(1)
    print("1...")
    sleep(1)
    print("2...")
    sleep(1)
    print("3...")
    sleep(1)
    print("program dihentikan")
    exit()
      

if __name__ == '__main__':
      welcome_message()
      exit_program()