# Exercise from the book "Python Crash Course" 
# This is ex5-8.
# ----------------------------------------------------------------------------
# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting 
# to each user:
#   1. If the username is 'admin', print a special greeting, such as Hello 
# admin,would you like to see a status report?
#    2. Otherwise, print a generic greeting, such as Hello Eric, thank you 
# for logging in again.
# ----------------------------------------------------------------------------
print("Here is ex5-8: ")
usernames = ['haley', 'alex', 'luke', 'admin', 'manny']

for username in usernames:
    if username.lower() == 'admin':
        print("Hello " + username + ", would you like to see status report?")
    else:
        print("Hello " + username + ", thank you for logging again.")
            
# ----------------------------------------------------------------------------
# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of 
# users is not empty.
#    1.If the list is empty, print the message We need to find some users!
#    2.Remove all of the usernames from your list, and make sure the correct
# message is printed.
# ----------------------------------------------------------------------------
print("\nHere is ex5-9: ")
if len(usernames) != 0:
    print("We still have " + str(len(usernames)) + " users !")

#Remove all of the usernames from the list
usernames = []

if len(usernames) == 0:
    print("We need to find some users!")

# ----------------------------------------------------------------------------
# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
#    1. Make a list of five or more usernames called current_users.
#    2. Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
#    3. Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available
#    4. Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.
# ---------------------------------------------------------------------------- 
print("\nHere is ex5-10: ")
current_users = ['haley', 'alex', 'luke', 'lily', 'manny', 'jay']
new_users = ['joe', 'LILY', 'alex', 'kate', 'kavin']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + ", you need to enter a new username.")
    else:
        print(new_user + ", your name is available!")

# ----------------------------------------------------------------------------
# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, 
# such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#    1. Store the numbers 1 through 9 in a list.
#    2. Loop through the list.
#    3. Use an if-elif-else chain inside the loop to print the proper ordinal 
# ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line.
# ----------------------------------------------------------------------------
print("\nHere is ex5-11: ")
numbers = []

for number in range(1,10):
    numbers.append(number)

print("Now the numbers are: ")
print(numbers)

print("\nThe oedinal numbers are: ")
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")



