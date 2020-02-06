# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

import string
def alphabet_position(text):
    letter_count = dict(zip(string.ascii_lowercase, [0]*26))
    count = 1
    for k,v in letter_count.items():
        letter_count[k] += count
        count += 1
    new_text = text.lower()
    for k,v in letter_count.items():
        if k in new_text:
            new_text = new_text.replace(k,str(v) + ' ')
        else:
            new_text += ''
    return new_text.strip()

print(alphabet_position('-.-'))