# Import foreground function to print the foreground.
from coloredterm import fg

# Setup a loop to print all ansi codes for the fg function.
for i in range(1, 256):
    if int(i) % 15 == 0:
        print(fg(i)+str(i), end=", \n")
    else:
        print(fg(i)+str(i), end=", ")
