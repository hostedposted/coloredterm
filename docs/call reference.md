# Call Reference

Here you will find info about all functions and classes in the coloredterm library.

## HEX Function
``The HEX function converts a Hex color code to the closest ansi escape code.``
```py
HEX(
    color
)
```

## RGB Function
``The RGB function converts a Rgb tuple to the closest ansi escape code.``
```py
RGB(
    r,
    g,
    b
)
```

## fg Function
``The fg function changes the foreground of the terminal.``
```py
fg(
    color
)
```

## bg Function
``The bg function changes the background of the terminal.``
```py
bg(
    color
)
```

## Style Class
``The Style class has all of the codes to change the style of the terminal.``
```py
Style.BOLD = "\x1b[1m"
Style.DIM = "\x1b[2m"
Style.UNDERLINE = "\x1b[4m"
Style.BLINK = "\x1b[5m"
Style.REVERSE = "\x1b[7m"
Style.HIDDEN = "\x1b[8m"
Style.RESET = "\x1b[0m"
Style.__doc__ =     """\nCollection of different styles\n"""
```

## Fore Class
``The Fore class has 16 colors, you can make your terminals foreground.``
```py
Fore.BLACK = "\x1b[30m"
Fore.RED = "\x1b[31m"
Fore.GREEN = "\x1b[32m"
Fore.YELLOW = "\x1b[33m"
Fore.BLUE = "\x1b[34m"
Fore.PURPLE = "\x1b[35m"
Fore.CYAN = "\x1b[36m"
Fore.WHITE = "\x1b[37m"
Fore.LIGHTBLACK_EX = "\x1b[90m"
Fore.LIGHTRED_EX = "\x1b[91m"
Fore.LIGHTGREEN_EX = "\x1b[92m"
Fore.LIGHTYELLOW_EX = "\x1b[93m"
Fore.LIGHTBLUE_EX = "\x1b[94m"
Fore.LIGHTMAGENTA_EX = "\x1b[95m"
Fore.LIGHTCYAN_EX = "\x1b[96m"
Fore.LIGHTWHITE_EX = "\x1b[97m"
```

## Back Class
``The Back class has 16 colors, you can make your terminals background.``
```py
Back.BLACK = "\x1b[30m"
Back.RED = "\x1b[31m"
Back.GREEN = "\x1b[32m"
Back.YELLOW = "\x1b[33m"
Back.BLUE = "\x1b[34m"
Back.PURPLE = "\x1b[35m"
Back.CYAN = "\x1b[36m"
Back.WHITE = "\x1b[37m"
Back.LIGHTBLACK_EX = "\x1b[90m"
Back.LIGHTRED_EX = "\x1b[91m"
Back.LIGHTGREEN_EX = "\x1b[92m"
Back.LIGHTYELLOW_EX = "\x1b[93m"
Back.LIGHTBLUE_EX = "\x1b[94m"
Back.LIGHTMAGENTA_EX = "\x1b[95m"
Back.LIGHTCYAN_EX = "\x1b[96m"
Back.LIGHTWHITE_EX = "\x1b[97m"
```

## colored Function
``The colored function can output colored text with a colored background. With any style.``
```py
colored(
    text,
    color = None,
    on_color = None,
    style = None
)
```

## cprint Function
``Cprint is a combination of the colored and print function``
```py
cprint(
    text,
    color = None,
    on_color = None,
    style = None,
    end = None,
    file = None,
    flush = None
)
```

## pattern_print Function
``The Pattern_print function lets you print text with the next color from a pattern. After the first print statement you do not need to specify pattern.``
```py
pattern_print(
    text,
    pattern=["reset"],
    end=None, 
    file=None,
    flush=None
)
```

## pattern_input Function
``The Pattern_input function lets the user input a statement with the text being colored. After the first input statement you do not need to specify pattern.``
```py
pattern_input(
    text,
    pattern=["reset"]
)
```

## rand Function
``The rand function randomly picks a color and applies it to the text given.``
```py
rand(
    text
)
```