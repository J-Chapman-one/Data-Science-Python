# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # syntax error, was no brackets around statement to be printed
print ("\n") # syntax error, was unexpected indent and also was no brackets around statement to be printed

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 "  # syntax error, whole code block from line 9 to 15 was indented, removed indent # age_Str does not need to be ==, changed to = # removed years old as its in print statement on line 11
age = int(age_Str) 
print("I'm " + str(age) + " years old. ") # cast age as a string to allow it to be concatenate a str and int

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now) # cast years from now as int, as cannot add str and int

# removed print statement on this line as it made no sense

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + 6 # total needed to be total years  # needs to have +6 to get 330 months as 6 months later
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # syntax error, was no brackets around statement to be printed # could not concatenate so cast int as a str for final print statement

#HINT, 330 months is the correct answer

