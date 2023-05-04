![Omnilogo](https://raw.githubusercontent.com/D1j1t0/OmniShell-Branding/main/Logos/Omnishell%20Light%20Outline.png)
# What is OmniShell
OmniShell is a **Python-based shell** made with moddablity, configurability, and extensibility in mind.

A quick warning: this is my first big code project and **OmniShell is nowhere near complete** and **I still have many planned features**, so please keep this in mind before using it.

But now that that's out of the way, it's time to talk **features!**
## Features
- Ability to add Python files as shell commands, e.g. instead of `python ~/OmniShell/scripts/themetool.py` you can simply run `themetool`
- A nice theme engine
- Easily configurable
- Cross-platform
  - Windows
  - Linux
  - MacOS (currently untested -- I don't have a Mac)
- Extensible
- Uses your current shell as a base and extends apon it

## Requirements
- Python 3
- [Rich](https://github.com/Textualize/rich)

## Installation
### On Windows
The basic installation on Windows is basically the same as on any other operating system, simply download the latest release zip and extract it, then run `boot.py`. However if you don't want to have to run the Python file every time you want to use Omnishell there are many workarounds depending on your terminal.

#### If you use Windows Terminal:
If you use Windows Terminal the process is quite simple:
1. Open Windows Terminal and open the settings tab using the menu or by pressing `CTRL+,`
2. Next scroll down to the bottom of the sidebar and press the `+` icon and click `+ New empty profile`
3. Now click `Starting directory` and select the path to your OmniShell directory (the one that contains `boot.py`)
4. After that click `Command line` and select your `python.exe`. If you don't know where this is, there is a great guide on how to locate it [here](https://datatofish.com/locate-python-windows/)
5. Now add `boot.py` on the end of the command line field so it ends up looking similar to this: `[path to python.exe]\python.exe boot.py`
6. Finally, add any finishing touches to your OmniShell profile and, if you want, set it as the default profile

#### If you use Fluent Terminal:
If you use Fluent Terminal the process is incredibly similar to the setup on Windows Terminal:
1. Open Fluent Terminal and open the settings window using the menu or by pressing `CTRL+SHIFT+,`
2. Next click the `Profiles` button on the sidebar and click the `+ Create new` button
3. Now in the `Working directory` field select the path to your OmniShell directory (the one that contains `boot.py`)
4. After that in the `Shell executable location` field select your `python.exe`. If you don't know where this is there is a great guide on how to locate it [here](https://datatofish.com/locate-python-windows/)
5. Now in the arguments field put `boot.py`
6. Finally add any finishing touches to your OmniShell profile and, if you want, set it as the default profile

#### If you use Cmder:
If you use Cmder the process is slightly different to the other terminals, but is still very easy to set up:
1. Open Cmder and open the settings window using the menu or by pressing `WIN+ALT+p`
2. Next expand the `Startup` section on the side bar by pressing the `+` icon, and then click `Tasks`
3. Then click the `+` icon, and after that click `File path...` and select `boot.py`
4. Now click the `Startup dir...` button select the path to your OmniShell directory (the one that contains `boot.py`)
5. Finally add any finishing touches to your OmniShell task and, if you want, set it as the default task, and remember to click `Save settings`

### On Linux
The basic installation on Linux is basically the same as on any other operating system: simply download the latest release zip, and extract it, then run `boot.py`. Sadly I don't really know how to make it work on Linux quite as well as it works on Windows, e.g. start automatically on a new terminal instance, so if you have an idea of how I could implement this or even actually have it set up and working, please tell me in the issues how you did it, so I can put it here.

### On MacOS
The basic installation on MacOS is basically the same as on any other operating system: simply download the latest release zip, and extract it, then run `boot.py`. Please keep in mind that this won't make OmniShell start when a new terminal instance is opened. Sadly I don't know how to set this up on MacOS, and neither can I test or find a solution, as I don't have a Mac. However if you do have a way to do this, then please tell me in the issues, so I can add it here.

## Usage

### How to add commands
So you want to add custom commands to OmniShell? Don't worry, this is something I kept in mind the entire time while developing OmniShell, making sure to keep it **quick** and **simple**!

1. First enter the `scripts` directory in the root of your OmniShell folder (the one that contains `boot.py`), and create a new directory called whatever you want the command to be
2. Now in the directory that you've just created, add a file called: `WHATEVER_YOU_CALLED_THE_DIRECTORY.py`, `WHATEVER_YOU_CALLED_THE_DIRECTORY.bat`, `WHATEVER_YOU_CALLED_THE_DIRECTORY.exe` or `WHATEVER_YOU_CALLED_THE_DIRECTORY.lnk`
3. And thats it!

## How to contribute!
So you would like to extend the functionality, or improve the looks of your OmniShell? Well, you are in the right section of the docs, my friend. In this section I will be going over how to make extensions, themes, and scripts for OmniShell.

### How to make themes
So you would like to make a theme for Omnishell? Don't worry, this is very easy and this guide will walk you through how to make a theme, and get your OmniShell looking ***sexy*** in no time!

Now, before we begin, this guide will show you how to make and apply your theme using the theme tool that comes packaged with OmniShell, you can apply themes without the use of the tool but it is not recommended.

1. First enter the `themes` directory in your root OmniShell folder (the one that contains `boot.py`), and create a new directory called whatever the name of your theme will be
2. Now enter the directory you just created and make a new file called `theme.py`
3. Next open `theme.py` in your preferred editor, and create three new variables called `info`, `logo`, and `prompt`, so it looks like this:
```
info = """""" 

logo = """"""

prompt = """"""
```
4. Set the `logo` variable as your logo; this could be ASCII art, an ASCII banner, or any other string. It should look something like this:
```
info = """""" 

logo = """    _      _
   / \    | |    ___   __ _  ___
  / _ \   | |   / _ \ / _` |/ _ \
 / ___ \  | |__| (_) | (_| | (_) |
/_/   \_\ |_____\___/ \__, |\___/
                      |___/"""

prompt = """"""
```
5. Set the `prompt` variable to your prompt. It should look something like this:
```
info = """""" 

logo = """    _      _
   / \    | |    ___   __ _  ___
  / _ \   | |   / _ \ / _` |/ _ \
 / ___ \  | |__| (_) | (_| | (_) |
/_/   \_\ |_____\___/ \__, |\___/
                      |___/"""

prompt = """A
Prompt
can
be
multi
line> """
```

6. Nearly done! Set the info variable to any info you would like users to know about your theme, e.g. the name of the author and the inspiration for the theme. This will be printed when selecting a theme. Your file should now look like this:
```
info = """TEST THEME

This is a test theme to demonstrate how to create themes

By: D1j1t""" 

logo = """    _      _
   / \    | |    ___   __ _  ___
  / _ \   | |   / _ \ / _` |/ _ \
 / ___ \  | |__| (_) | (_| | (_) |
/_/   \_\ |_____\___/ \__, |\___/
                      |___/"""

prompt = """A
Prompt
can
be
multi
line> """
```
7. Add finishing touches. Remember that all these variables are printed with [rich](https://github.com/Textualize/rich) so you can do some fancy stuff. Here are some ideas:
	- You can use Unicode characters like this: `u"\uCHARACTERCODE"`, e.g. for `█` write `u"\u2588"`
	- You can use coloured, bold, italic, and blinking text like [this](https://rich.readthedocs.io/en/stable/style.html)
	- You can use variables in your prompt, logo, or info to make user customization easy, e.g.:
	```
	animal = "cow"
	prompt = (animal + " = best animal> ")
	```
	- You can use Python modules to put things like the time or battery percentage into the prompt, logo, or info, e.g.:
	```
	from datetime import datetime
	now = datetime.now()
	prompt = ("the time is: " + now.strftime('%H:%M:%S') + " > ")
	```
	- Here is a simple yet powerful trick to improve the look and usablity of the prompt: add `\n` as the first thing in the `prompt` variable to add spacing in between prompts, e.g. `prompt = """\nAPrompt> """`
8. Your theme is now complete. Apply it with `themetool` and gaze in awe at your new theme!

### How to make extensions
If you want to extend the functionality or add features to OmniShell then you might want to use extensions. This section will explain how to make and apply extensions.

However before we start there is an issue: different extensions do different things, the solution is that this guide will only show you how to set up environments to make extensions in, and apply the extensions you have made.

1. First enter the `scripts` directory in the root of your OmniShell folder (the one that contains `boot.py`), and create a new directory called whatever you want the command to run your extension to be
2. Now in the directory that you've just created, create a file called `WHATEVER_YOU_CALLED_THE_DIRECTORY.py`
3. Next write your extension in the `.py` file you've just created
4. If you want the extension to run at startup of OmniShell, then put `exec(open('</PATH/TO/PY/FILE>').read())` somewhere in your `.omnirc.py` file
5. Now go and make kick-ass extensions, and show the true power of OmniShell!

### Strut your stuff
You've made your themes and extensions, and you're ready to release them to the world. However, you want people to find them easily and gaze in awe at your readme. Well, don't worry, I have provided all of the OmniShell branding in a separate repo [here](https://github.com/D1j1t0/OmniShell-Branding). However, I also have some tips!

#### If you are releasing a theme
- Use this badge at the top of your `README.md` ![ThemeBadge](https://shields.io/badge/OmniShell-Theme-FFD43A?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMTI4IiBoZWlnaHQ9IjEyOCIgdmlld0JveD0iMCAwIDEyOCAxMjgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik05OS41IDMwVjEwLjVIMTE1QzExNi4zODEgMTAuNSAxMTcuNSAxMS42MTkzIDExNy41IDEzTDExNy41IDExNUMxMTcuNSAxMTYuMzgxIDExNi4zODEgMTE3LjUgMTE1IDExNy41TDMwLjYyMTMgMTE3LjVMMjEuNjIxMyAxMDguNUwzMC42MjEzIDk5LjVMOTggOTkuNUg5OS41Vjk4TDk5LjUgMzBaIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjMiLz4KPHBhdGggZD0iTTkgMTNDOSAxMC43OTA5IDEwLjc5MDkgOSAxMyA5SDk4TDEwOC41IDE5LjVMOTggMzBIMzBWOThMMTkuNSAxMDguNUwzMCAxMTlIMTNDMTAuNzkwOSAxMTkgOSAxMTcuMjA5IDkgMTE1VjEzWiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTU2IDQ2TDc0IDY0TDU2IDgyIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjgiIHN0cm9rZS1saW5lY2FwPSJzcXVhcmUiLz4KPC9zdmc+Cg==&style=for-the-badge) if you are unsure with markdown syntax simply put this at the top or under your logo `![ThemeBadge](https://shields.io/badge/OmniShell-Theme-FFD43A?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMTI4IiBoZWlnaHQ9IjEyOCIgdmlld0JveD0iMCAwIDEyOCAxMjgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik05OS41IDMwVjEwLjVIMTE1QzExNi4zODEgMTAuNSAxMTcuNSAxMS42MTkzIDExNy41IDEzTDExNy41IDExNUMxMTcuNSAxMTYuMzgxIDExNi4zODEgMTE3LjUgMTE1IDExNy41TDMwLjYyMTMgMTE3LjVMMjEuNjIxMyAxMDguNUwzMC42MjEzIDk5LjVMOTggOTkuNUg5OS41Vjk4TDk5LjUgMzBaIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjMiLz4KPHBhdGggZD0iTTkgMTNDOSAxMC43OTA5IDEwLjc5MDkgOSAxMyA5SDk4TDEwOC41IDE5LjVMOTggMzBIMzBWOThMMTkuNSAxMDguNUwzMCAxMTlIMTNDMTAuNzkwOSAxMTkgOSAxMTcuMjA5IDkgMTE1VjEzWiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTU2IDQ2TDc0IDY0TDU2IDgyIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjgiIHN0cm9rZS1saW5lY2FwPSJzcXVhcmUiLz4KPC9zdmc+Cg==&style=for-the-badge)`
- And use the `omnishell` and `omnishell-theme` topics on github
#### If you are releasing an extension
- Use this badge at the top of your `README.md` ![ExtensionBadge](https://shields.io/badge/OmniShell-Extension-5A88FF?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMTI4IiBoZWlnaHQ9IjEyOCIgdmlld0JveD0iMCAwIDEyOCAxMjgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik05OS41IDMwVjEwLjVIMTE1QzExNi4zODEgMTAuNSAxMTcuNSAxMS42MTkzIDExNy41IDEzTDExNy41IDExNUMxMTcuNSAxMTYuMzgxIDExNi4zODEgMTE3LjUgMTE1IDExNy41TDMwLjYyMTMgMTE3LjVMMjEuNjIxMyAxMDguNUwzMC42MjEzIDk5LjVMOTggOTkuNUg5OS41Vjk4TDk5LjUgMzBaIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjMiLz4KPHBhdGggZD0iTTkgMTNDOSAxMC43OTA5IDEwLjc5MDkgOSAxMyA5SDk4TDEwOC41IDE5LjVMOTggMzBIMzBWOThMMTkuNSAxMDguNUwzMCAxMTlIMTNDMTAuNzkwOSAxMTkgOSAxMTcuMjA5IDkgMTE1VjEzWiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTU2IDQ2TDc0IDY0TDU2IDgyIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjgiIHN0cm9rZS1saW5lY2FwPSJzcXVhcmUiLz4KPC9zdmc+Cg==&style=for-the-badge) if you are unsure with markdown syntax simply put this at the top or under your logo `![ExtensionBadge](https://shields.io/badge/OmniShell-Extension-5A88FF?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMTI4IiBoZWlnaHQ9IjEyOCIgdmlld0JveD0iMCAwIDEyOCAxMjgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik05OS41IDMwVjEwLjVIMTE1QzExNi4zODEgMTAuNSAxMTcuNSAxMS42MTkzIDExNy41IDEzTDExNy41IDExNUMxMTcuNSAxMTYuMzgxIDExNi4zODEgMTE3LjUgMTE1IDExNy41TDMwLjYyMTMgMTE3LjVMMjEuNjIxMyAxMDguNUwzMC42MjEzIDk5LjVMOTggOTkuNUg5OS41Vjk4TDk5LjUgMzBaIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjMiLz4KPHBhdGggZD0iTTkgMTNDOSAxMC43OTA5IDEwLjc5MDkgOSAxMyA5SDk4TDEwOC41IDE5LjVMOTggMzBIMzBWOThMMTkuNSAxMDguNUwzMCAxMTlIMTNDMTAuNzkwOSAxMTkgOSAxMTcuMjA5IDkgMTE1VjEzWiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTU2IDQ2TDc0IDY0TDU2IDgyIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjgiIHN0cm9rZS1saW5lY2FwPSJzcXVhcmUiLz4KPC9zdmc+Cg==&style=for-the-badge)`
- And use the `omnishell` and `omnishell-extension` topics on github
# That's All Folks
 I'll add more if I think of anything or if anyone has any good suggestions! :)
