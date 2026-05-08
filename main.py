from libs import welcome_message, exit_program, menu, back_to_menu
from services import auth 

def main():
    try:
        auth.auth_start()
        welcome_message()

        while True:
            menu()
            back_to_menu()
    except:
         print ("kamu mematikan program secara paksa")

if __name__ == '__main__':
      main()