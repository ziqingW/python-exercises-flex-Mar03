word = input("Give a word to start: ")
word_ori = word.lower()
vowels = []
changed_word = ""
for i in range(len(word)):
    chr = word_ori[i]
    if chr in ["a", "e", "i", "o", "u"]:
        vowel = (chr, i)
        vowels.append(vowel)
vowels_num = len(vowels)
if vowels_num == 1:
    if vowels[0][1] == len(word) - 1:
        changed_word = word[:-1] + word[-1] * 5
    elif vowels[0][0] in ["i", "o"] and vowels[0][1] < len(word) - 2:
        changed_word = word[:vowels[0][1]] + vowels[0][0] * 5 + word[(vowels[0][1] + 1):]
    else:
        changed_word = word
elif vowels_num == 2:
    if vowels[0][0] == vowels[1][0] and vowels[0][1] == vowels[1][1] - 1:
        changed_word = word[:vowels[0][1]] + vowels[0][0] * 5 + word[(vowels[1][1] + 1):]
    else:
        changed_word = word[:vowels[0][1]] + vowels[0][0] * 5 + word[(vowels[0][1] + 1):]
else:
    changed_word = word
print(changed_word)