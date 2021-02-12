from coloredterm import pattern_print

# The pattern_print function lets you print text with the color being the next one in the pattern.

# Simplify so you do not need do put in the pattern variable.

pattern = ["blue", "green", "yellow"]

# Simplify so you do not need do put in the pattern variable.
def pattern_p(text, **kwargs):
    pattern_print(text, pattern, **kwargs)

pattern_p("Welcome", end=", ")
pattern_p("To The", end=" ")
pattern_p("Demo", end="!")