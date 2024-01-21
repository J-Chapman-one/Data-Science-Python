# Write code to show the * pattern output below

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

pattern = "*"

for row in range(1,10): # loop for 9 rows of pattern
    
    if row <=5: # increase number stars by one star each iteration in pattern until 5th row is reached
        print(pattern * row)
        
    else: # decrease number of stars in pattern by one star each iteration
        print(pattern * (10 - row))