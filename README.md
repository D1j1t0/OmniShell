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

# For more info check the [wiki](https://github.com/D1j1t0/OmniShell/wiki)
