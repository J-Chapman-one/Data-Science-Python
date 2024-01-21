age = int(input("Please input your age: ")) #ask user to input age, this is in whole number(integer) format
if age > 100:
    print("Sorry you're dead") #message displayed if user is older than 100
elif age >64:
    print("Enjoy your retirement") #message displayed if user is aged between 65 and 99
elif age > 40:
    print("You're over the hill") #message displayed if user is aged between 41 and 64
elif age==21:
    print("Congrats on your 21st!") #message displayed if user is aged exactly 21
elif age <13:
    print("You qualify for the kiddie discount") #message displayed if user is aged 12 or under
else:
    print("Age is just a number.") #message displayed if user is aged between 13 and 20 or aged between 22 and 39