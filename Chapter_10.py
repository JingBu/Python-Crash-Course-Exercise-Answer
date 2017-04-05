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
