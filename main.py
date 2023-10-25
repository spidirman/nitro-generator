import os
import random
import string
import time
import ctypes
import requests
from colorama import Fore
import threading

class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes.txt"
        self.valid = []
        self.invalid = 0

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
        else:
            print(f'\33]0;Nitro Generator and Checker - Made by spidirman', end='', flush=True)

        print(Fore.MAGENTA + """


███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗    ██████╗ ██╗   ██╗
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║    ██╔══██╗╚██╗ ██╔╝
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║    ██████╔╝ ╚████╔╝ 
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║    ██╔══██╗  ╚██╔╝  
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║    ██████╔╝   ██║   
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═════╝    ╚═╝   
                                                                                           
███████╗██████╗ ██╗██████╗ ██╗██████╗ ███╗   ███╗ █████╗ ███╗   ██╗                        
██╔════╝██╔══██╗██║██╔══██╗██║██╔══██╗████╗ ████║██╔══██╗████╗  ██║                        
███████╗██████╔╝██║██║  ██║██║██████╔╝██╔████╔██║███████║██╔██╗ ██║                        
╚════██║██╔═══╝ ██║██║  ██║██║██╔══██╗██║╚██╔╝██║██╔══██║██║╚██╗██║                        
███████║██║     ██║██████╔╝██║██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║                        
╚══════╝╚═╝     ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                                     
""")
        time.sleep(2)
        self.slowType("mon github : https://github.com/spidirman/", .02)
        time.sleep(1)
        self.slowType("\nTu veux générer combien de liens ? : ", .02, newLine=False)

        num = int(input(''))

        self.slowType("\nInsère le lien de ton webhook\nAppuie sur ENTRÉE si tu n'en as pas : ", .02, newLine=False)
        url = input('')
        webhook = url if url else None

        threads = []

        for i in range(num):
            thread = threading.Thread(target=self.generate_and_check, args=(webhook,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        print(Fore.YELLOW + f"""
Resultats:
 Valid: {len(self.valid)}
 Invalid: {self.invalid}
 Valid Codes: {', '.join(self.valid )}""")

        input("\nFini ! Appuie 3 fois sur ENTRÉE pour voir mon github et fermer le programme, sinon appuie sur la croix rouge en haut à droite")
        [input(i) for i in range(3, 2, 1)]

    def slowType(self, text, speed, newLine=True):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def generate_and_check(self, webhook):
        try:
            code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
            url = (Fore.RED + f"https://discord.gift/{code}")

            result = self.quickChecker(url, webhook)

            if result:
                self.valid.append(url)
            else:
                self.invalid += 1
        except Exception as e:
            print(f" Error | {e}")
            time.sleep(1)

    def quickChecker(self, nitro, notify=None):
        url = f"https://discordapp.com/api/v10/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)

            if notify:
                requests.post(notify, json={"content": f"Code nitro valide! @everyone \n{nitro}"})

            return True
        else:
            print(f" Invalid | {nitro} ", flush=True, end="\n" if os.name == 'nt' else "\n")
            return False

if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
