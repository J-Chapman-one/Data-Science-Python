# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"  # runtime error - Lion was not defined, was meant to be string so added "" 
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth." # runtime error - used f string to get defined variables to carry through # also likely human error, number of teeth and animal type needed swaping around # added fullstop after teeth

print (full_spec) # syntax error, was no brackets around statement to be printed

