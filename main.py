from libs import welcome_message, exit_program, menu, back_to_menu
from services import auth 

def main():
    auth.auth_start()
    welcome_message()
    menu()
    back_to_menu()
    exit_program()

if __name__ == '__main__':
      main()