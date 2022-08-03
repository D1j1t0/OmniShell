#this runs your .omnirc file
exec(open('.omnirc.py').read())

#This section imports the dependent libraries
import sys
import subprocess
import os
import theme
import options
from rich.console import Console
from rich.prompt import Prompt as prompt
import shutil
from importlib import reload
from pathlib import Path
import time

#defines the login sequence
def login():
    f = open("password.txt", "r")
    lgin = (f.read())
    usr = input("Please enter your Username: ")
    usr = (usr + "\n")
    pss = input("Now enter your Password: ")
    usrpss = (usr + pss)
    if lgin == usrpss:
        print("Correct!")
    else:
        print("Incorrect, try again!")
        login()

#This section shows the splash logo
logo = theme.logo
if options.dologo == True:
    Console().print(logo)

#This section checks if the setup has already been completed
stpcmplt = (os.path.isfile("./password.txt"))

#This section does the main setup
if stpcmplt == (bool(False)):
    usrnm = input("Please assign a Username: ")
    psswrd = input("Please assign a Password: ")
    usrnm = (usrnm + "\n")
    lgn = (usrnm + psswrd)
    print("Writing Password...")
    f = open("password.txt", "w")
    f.write(lgn)
    f.close()
    print("Setup complete")
    exec(open('prompt.py').read())
else:
    #calls the login sequence
    if options.dologin == True:
        login()
    exec(open('prompt.py').read())
