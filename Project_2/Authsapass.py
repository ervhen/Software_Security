import os
import json
import sys
import secrets
from pathlib import Path
import hashlib

def mkplaintxt():
    nameflag = 1
    passflag = 1
    filename = Path("plainpass.txt")
    file = open(filename, "a")
    while nameflag == 1:
        name = input("Input Username")
        if len(name) == 8:
            nameflag = 0
            break
        else:
            print("Must be 8 chars only")
    while passflag == 1:
        password = input("Input Password")
        passflag = 0
        for c in password:
            if c.isupper():
                passflag = 1
        if passflag == 0:
            break
    seq = name, ",", password,"\n"
    file.writelines(seq)
    file.close()
    
    
        
def mkhashpass():
    nameflag = 1
    passflag = 1
    filename = Path("hashpass.txt")
    file = open(filename, "a")
    while nameflag == 1:
        name = input("Input Username")
        if len(name) == 8:
            nameflag = 0
            break
        else:
            print("Must be 8 chars only")
    while passflag == 1:
        password = input("Input Password")
        passflag = 0
        for c in password:
            if c.isupper():
                passflag = 1
        if passflag == 0:
            break
    password = hashlib.sha256(password.encode()).hexdigest()
    seq = name, ",", password,"\n"
    file.writelines(seq)
    file.close()

def mksaltedpass():
    nameflag = 1
    passflag = 1
    filename = Path("salted.txt")
    file = open(filename, "a")
    while nameflag == 1:
        name = input("Input Username")
        if len(name) == 8:
            nameflag = 0
            break
        else:
            print("Must be 8 chars only")
    while passflag == 1:
        password = input("Input Password")
        passflag = 0
        for c in password:
            if c.isupper():
                passflag = 1
        if passflag == 0:
            break
    salt = secrets.token_hex(1)
    password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    seq = name, ",", salt, ",", password,"\n"
    file.writelines(seq)
    file.close()

def logplaintxt():
    flag = 1
    filename = Path("plainpass.txt")
    file = open(filename, "r")
    name = str(input("Input Username"))
    password = str(input("Input Password"))
    seq = name+','+password+'\n'
    for line in file:
        if line == seq:
            print("Welcome,", name)
            flag = 0
            break
    if flag is 1:
        print("Your username or password was incorrect")
    file.close()

def loghashed():
    flag = 1
    filename = Path("hashpass.txt")
    file = open(filename, "r")
    name = str(input("Input Username"))
    password = input("Input Password")
    password = hashlib.sha256(password.encode()).hexdigest()
    seq = name+','+password+'\n'
    for line in file:
        if line == seq:
            print("Welcome,", name)
            flag = 0
            break
    if flag is 1:
        print("Your username or password was incorrect")
    file.close()

def logsalt():
    filename = Path("salted.txt")
    file = open(filename, "r")
    name = str(input("Input Username"))
    for line in file:
        if line.split(',')[0] == name:
            salt = line.split(',')[1]
            stored = line
    password = input("Input Password")
    password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    seq = name+','+salt+','+password+'\n'
    if stored == seq:
       print("Welcome," + name)
    else:
        print("Your username or password was incorrect")
    file.close()
    

useinput = 0
oin = 0
while useinput is not 4:
    useinput = int(input("How would you like authenticate through?\n1)Plain Text 2)Some Security 3)More Security 4)Quit"))
    if useinput == 1:
        while oin != 3:
            oin = int(input("1)Login 2)Make Account 3)Quit"))
            if oin == 1:
                 logplaintxt()
            if oin == 2:
                 mkplaintxt()
            if oin == 3:
                 break
    if useinput == 2:
        while oin != 3:
            oin = int(input("1)Login 2)Make Account 3)Quit"))
            if oin == 1:
                 loghashed()
            if oin == 2:
                 mkhashpass()
            if oin == 3:
                 break
    if useinput == 3:
        while oin != 3:
            oin = int(input("1)Login 2)Make Account 3)Quit"))
            if oin == 1:
                logsalt()
            if oin == 2:
                mksaltedpass()
            if oin == 3:
                break
    if useinput == 4:
        break
    
