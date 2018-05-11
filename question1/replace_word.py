#!/usr/local/bin/python
""" Replace a given word in all text files in the current directory"""
import sys
import glob
import os
os.chdir(".")


def replace_word(filename, find, replace):
    with open(filename, 'r') as f:
        s = f.read()
        if find not in s:
            return
        f.close()
        os.chdir("./replace")
        with open(filename,'w') as f:
            s = s.replace(find, replace)
            f.write(s)
            f.close()
            os.chdir("..")

if __name__ == "__main__":
    if not os.path.exists("./replace"):
        os.makedirs('replace')
    find = sys.argv[1]
    replace = sys.argv[2]
    for file in glob.glob("*.txt"):
        replace_word(file, find, replace)

