import os

with open("Newfile","w") as nf:
    nf.write("This is line 1\nThis is line 2")
    nf.close()
with open ("Newfile","r") as nf:
        lines = nf.readlines()
        print(lines[1])