#Define the prompt function
def main(cmdno, theme, os):
    try:
        #Loads theme
        reload(theme)
        prompt = (theme.prompt)

        #Exits omnishell
        if cmdno.lower() == ("exit"):
            print("Bye, Bye")
            exit()

        #Show current directory
        elif cmdno == ("cdir"):
            dir_path = os.path.dirname(os.path.realpath(__file__))
            print(dir_path)

        #Does nothing, just prints new prompt
        elif cmdno == (""):
            #Don't worry this isn't meant to do anything
            0 == 0

        #Runs different files and scripts
        else:
            #Checks which file types exist in ./scripts/
            filechkpy  = (os.path.isfile("./scripts/" + cmdno + "/" + cmdno + ".py" ))
            altchkpy   = (os.path.isfile("./scripts/" + cmdno + "/main.py"          ))
            filechkbat = (os.path.isfile("./scripts/" + cmdno + "/" + cmdno + ".bat"))
            filechkexe = (os.path.isfile("./scripts/" + cmdno + "/" + cmdno + ".exe"))
            filechklnk = (os.path.isfile("./scripts/" + cmdno + "/" + cmdno + ".lnk"))

            #Gets the number of matching files
            filematches = 0
            if filechkpy == True:
                filematches = filematches + 1
            if altchkpy == True:
                filematches = filematches + 1
            if filechkbat == True:
                filematches = filematches + 1
            if filechkexe == True:
                filematches = filematches + 1
            if filechklnk == True:
                filematches = filematches + 1

            #Sets file conflict mode
            if filematches > 1:
                print("Looks like there is a file conflict")
                print(os.listdir("./scripts/" + cmdno + "/"))
                conflict = input("choose a file: ")
            else:
                conflict = False

            #Runs python files
            if filechkpy == (bool(True)) or altchkpy == (bool(True)) or conflict == (cmdno + ".py") or conflict == "main.py" :
                cmd = (cmdno + ".py")
                if altchkpy == (bool(True)) and conflict != (cmdno + ".py"):
                    cmd = ("main.py")
                exec(open("./scripts/" + cmdno + "/" + cmd).read())

            #Runs .bat files
            elif filechkbat == (bool(True)) or conflict == (cmdno + ".bat") and options.unixmode == (bool(False)):
                cmd = (cmdno + ".bat")
                dir_path = os.path.dirname(os.path.realpath(__file__))
                bat_path = os.path.join(dir_path, "scripts", cmdno, cmd)
                subprocess.call([bat_path])

            #Runs .exe files
            elif filechkexe == (bool(True)) or conflict == (cmdno + ".exe") and options.unixmode == (bool(False)):
                cmd = (cmdno + ".exe")
                dir_path = os.path.dirname(os.path.realpath(__file__))
                exe_path = os.path.join(dir_path, "scripts", cmdno, cmd)
                subprocess.call(exe_path)

            #Runs .lnk files (shortcuts)
            elif filechklnk == (bool(True)) or conflict == (cmdno + ".lnk") and options.unixmode == (bool(False)):
                cmd = (cmdno + ".lnk")
                dir_path = os.path.dirname(os.path.realpath(__file__))
                lnk_path = os.path.join(dir_path, "scripts", cmdno, cmd)
                os.startfile(lnk_path)

            #If input begins with "p! " run as python code
            elif cmdno[0:3] == ("p! "):
                exec(cmdno[3:])

            #If input begins with "b! " run as bash
            elif cmdno[0:3] == ("b! "):
                os.system("/bin/bash -c " + cmdno[3:])

            #If input begins with "z! " run as zsh
            elif cmdno[0:3] == ("z! "):
                os.system("/bin/zsh -c " + cmdno[3:])

            #If input begins with "f! " run as fish
            elif cmdno[0:3] == ("f! "):
                os.system("/bin/fish -c " + cmdno[3:])

            #If no file exists, it will then try and run it as a shell command
            else:
                os.system(cmdno)

    #If there is an error it prints it
    except Exception as errmess:
        print("Error", errmess)

#Sets the autocomplete list to include: $PATH, native commands, and scripts
completionlist = []
path = os.environ['PATH']
path = path.split(':')
for i in range(len(path)):
    completionlist = completionlist + os.listdir(path[i])
completionlist = completionlist + os.listdir("./scripts/") + ['exit', 'cdir', 'p!', 'b!', 'z!', 'f!']
#Turns the list into a dictionary so that the completetion only happens on the first word, to reduce lag
completiondict = {item: None for item in completionlist}
completer = NestedCompleter.from_nested_dict(completiondict)

#Defines the rules for what counts as a valid command
def valcmd(text):
    #Spaces are valid
    if not text or text.isspace():
        return True

    #If the first word is on the completion list then it is valid
    else:
        text = text.split(maxsplit=1)
        return text[0] in completionlist

#Sets the error for if a command is not valid
cmdvalidator = Validator.from_callable(
    valcmd,
    error_message="Invalid Command",
    move_cursor_to_end=True,
)

#Sets the history file
session = PromptSession(history=FileHistory("./.omnihistory"))

#The prompt
while True:
    main(session.prompt(theme.prompt, style=theme.style, validator=cmdvalidator, validate_while_typing=True, completer=completer, auto_suggest=AutoSuggestFromHistory()), theme, os)
