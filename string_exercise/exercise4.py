para = "She did not know what was more satisfying: the sound of a dozen swords drawn as one or the look on Tyrion Lannister's face."
new_para = ""
for chr in para:
    if chr.upper() == "A":
        new_para += str(4)
    elif chr.upper() == "E":
        new_para += str(3)
    elif chr.upper() == "G":
        new_para += str(6)
    elif chr.upper() == "I":
        new_para += str(1)
    elif chr.upper() == "O":
        new_para += str(0)
    elif chr.upper() == "S":
        new_para += str(5)
    elif chr.upper() == "T":
        new_para += str(7)
    else:
        new_para += chr
print(new_para)