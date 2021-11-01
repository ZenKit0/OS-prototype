import Design, Commands, Login, Group

UserName, accIndex = Login.mainLogin()

color = Design.Color()
Design.PrintLogo()

while True:
    accData = Login.ReadAccData()
    UserRole = Group.RoleData[accData[accIndex][2]]
    UserRoleSave = Group.RoleData2[UserRole]
    UserGroup = Group.GroupData[accData[accIndex][3].strip('\n')]
    commandStr = input(color.PrintColor(Design.Symbols[accData[accIndex][3].strip('\n')], 'cyan') % (UserRole, UserName))
    if commandStr in Commands.CommandsList:
        if commandStr == "chgpwd":
            Commands.CommandsDict[commandStr](UserName, UserRoleSave, UserGroup, accIndex)
        else:
            Commands.CommandsDict[commandStr]()
    elif commandStr == "":
        continue
    else:
        print(f"Don't recognized \"{commandStr}\" internal command or executable file.")

