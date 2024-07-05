# esta sin testear y todavia no se si funciona, si funciona que alguien me lo diga, lo que hace es basicamente contactar con la api de roblox y si el usuario esta en uso sigue intentando con todas las combinaciones de 3 a 7 letras
# in english 4 universal understanmd :)

import requests
from itertools import product
from string import ascii_lowercase
from colorama import Fore, init, Style
from time import sleep
import os
init()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_purple(text):
    # Función para imprimir texto en morado
    print(Fore.MAGENTA + text + Style.RESET_ALL)

def print_ascii_art():
    clear_screen()
    print_purple("                        ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗██████╗ ██╗      ██████╗ ██╗  ██╗")
    print_purple("                       ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔══██╗██║     ██╔═══██╗╚██╗██╔╝")
    print_purple("                       ██║     ███████║█████╗  ██║     █████╔╝ ██████╔╝██║     ██║   ██║ ╚███╔╝ ")
    print_purple("                       ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══██╗██║     ██║   ██║ ██╔██╗ ")
    print_purple("                       ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗██████╔╝███████╗╚██████╔╝██╔╝ ██╗")
    print_purple("                       ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝  BETA")
    print(f'{Fore.RED}                                                 By cizcow / francis ;)')
    print(f'{Fore.GREEN}                                  Prepare for {Fore.CYAN} cizpass {Fore.GREEN} first release - gg/SprvEruq')


def menu():
    print_ascii_art()






def generate_username_combinations(length):
    chars = ascii_lowercase
    for combination in product(chars, repeat=length):
        yield "".join(combination)

def is_username_available(username):
    url = "https://users.roblox.com/v1/usernames/validate"
    payload = {
        "context": "Signup",
        "username": username
    }
    response = requests.post(url, json=payload)
    data = response.json()
    
    if 'code' in data:
        return data['code'] == 0
    else:

        return False

def main():
    menu()
    opcion = input(f"{Fore.YELLOW}\n               [🦊] This CHECKER is in dev and unchecked, please mind that b4 talking shit ;) | Proceed? (y/n): ")
    if opcion == "y":
        clear_screen()
        print_ascii_art()
        print_purple("cizcow@francis~$: Preparing.")
        sleep(1)
        clear_screen()
        print_ascii_art()
        print_purple("cizcow@francis~$: Preparing..")
        sleep(1)
        clear_screen()
        print_ascii_art()
        print_purple("cizcow@francis~$: Preparing...")
        sleep(1)
        clear_screen()
        print_ascii_art()
        print_purple("Please wait...")
        sleep(1)
        clear_screen()
        print_ascii_art()
        print_purple("...")


        sleep(2)

    elif opcion == "n":
        clear_screen()
        print(f"{Fore.RED}Aborting...")
        sleep(1)
        exit()


    else:
        clear_screen()
        print_ascii_art()
        print(f"{Fore.RED}Invalid option, please try again.")
        sleep(1)
        clear_screen()
        main()
        

    

    found_username = False

    for length in range(3, 7):
        if found_username:
            break

        username_generator = generate_username_combinations(length)
        
        for username in username_generator:
            if is_username_available(username):
                print(f"{Fore.GREEN}                            [🟢] Username {username} is available. | cizcow checker")
                found_username = True
                break
            else:
                print(f"{Fore.RED}                              [🔴] Username {username} is already in use or invalid. | cizcow checker")

if __name__ == "__main__":
    main()
