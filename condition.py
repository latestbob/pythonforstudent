# what are conditional statement

#  if and else
# if(condition):
        # action
#    else:
        # action

# age = 45

# if(age < 18)
#     print("You are not an adult")
# else:
#     print("You are an adult")


# name = "Chuks"
# country = "China"

# if(country == 'Nigeria'):
#     print(f"Welcome {name} from {country}")
# else:
#     print("You are not a Nigerian")

# favourite = "Ice Cream"

# if(favourite == 'Pizza'):
#     print("Yes this is my favourite dessert")
# else:
#     print(f"I don't like  {favourite}")

# username = "John"
# password = "12345"

# if(username == "John"):
#     print(f"You are logged in as {username}")
# else:
#     print(f"{username} is not a registered user")

# if(username == 'John' and password == "12345"):
#     print("You are logged in")
# else:
#     print(f"{username}  is not a registered user")

# server_username = "Johnny"
# server_password = "John123**"

# username = input("Welcome kindly enter your username ")
# password = input("Kindly enter your secured password ")

# if(username == server_username and password == server_password):
#     print(f"You are logged in as {username}")

# else:
#     print(f"{username} is not a registered user")

age = 25

# check if the person is a young adult (18 to 25)

# check if the password  is a teenager

# check if the person is a kid


# if(age >= 18 and age < 26):
#     print("You are a young adult")

# elif(age > 12 and age < 18):
#     print("You are a teenager")

# elif(age <= 12):
#     print("You are are kid")

# else:
#     print("You are an elderly adult")



# when username and password is not correct

# when username is correct and password is not correct

# when userame is not valid and password is valid

# when both are correct (Loggin successful)

server_username = "Johnny"
server_password = "Johnny123**"

username = input("Please enter your username ")

password = input("Please enter your password ")


if(username != server_username and password != server_password):
    print("Both username and password credentials are invalid")

elif(username == server_username and password != server_password):
    print("Invalid password credential")

elif(username != server_username and password == server_password):
    print("Invalid Username")

elif(username == server_username and password == server_password):
    print(f"You are successfully logged in as {username}")