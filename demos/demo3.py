# Import dictionary with all ansi codes and there hex. Import foreground function to print the foreground.
from coloredterm import colors, fg

for i in colors:
    if int(i) % 15 == 0:
        print(fg(int(i))+i+" "+colors[i], end=", \n")
    else:
        print(fg(int(i))+i+" "+colors[i], end=", ")
