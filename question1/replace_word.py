#!/usr/local/bin/python
""" Replace a given word in all text files in the current directory"""
import sys
import glob, os
os.chdir(".")
def replace_word(find, replace):
    print (find, replace)



if __name__ == "__main__":
    for file in glob.glob("*.txt"):
        print (file)
    
