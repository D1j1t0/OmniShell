from prompt_toolkit.styles import Style

logo=("""[red italic]
       `'';;
          ;;
          ;;;;;;;
          ;;
          ;;
          ;;
          ;;
   ,;''';;';,
   ';,,;'   '',,
[/red italic]""")

style = Style.from_dict({
    'main': 'bg:ansired fg:ansiblack',
    'end':  'bg:ansibrightred fg:ansired',
})

prompt=[('class:main', ' よ'), ('class:end', '▌')]
