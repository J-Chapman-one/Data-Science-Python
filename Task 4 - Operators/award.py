swim_time = int(input("Please input your time taken for swimming in minutes: ")) #ask user to input qualifying time for swimming in minutes, this is in whole number(integer) format
print("Your time taken for swimming was: ", swim_time, "minutes. \n")

cycle_time = int(input("Please input your time taken for cycling in minutes: ")) #ask user to input qualifying time for cycling in minutes, this is in whole number(integer) format
print("Your time taken for cycling was: ", cycle_time, "minutes. \n")

running_time = int(input("Please input your time taken for running in minutes: ")) #ask user to input qualifying time for cycling in minutes, this is in whole number(integer) format
print("Your time taken for running was: ", running_time, "minutes. \n")

total_time=swim_time+cycle_time+running_time # total time for swimming, cycling, and running
print("Your total time taken for the triathalon was: ",total_time, "minutes.\n")

if total_time<100: # if total time less than 100 mins, display provincial colours award
    print("Your award is Provincial Colours.")

elif (total_time> 101 and total_time <=105): # if total time more than 100 mins and less than 105 mins, display provincial half colours award
    print("Your award is Provincial Half Colours.")
    
elif (total_time> 105 and total_time <=110): # if total time more than 105 mins and less than 110 mins, display provincial scroll award
    print("Your award is Provincial Scroll.")
    
else: # if total time more than 110 mins, display no award
    print("Your received no award.")