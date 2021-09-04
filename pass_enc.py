print(":-> Password Encryptor")
pre_password = input("Enter ur shitty Password : ")
password = ""

for i in range(len(pre_password)):
    if pre_password[i].lower() == "a":
        password += "Q"

    elif pre_password[i].lower() == "b":
        password += "W"

    elif pre_password[i].lower() == "c":
        password += "E"

    elif pre_password[i].lower() == "d":
        password += "R"

    elif pre_password[i].lower() == "e":
        password += "T"

    elif pre_password[i].lower() == "f":
        password += "Y"

    elif pre_password[i].lower() == "g":
        password += "U"

    elif pre_password[i].lower() == "h":
        password += "I"

    elif pre_password[i].lower() == "i":
        password += "&"

    elif pre_password[i].lower() == "j":
        password += "P"

    elif pre_password[i].lower() == "k":
        password += "a"

    elif pre_password[i].lower() == "l":
        password += "s"

    elif pre_password[i].lower() == "m":
        password += "d"

    elif pre_password[i].lower() == "n":
        password += "#"

    elif pre_password[i].lower() == "o":
        password += "g"

    elif pre_password[i].lower() == "p":
        password += "h"

    elif pre_password[i].lower() == "q":
        password += "j"

    elif pre_password[i].lower() == "r":
        password += "k"

    elif pre_password[i].lower() == "s":
        password += "l"

    elif pre_password[i].lower() == "t":
        password += "Z"

    elif pre_password[i].lower() == "u":
        password += "@"

    elif pre_password[i].lower() == "v":
        password += "f"

    elif pre_password[i].lower() == "w":
        password += "$"

    elif pre_password[i].lower() == "x":
        password += "v"

    elif pre_password[i].lower() == "y":
        password += "x"

    elif pre_password[i].lower() == "z":
        password += "M"
    
    else:
        password += pre_password[i]

print(password)
