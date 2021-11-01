import os

def mainLogin():
    IsCorrect = False

    acc = ReadAccData()
    while not IsCorrect:
        UserNameLogin = input("Enter your username: ")
        UserPasswordLogin = input("Enter your password: ")

        os.system("cls")
        
        UserName = UserNameLogin
        UserPassword = UserPasswordLogin
        
        for accNum in range(len(acc)):
            if acc[accNum][0] == UserName and acc[accNum][1] == UserPassword:
                IsCorrect = True
                accIndex = accNum
    return UserName, accIndex

def AccountFileLength():
    File = open("data/accounts/account.txt", "r")
    accFileLength = len(File.readlines())
    File.close()
    return accFileLength

def ReadAccData():
    accFile = open("data/accounts/account.txt", "r")
    acc = []
    for account in range(AccountFileLength()):
        acc.append(accFile.readline().split(' '))
    accFile.close()
    return acc

def WriteNewPassword(username, pwd, role, group, accIndex):
    file = open("data/accounts/account.txt", "r")
    
    list_of_lines = file.readlines()
    if AccountFileLength() <= 1:
        list_of_lines[accIndex] = f"{username} {pwd} {role} {group}"
    else:
        list_of_lines[accIndex] = f"{username} {pwd} {role} {group}\n"

    file = open("data/accounts/account.txt", "w")
    file.writelines(list_of_lines)
    file.close()

def Encryption():
    return

def Decryption():
    return