import math

# this is a calculator to show how much interest you will earn on your investment (either based upn simple or compound interest dependent on selection)
# or conversely if you have a bond, how much you will have to repay on the home loan.


list1 = ["investment", "bond"]
user_choice= input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
    
if user_choice.lower() == "investment" in list1: # if investment is selected then user will be asked the following  
    deposited_money = float(input("Enter the amount of money you are depositing, £"))
    interest_rate = float(input("\n Enter your interest rate: "))                 
    years_invest = int(input("\n Enter the number of years you will invest for: "))

    list2 = ["simple", "compound"] # simple or compound interest option chosen by user
    interest = input("\n Enter either 'simple' or 'compound' interest type from the menu above to proceed: ").lower()
    
    if interest == "simple":
        simple_interest = deposited_money*(1 + ((interest_rate/100)*years_invest)) # calculation of compound interest on savings 
        print("\n Your total savings after", (years_invest), "years will be £", round(simple_interest, 2))
    
    elif interest == "compound":
        compound_interest = deposited_money*math.pow ((1+(interest_rate/100)), years_invest) # calculation of compound interest on savings 
        print("\n Your total savings after", (years_invest), "years will be £", round(compound_interest, 2)) 
    else:
        print("Enter either 'simple' or 'compound' from the menu above to proceed: ")    
           
elif user_choice.lower() == "bond" in list1:  # if bond is selected then user will be asked the following  
    house_value = float(input("Enter the value of your house, £:"))
    house_interest = float(input("\n Enter your annual house interest rate: "))
    months = int(input("\n Enter the number of months you plan to take to repay the bond: "))
    monthly_house_interest = (house_interest/100)/12
    
    
    repayment = ((monthly_house_interest)*house_value)/(1-(1+monthly_house_interest)**(- months)) #calculation of monthly interest on house

    print ("\n Your monthly repayment on your house will be £", round(repayment,2)) # display to 2 decimal places
    
else:
    print ("You have made an incorrect selection, please choose either bond or investment to proceed.") 
    
    
    
   
