import questionary
from termcolor import colored
from dotenv import load_dotenv
import os
import bcrypt
import sys


class PyScreen:

    def unlock(self):
        print(colored('\n\nWelcome to Proxifier\n', 'blue', attrs=['bold']))
        answer = questionary.password("What's your secret?").ask()
        salt = bcrypt.gensalt()
        hashed_answer = bcrypt.hashpw(answer.encode('utf-8'), salt)

        load_dotenv()
        secret = os.getenv('PROXIFIER_SECRET')
        hashed_secret = bcrypt.hashpw(secret.encode('utf-8'), salt)

        if(hashed_answer != hashed_secret):
            print(colored('\n\nWrong Secret\n', 'red', attrs=['bold']))
            sys.exit()

    def input_platforms(self):
        choice = questionary.select(
            "Choose one or more platforms:",
            choices=[
                'Markless',
                'ProxyBay',
            ],
        ).ask()

        return choice

    def input_type(self):
        choice = questionary.select(
            "Choose one or more platforms:",
            choices=[
                'http',
                'socks4',
                'socks5',
            ],
        ).ask()

        return choice
