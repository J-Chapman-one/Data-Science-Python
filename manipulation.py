# Ask user to enter sentence, then sentence and its lentght (number characters) will be dispalyed. 
# There will be further manipulation of of the user's sentence as below


str_manip = input("Enter a sentence: \n")
print ("Lenght of sentence is: \n", len(str_manip), "characters \n")

str_manip_length = len(str_manip) # Calculate and print length of sentence here

last_letter=str_manip[-1]
print("The last letter of the sentence is: \n", last_letter, "\n")

print("The sentence with the each instacne of last letter replaced by @ is: \n", str_manip.replace(last_letter, "@"), "\n") # Find last letter in user's sentence and replace each instance of that letter with'@'

print ("The last three letter of the sentence backwards are: \n",str_manip[ : -4: -1], "\n")    # Display the last 3 characters in user's sentence backwards

five = str_manip[ : 3]+str_manip [-2 : ] # Create a five-letter word that is made up of the first three characters and the last two characters of users sentence
print ("A five-letter word made up of first three and last two characters of the sentence is: \n",five)