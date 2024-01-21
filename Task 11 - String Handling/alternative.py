# below program changes phrase Hello World makes each alternate character into an upper case character and each other
# alternate character a lower case character, phrase becomes HeLlO WoRlD

sentence = "Hello World"
final_string = ""

# variable that is used to store the value of the current iteration of a loop in range which is length of sentence
for i in range(len(sentence)): 

# every odd index will be upper case or else will be lower case

    if i % 2 == 1:
        
        final_string += sentence [i].upper()
        
    else:
        
        final_string += sentence [i].lower()
        
print(final_string)

# below program changes phrase I am learning to code makes each alternate word into upper case and each other
# alternate word lower case , phrase becomes I am learning to code

sentence2 = "I am learning to code"
new_sentence = sentence2.split(" ") # sentence split words to list
another_list = [] # this is where new list will be appended

for counter in range(len(new_sentence)):  # counter 0 in first iteration and so on, range is length of list
    if counter %2 ==0:
        another_list.append (new_sentence[counter].upper())
    else: 
        another_list.append  (new_sentence[counter].lower())
    
print(" ".join(another_list))  # prints joined new sentence from another_list  