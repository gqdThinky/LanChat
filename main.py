import socket, sys
from colorama import init, Fore, Back, Style
from configparser import ConfigParser
from pathlib import Path

init(autoreset=True)
config = ConfigParser()


def Main():
    
    print('{:^230s}'.format("""
                                                                                               _                 _____ _           _   
                                                                                              | |               /  __ \ |         | |  
                                                                                              | |     __ _ _ __ | /  \/ |__   __ _| |_ 
                                                                                              | |    / _` | '_ \| |   | '_ \ / _` | __|
                                                                                              | |___| (_| | | | | \__/\ | | | (_| | |_ 
                                                                                              \_____/\__,_|_| |_|\____/_| |_|\__,_|\__|"""))

    print('\n{:^240s}'.format(Fore.RED + "CONNECT"))
    print('\n{:^240s}'.format(Fore.RED + "SETTINGS"))

    input_user = input('\n\n\n{:^100s}'.format(Fore.GREEN + "user@lanchat: "))


    if input_user.lower() == "connect":
        pass
    if input_user.lower() == "settings":
        Settings()

def Settings():
    
    print('{:^230s}'.format("""
                                                                                               _                 _____ _           _   
                                                                                              | |               /  __ \ |         | |  
                                                                                              | |     __ _ _ __ | /  \/ |__   __ _| |_ 
                                                                                              | |    / _` | '_ \| |   | '_ \ / _` | __|
                                                                                              | |___| (_| | | | | \__/\ | | | (_| | |_ 
                                                                                              \_____/\__,_|_| |_|\____/_| |_|\__,_|\__| (settings)"""))
    file_path = Path(r"data\userinfo.ini")
    
    # parse existing file
    config.read(file_path)

    # read values from a section
    user_val = config.get('user_info', 'name')

    print('\n\n{:^100s}'.format(Fore.GREEN + "Current name :" + Back.WHITE + " {}".format(user_val)) + Style.RESET_ALL)
    input_user = input('\n\n\n{:^100s}'.format(Fore.GREEN + "user@lanchat: "))

    # update existing value
    config.set('user_info', 'name', input_user)

    # save to a file
    with open(file_path, 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    Main()
