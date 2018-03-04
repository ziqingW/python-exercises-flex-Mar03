word = input("Give a word to start: ")
word_ori = word.lower()
vowels = []
changed_word = ""
# find out how many vowels in word
# record the vowel in tuple as (vow, index)
# collect all the vowel tuples in a list
for i in range(len(word)):
    chr = word_ori[i]
    if chr in ["a", "e", "i", "o", "u"]:
        vowel = (chr, i)
        vowels.append(vowel)
vowels_num = len(vowels)
# rule 1: if there's only one vowel, and it's at the end of the word,
# this vowel is long vowel
if vowels_num == 1:
    if vowels[0][1] == len(word) - 1:
        changed_word = word[:-1] + word[-1] * 5
# rule 2: if only one vowel as 'i' or 'o',
# and there are two or more consonants followed, it can be long vowel
    elif vowels[0][0] in ["i", "o"] and vowels[0][1] < len(word) - 2:
        changed_word = word[:vowels[0][1]] + vowels[0][0] * 5 + word[(vowels[0][1] + 1):]
    else:
        changed_word = word
# rule 3: if there are two vowels, the first vowel is long vowel        
elif vowels_num == 2:
# here, considering two continus vowels, take the first as long vowel, omit the second
    if vowels[0][0] == vowels[1][0] and vowels[0][1] == vowels[1][1] - 1:
        changed_word = word[:vowels[0][1]] + vowels[0][0] * 5 + word[(vowels[1][1] + 1):]
# for other situation, multiply the first vowel to five folds
    else:
        changed_word = word[:vowels[0][1]] + vowels[0][0] * 5 + word[(vowels[0][1] + 1):]
else:
    changed_word = word
print(changed_word)