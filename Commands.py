import os, Design, Login

def Command_Help():
    help_str = '''
Help: 
    Commands Syntax: command_name, *attr_name = *attr_val

Commands:
    - help - show help about everything
    - yes - 'yes' string loop, press ctrl + c to stop :)
    - clear - clear screen
    - chgpwd - change password for actual user
'''
    print(help_str)

def Command_Yes():
    Rainbow = Design.Color()
    try:
        while True:
            Rainbow.PrintRainbow("yes")
    except KeyboardInterrupt:
        print("Stopped 'yes' command. :3s")
        

def Command_clear():
    os.system("cls")
    Design.PrintLogo()

def Command_chgpwd(username, role, group, accIndex):
    acc = Login.ReadAccData()
    pwd1 = "a"
    pwd2 = "b"
    while True:
        print(f"Changing password for \'{username}\'")
        pwd1 = input("Enter new password: ")
        pwd2 = input("Re-enter new password: ")
    
        if pwd1 == pwd2:
            if acc[accIndex][1] == pwd1:
                print("Use other password than actual!")
            else:
                print("Password changed succesful")
                Login.WriteNewPassword(username, pwd1, role, group, accIndex)
                break

CommandsList = [
    "help", #display help command
    "yes", #while looping string yes
    "clear", #clear screen
    "chgpwd" #change password
]

CommandsDict = {
    "help":Command_Help,
    "yes":Command_Yes,
    "clear":Command_clear,
    "chgpwd": Command_chgpwd
}