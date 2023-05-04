#Prints all installed themes and asks you to select one
print("\nPick a theme", os.listdir("./themes/"))
selecttheme = input("Type the name of a theme: ")
themechk = os.path.isdir("./themes/" + selecttheme + "/")
themepath = ("./themes/" + selecttheme)

#If the theme you selected is valid it imports it
if themechk == True:
    sys.path.insert(0, themepath)
    import theme
    sys.modules.pop('theme')
    import theme
    
    #If the theme has an info variable it will print it
    if hasattr(theme, 'info'):
        Console().print(theme.info)
    
    #It then checks if the theme has a logo and prompt
    print("Features:")
    if hasattr(theme, 'logo'):
        print(u'\u2714' + " Custom Logo")
    else:
        print(u'\u2717' + " Custom Logo")
    if hasattr(theme, 'prompt'):
        print(u'\u2714' + " Custom Prompt")
    else:
        print(u'\u2717' + " Custom Prompt")

    #Then it asks if you would like to install the theme and if yes then it will install it
    switch = input("\nDo you want to switch to this theme? y/n: ")
    if switch.lower() == ("y"):
        if hasattr(theme, 'logo') and hasattr(theme, 'prompt'):
            path = (os.path.dirname(os.path.realpath(__file__)))
            oldtheme = os.path.join(path, 'theme.py')
            applytheme = os.path.join(path, 'themes', selecttheme, 'theme.py')
            shutil.copyfile(applytheme, oldtheme)
            exit()
        else:
            print("\nError: Missing variables in theme file")
    else:
        sys.path.insert(0, "./")
        reload(theme)
        exit()
#If theme doesn't exist it will exit
elif themechk == False:
    print("Theme does not exist")
