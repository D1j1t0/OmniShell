from prompt_toolkit.styles import Style
from datetime import datetime
now = datetime.now()
usrname = ("put your username here")
logo = ('')

info = """[blink][red] ____[yellow]_    [green]     [blue]  _  [purple] _   [red]     [yellow]   _ [green]     [blue]    _[purple] _
|[red]_   _[yellow]|   _[green] _ __[blue]| |_|[purple] | __[red]_  __[yellow]_| |_[green]_   _[blue]__| |[purple] |
  [red]| || [yellow]| | |[green] '__|[blue] __| [purple]|/ _ [red]\/ __[yellow]| '_ [green]\ / _[blue] \ | [purple]|
  |[red] || |[yellow]_| | [green]|  | [blue]|_| |[purple]  __/[red]\__ \ [yellow]| | [green]|  __[blue]/ | |[purple]
  |_[red]| \__[yellow],_|_|[green]   \_[blue]_|_|\_[purple]__||[red]___/_[yellow]| |_|[green]\___|[blue]_|_|
[/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/blink]
 - Showing off the [b]power[/b] of [yellow]Omni[/yellow]-[blue]Shell[/blue]

 Author: D1j1t"""

style = Style.from_dict({
    'front': 'ansigreen',
    'first': 'bg:ansigreen fg:ansiblack',
    'transition1': 'bg:ansiyellow fg:ansigreen',
    'second': 'bg:ansiyellow fg:ansiblack',
    'transition2': 'bg:ansiblue fg:ansiyellow',
    'third': 'bg:ansiblue fg:ansiblack',
    'end': 'ansiblue',
})

prompt = [('class:front', '\n'), ('class:first', ' ' + logo + ' '), ('class:transition1', ''), ('class:second', ' ' + usrname + ' '), ('class:transition2', ''), ('class:third', ' ' + now.strftime('%H:%M:%S') + ' '), ('class:end', ' ')]

logo = """[blink][red] ____[yellow]_    [green]     [blue]  _  [purple] _   [red]     [yellow]   _ [green]     [blue]    _[purple] _
|[red]_   _[yellow]|   _[green] _ __[blue]| |_|[purple] | __[red]_  __[yellow]_| |_[green]_   _[blue]__| |[purple] |
  [red]| || [yellow]| | |[green] '__|[blue] __| [purple]|/ _ [red]\/ __[yellow]| '_ [green]\ / _[blue] \ | [purple]|
  |[red] || |[yellow]_| | [green]|  | [blue]|_| |[purple]  __/[red]\__ \ [yellow]| | [green]|  __[blue]/ | |[purple]
  |_[red]| \__[yellow],_|_|[green]   \_[blue]_|_|\_[purple]__||[red]___/_[yellow]| |_|[green]\___|[blue]_|_|
[/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/purple][/red][/yellow][/green][/blue][/blink]"""
