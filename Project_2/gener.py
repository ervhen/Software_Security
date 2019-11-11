import random
import hashlib
import string
import secrets
from pathlib import Path

def gensalt(hmany,pwsz,pwsm):
    fileplain = Path("plainpass.txt")
    filesalt = Path("salted.txt")
    filehash = Path("hashpass.txt")
    fs = open(filesalt, "a")
    fh = open(filehash, "a")
    fpl = open(fileplain, "a")
    for i in range(hmany):
        name = ''.join(random.choices(string.ascii_lowercase+string.digits,k=8))
        passize = random.randint(pwsm,pwsz)
        password = ''.join(random.choices(string.ascii_lowercase,k=passize))
        hashed = hashlib.sha256(password.encode()).hexdigest()
        salt = secrets.token_hex(1)
        salt_pass = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        ses = name, ",", salt, ",", salt_pass,"\n"
        seq = name, ",",password, "\n"
        seh = name, ",",hashed, "\n"
        fpl.writelines(seq)
        fs.writelines(ses)
        fh.writelines(seh)
    fpl.close()
    fh.close()
    fs.close()



useinput = 0
hmany = 0
while useinput is not 3:
    useinput = int(input("Press 1"))
    if useinput == 1:
        hmany = int(input("How many?"))
        pwsm = int(input("What should the lower bound for pass size be"))
        passize = int(input("What should the max size be?"))
        gensalt(hmany,passize, pwsm)
    if useinput == 2:
        exit()
