# In Python, functions are blocks of reusable code that perform a specific task. 
# They help make your code organized and modular. 
# A function is defined using the def 
# keyword, followed by the function name and parameters (optional). 

# functions without parameter


# def greeting():
#     print("Good morning")


# def greetTwo():
#     print("Happy Sunday to you")
#     print("inside function")

# print("outside function")
# greetTwo()


first = 100
second = 300
sum = second - first
def addition():
    
    print(f"the addition of {first} and {second} is {sum}")


# addition()

# functions with parameters


def greetings(firstname, lastname):
    print(f"Good Morning {firstname} {lastname}")



# greetings("Bobson","Edidiong")


def favourite(food):
    print(f"My favourite food is {food}")


# favourite("Amala")



# create function to calculate any age

def ageCalcuator(year):

    age = 2024 - int(year)
    
    print(f"Your age is {age}")


# ageCalcuator('2002')

# # Calculate simple interest
    # interest = (principal * rate * time) / 100

    # Total repayment = Interest + principal

    # total repayment amount for a load in GTBank

rate = 2.5


def totalLoanPayment():

    # loan principal

    principal = input("Kindly enter your loan amount ")

    time = input("How many years would you like to clear your loan ")

    principal = float(principal)
    time = float(time)

    interest = (principal * rate * time) / 100

    totalamount = interest + principal

    print(f"Your total repayment amount for loan of {principal} duration {int(time)} years is N{totalamount}")




totalLoanPayment()
# discount purchase


