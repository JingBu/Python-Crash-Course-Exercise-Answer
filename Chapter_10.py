# ----------------------------------------------------------------------------
# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.
# ----------------------------------------------------------------------------
name_0 = raw_input("What's your name?")

filename_0 = "guest.txt"

with open(filename_0, 'w') as file_object:
    file_object.write(name_0.title())

print("This is the end of ex10-3.\n")    
# ----------------------------------------------------------------------------
# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line 
# recording their visit in a file called guest_book.txt. Make sure each entry 
# appears on a new line in the file.
# ----------------------------------------------------------------------------
print("\nThis is ex10-4: ")
print("(Enter 'q' to quit.)")

filename = "guest_book.txt"

while True:
    name = raw_input("What's your name? ")
    
    if name != 'q':
        with open(filename, 'a') as file_object:
            file_object.write(name.title() + "\n")
    
        print("Hello, " + name.title() + "!")
    else:
        break
        
# ----------------------------------------------------------------------------
# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.
# ----------------------------------------------------------------------------
print("\nThis is ex10-5: ")
print("(Enter 'q' to quit.)")

filename = "programming_reason.txt"

while True:
    reason = raw_input("Why you like programming? ")
    
    if reason != 'q':
        with open(filename, 'a') as file_object:
            file_object.write(reason + "\n")
    else:
        break

# ----------------------------------------------------------------------------
# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a TypeError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError if
# either input value is not a number, and print a friendly error message. 
# Test your program by entering two numbers and then by entering some text 
# instead of a number.
# ----------------------------------------------------------------------------
# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.
# ----------------------------------------------------------------------------
print("Give me two numbers, and I'll add them.")
print("(Enter 'q' to quit.)")

while True:
    try:
        first_number = raw_input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = raw_input("Second number: ")
        if second_number == 'q':
            break
    
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry, I really need a number.")
    else:
        print("The answer is: " + answer)

print("This is the end of addition process.\n")
# ----------------------------------------------------------------------------
# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least
# three names of cats in the first file and three names of dogs in the second 
# file. Write a program that tries to read these files and print the contents 
# of the file to the screen. Wrap your code in a try-except block to catch the 
# IO error, and print a friendly message if a file is missing. 
# Move one of the files to a different location on your system, and make sure 
# the code in the except block executes properly.
# ----------------------------------------------------------------------------
# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.
# ----------------------------------------------------------------------------
d_filename = "dogs.txt"
c_filename = "cats.txt"

try:
    with open(d_filename) as df_obj:
        dcontents = df_obj.read()
    with open(c_filename) as cf_obj:
        ccontents = cf_obj.read()
except IOError:
    pass
else:
    print("\nReading File: " + d_filename)
    print(dcontents)
    print("\nReading File: " + c_filename)
    print(ccontents)
    
# Another version using for loop

filenames = ['dogs.txt', 'cats.txt']

for filename in filenames:
    print("\nReading File: " + filename)
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except IOError:
        print("Sorry, I can't find that file.")
    else:
        print(contents)

# ----------------------------------------------------------------------------
# 10-10. Common Words: Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.You can use the count() method to find out how many times a word or
# phrase appears in a string.
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text.
# ----------------------------------------------------------------------------
print("\nThis is ex10-10: ")
line = "Row, row row your boat."
print(line.count('row'))

print(line.lower().count('row'))


import json

# ----------------------------------------------------------------------------
# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate 
# program that reads in this value and prints the message, “I know your 
# favorite number! It’s _____.”
# ----------------------------------------------------------------------------
# 10-12. Favorite Number Remembered: Combine the two programs from Exercise 
# 10-11  into one file. If the number is already stored, report the favorite 
# number to the user. If not, prompt for the user’s favorite number and store 
# it in a file. Run the program twice to see that it works.
# ----------------------------------------------------------------------------
filename = 'favorite_number.json'
try:
    with open(filename) as f_obj:
        favor_num = json.load(f_obj)
except IOError:
    favor_num = raw_input("What's your favorite number? ")
    with open(filename,'w') as f_obj:
        json.dump(favor_num, f_obj)
        print("Thanks, I'll remember that.")
else:
    print("I know your favorite number! It's " + favor_num)
            
print("This is the end of ex10-11 and ex10-12.\n")
# ----------------------------------------------------------------------------
# 10-13. Verify User: The final listing for remember_me.py assumes either that 
# the user has already entered their username or that the program is running 
# for the first time. We should modify it in case the current user is not the 
# person who last used the program.
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username. If it’s not, call get_new_username() to get 
# the correct username.
# ----------------------------------------------------------------------------
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except IOError:
        return None
    else:
        return username
        
def get_new_username():
    """Prompt for a new username."""
    username = raw_input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
        
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        msg = "Is " + username + " the correct username? (y/n) "
        user_info = raw_input(msg)
        if user_info == 'y':
            print("Welcome back, " + username.title() + "!")
        else:
            username = get_new_username()
            print("Welcome back, " + username.title() + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
