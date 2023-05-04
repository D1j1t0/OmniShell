#!/usr/bin/env python3

import os

#Changes Current directory to the OmniShell
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Creates .omnirc.py if it doesn't exist
if os.path.isfile("./.omnirc.py") == False:
    f = open(".omnirc.py", "w")
    f.close()

#This runs your .omnirc file
exec(open('.omnirc.py').read())

#This section imports the dependent libraries
import sys
import subprocess
import os
import options
from rich.console import Console
from rich.prompt import Prompt as prompt
import shutil
from importlib import reload
from pathlib import Path
import time
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.validation import Validator
from prompt_toolkit.styles import Style
import theme

#Defines the login sequence
def login():
    f = open("password.txt", "r")
    lgin = (f.read())
    usr = input("Please enter your Username: ")
    usr = (usr + "\n")
    pss = input("Now enter your Password: ")
    usrpss = (usr + pss)
    if str(lgin) == str(usrpss):
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
if stpcmplt == False and options.dologin == True:
    usrnm = input("Please assign a Username: ")
    psswrd = input("Please assign a Password: ")
    usrnm = (usrnm + "\n")
    lgn = (usrnm + psswrd)
    print("Writing Password...")
    f = open("password.txt", "w")
    f.write(lgn)
    f.close()
    print("Setup complete")
else:
    #Calls the login sequence
    if options.dologin == True:
        login()

#Runs the prompt file
exec(open('prompt.py').read())
