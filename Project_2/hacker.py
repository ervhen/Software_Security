import secrets
import hashlib
import string
import itertools
import time
from pathlib import Path


class node:
    def __init__(self, val=None):
        self.key = val
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

def Insert(start, val):
    if start.key is None:
        start.key = val
    else:
        if start.key > val:
            if start.left is None:
                start.left = node(val)
            else:
                Insert(start.left, val)
        else:
            if start.right is None:
                start.right = node(val)
            else:
                Insert(start.right, val)

def Searcher(start, val):
    if start == None:
        return False
    while start != None:
        if start is None:
            return False
        elif start.key.strip() > val.strip():
            start = start.left
        else:
            if start.key.strip() == val.strip():
                return True
            else:
                start = start.right

def Search(start, val):
    if start is None:
        return False
    else:
        if start.key.strip() > val.strip(): 
            if start.key.strip() == val.strip():
                return 1
            Search(start.left, val)
        else:
            if start.key.strip() == val.strip():
                return 1
            Search(start.right, val)


def hackhash(pasize):
    passflag = 0
    counter = 0
    num = 2
    tree = BST()
    tree.root = node()
    filename = Path("hashpass.txt")
    file = open(filename, "r")
    for line in file:
        Insert(tree.root, line.split(',')[1].strip())
    while num <= pasize:
        for x in itertools.product(string.ascii_lowercase, repeat = num):
            counter = counter + 1
            password = ''.join(x)
            hashpass = hashlib.sha256(password.encode()).hexdigest()
            if Searcher(tree.root, hashpass) == 1:
                print("Match found ", password," in ", counter, " tries")
                file.close()
                return
        num = num + 1
                
def hacksalt(pasize):
    passflag = 0
    counter = 1
    num = 2
    count = 0
    tree = BST()
    tree.root = node()
    filename = Path("salted.txt")
    file = open(filename, "r")
    for line in file:
        Insert(tree.root, line.split(',')[2].strip())
    while count <= 255 :
        for i in itertools.product(string.hexdigits, repeat = 2):
            salt = ''.join(i)
            while num <= pasize:
                for x in itertools.product(string.ascii_lowercase, repeat = num):
                    counter = counter + 1
                    password = ''.join(x)
                    salt_pass = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
                    if Searcher(tree.root, salt_pass) == 1:
                        print("Match found ", password, "in ", counter, " tries") 
                        file.close()
                        return 
                num = num + 1
            num = 2
        count = count + 1

thein = 0
while thein is not 3:
    thein = int(input("1)Brute Force into hash or 2)BF into salt"))
    if thein == 1:
        pasize = int(input("Max pass size"))
        start = time.time()
        hackhash(pasize)
        print("It took ", time.time() - start, " seconds")
    if thein == 2:
        pasize = int(input("Max pass size"))
        start = time.time()
        hacksalt(pasize)
        print("It took ", time.time() - start, " seconds")
    else:
        break
