# change and reprint inital sentence “The!quick!brown!fox!jumps!over!the!lazy!dog.” to remove !'s
# change and print next sentence “The quick brown fox jumps over the lazy dog” to uppercase
# print sentence in reverse

sentence_1 = "The!quick!brown!fox!jumps!over!the!lazy!dog."
sentence_2 = sentence_1.replace("!"," ")
print (sentence_2)

sentence_3 = sentence_2.upper()
print (sentence_3)

print(sentence_3[ : : -1])