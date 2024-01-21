count = 0  # count is control variable
total = 0   #  another variable to add to user input, will store vlaue of all numbers users enters


while True:
    user_input = int(input("Please input a whole number and input -1 to stop: ")) 
    
    count += 1   # this increases the control variable by one with each pass of the loop
    
    if user_input != -1:
        total += user_input # will add user input to total with each iteration, as long as -1 not inputted by user
        
    elif user_input == -1:
        break 
     
average = total / count  # determins average of numbers input by user, but not including the -1 enterred.
    
print (average)

#programme is designed for user to input as many values as they like
#and this will not stop unless they enter -1.
#The average of the numbers they input should then be printed, but should not include the -1 break statement in the caluculation.

# whilst the above prorgramme runs there is a logical erorr in that the average calculation includes the -1 in calculation.
# This is becasue the count +=1 on line 12 needs to be in the if statement, so that user input is only added to total
# when the user input number is not -1 (i.e. all other numbers inputted will be added total for the final avergae caluclation but not -1).