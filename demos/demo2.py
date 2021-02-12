# Import background function to print the background. Also Style so we can clear the background after each print.
from coloredterm import bg, Style

# Setup a loop to print all ansi codes for the bg function.
for i in range(1, 256):
    if int(i) % 15 == 0:
        print(bg(i)+str(i), end=", \n")
        print(Style.RESET, end="")
    else:
        print(bg(i)+str(i), end=", ")
        print(Style.RESET, end="")
