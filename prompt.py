#loads theme and asks for input
cmdno = Console().input(theme.prompt)
reload(theme)
prompt = (theme.prompt)

#exits omnishell
if cmdno.lower() == ("exit"):
    print("Bye, Bye")

#show current directory
elif cmdno == ("cdir"):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    exec(open('prompt.py').read())

#does nothing, just prints new prompt
elif cmdno == (""):
    exec(open('prompt.py').read())

#runs different files and scripts
else:
    #checks which file types exist in ./scripts/
    filechkpy = (os.path.isfile("./scripts/" + cmdno + "/" + cmdno + ".py"))
    filechkbat = (os.path.isfile("./scripts/" + cmdno + "/" + cmdno + ".bat"))
    filechkexe = (os.path.isfile("./scripts/" + cmdno + "/" + cmdno + ".exe"))
    filechklnk = (os.path.isfile("./scripts/" + cmdno + "/" + cmdno + ".lnk"))

    #prioritises python files
    if filechkpy == (bool(True)):
        cmd = (cmdno + ".py")
        Console().print(prompt + "executing: " + cmd)
        exec(open("./scripts/" + cmdno + "/" + cmd).read())
        exec(open('prompt.py').read())

    #then .bat files
    elif filechkbat == (bool(True)) and options.unixmode == (bool(False)):
        cmd = (cmdno + ".bat")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = os.path.join(dir_path, "scripts", cmdno, cmd)
        Console().print(prompt + "executing: " + cmd)
        subprocess.call([bat_path])
        exec(open('prompt.py').read())

    #next .exe files
    elif filechkexe == (bool(True)) and options.unixmode == (bool(False)):
        cmd = (cmdno + ".exe")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        exe_path = os.path.join(dir_path, "scripts", cmdno, cmd)
        Console().print(prompt + "executing: " + cmd)
        subprocess.call(exe_path)
        exec(open('prompt.py').read())

    #last .lnk files (shortcuts)
    elif filechklnk == (bool(True)) and options.unixmode == (bool(False)):
        cmd = (cmdno + ".lnk")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        lnk_path = os.path.join(dir_path, "scripts", cmdno, cmd)
        Console().print(prompt + "executing: " + cmd)
        os.startfile(lnk_path)
        exec(open('prompt.py').read())

    #if no file exists, it will then try and run it as a shell command
    else:
        os.system(cmdno)
        exec(open('prompt.py').read())
