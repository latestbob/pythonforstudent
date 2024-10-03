# variables : Python variables are simply containers for storing data values. 
# variable data types (String, integer, float, boolean, List, Dict, Set)

name = 'John'
car = "Benz"
country = 'Nigeria'
age = 28




# String : alphanumerical : Noun is a name of any person, animal , place or thing

name = 'Joseph'
food = 'Egusi'
state = 'Imo State'



# print(f"My name is {name}, I love {food}, and am from {state}")



# integer are data types for whole numbers

# numbers without decimals

age = 999
length = 60
distance = 300
weight = 70

first = 100
second = 20

# sum = first + second


# print(f"The addition of {first}  and {second} is {sum}")

# print(f"I love to own a {car} ")
# print(f"I am {age} years old and am from  {country}")


# float are data types to store numerical decimals
# example 30.99, 

price = 30.99
area = 62.40
weight = 70.50



# print(f"The area of a circle is {area}")


# Boolean are data type that sures the truthness or falseness of an expression or conditon
#  True or False

isLogging = True

isSubcribed = False


# print(3>4)
# print(isSubcribed)


# Array , List : is just collection of similar or disimilar data


fruits = ["mango", "apple", "orange", "banana", 30]
scores = [20, 40, 60, 70, 70]


print(len(fruits))

# print(fruits)

# print(fruits[4])

# print(f"I love {fruits[0]} and {fruits[3]}")

# print(scores[2])


# Dicionary is way a of story data with key value pairs

# Lionel Messi

# messi_name = 'Messi'
# messi_age = 36
# messi_country = 'Argentina'



# messi = {"name":"Lionel Messi","age":36,"country":"Argentina","footType":"left footed"}


# print(messi["footType"])
# print(f"The name of the best player in the world is {messi['name']} , he is from {messi['country']}, he is {messi['age']} years old")


family = {'John','James','Jude','Jude'}

# print(family)


# Let's talk about tranforming from one variable to another

# tranfrom to string using the str() method

age = 202

myage = '20'


anotherage = 20.5




convertedvalue = str(anotherage)





typeofdata = type(convertedvalue)

# print(typeofdata)
# print(convertedvalue)


# booloean to string

# True or False

isLogging = False
isSubcribed = True



isLogging = str(isLogging)


# print(type(isLogging))



# transform ton integer using the int() method



count = '10'

count_two = '4'

# sum = count - count_two

sum  = int(count) - int(count_two)

# print(sum)



price = 80.99

price = int(price)

# print(type(price))
# print(price)


active = False

active = int(active)
# print(active)


# count = int(count)

# print(type(count))

# tranform to float using to float() method

# converting string to float

weight = '70.5'


weight = float(weight)

multiply = 2 * weight
# print(multiply)

# print(type(weight))

# integer to float

length = 561

new_length = float(length)

# print(type(new_length))
# print(new_length)







# tranform to boolean using the bool() method


# Arithemtic operations in python
#  addition +
# substraction using -
# multiplicatioin *
# division using /
# BODMAS



# first = 10
# second = 300
# sum = first + second



# SUBSTRACTION
# first = 10
# second = 300
# sum = second - first

# ctrl + /


# Multiplication 

# first = 10.5
# second = 30.5
# sum = second * first

# # convert to nearest whole number

# sum = int(sum)

# Division

first = 100
second = 5
sum = first / second

# convert to nearest whole number

sum = int(sum)










# print(f"The division of {first} and  {second} is {sum}")

# Learn how to prompt user input
# use the input()

# user information, like name, age, place of birth


name = input("Please enter your name ")

age = input("Please enter your age ")

place_of_birth = input("Kindly enter your place of birth ")

state = input("Kindly enter your state of origin ")

# print(f" Welcome {name} to this application")

age = int(age)

dateofbirth = 2024 - age


print(type(age))
print(f"Welcome {name}, your age is {age}, your date of birth is {dateofbirth}")


# Create a console application
# That calculate a worker annual salary from the monthly salary

# Prompt user to enter their monthly salary
# print(f"Your annual salary is {annual_salary}"
# newest