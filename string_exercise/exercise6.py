letters = "abcdefghijklmnopqrstuvwxyz"
text = "lbh zhfg hayrnea jung lbh unir yrnearq"
decipher = ""
for chr in text:
    if chr != " ":
        pos = letters.index(chr)
        if pos >= 13:
            decipher += letters[pos-13]
        else:
            decipher += letters[pos+13]
    else:
        decipher += chr
print(decipher)