#ask user to input three different numbers
#then ensure all numbers are in integer(i.e number format)
#carry out four caclulations as respective four variable names refer to and print the output from these four caclualtions

x = input("Enter a number: ")
y = input("Enter a different number: ")
z = input("Enter a different number you have not entered before: ")

x = int(x) #Feedback - It's helpful to validate that the numbers are real integers
y = int(y)
z = int(z)

total = x+y+z
print (total)

firstnum_minus_second = x-y
print (firstnum_minus_second)

third_num_times_first_num = x*z
print (third_num_times_first_num)

all_nums_dived_by_third_num = total/z
print (all_nums_dived_by_third_num)