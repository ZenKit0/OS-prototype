from time import sleep
from termcolor import colored

OSLogo = '''   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄
 ▄█▄─▄█▄─▄▄─█▄─▄███▄─▄███▄─█─▄█ █─▄▄─█─▄▄▄▄█
█─▄█─███─▄█▀██─██▀██─██▀██▄─▄█  █─██─█▄▄▄▄─█
▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀  ▀▄▄▄▄▀▄▄▄▄▄▀'''

Symbols = {
    "Administrators" : "<<%s~%s>> ",
    "Users" : "<<%s/%s>> "
}

# if user is Developer in Administrators group: <<%s~%s>>
# if user is User in Users group: <<%s\%s>>

OSVersion = "Ver: 1.2.0 (Stable). Copyright© SantaTech\n"

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'blue', 'cyan', 'green', 'yellow']



def PrintLogo():
    print(OSLogo)
    print(OSVersion)

class Color():
    def PrintColor(self, text, color = 'white'):
        return colored(text, color)

    def PrintRainbow(self, text):
        from time import sleep
        for color in colors:
            print(colored(text, color))
            sleep(0.05)