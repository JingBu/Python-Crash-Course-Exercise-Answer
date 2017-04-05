# ----------------------------------------------------------------------------
# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
# ----------------------------------------------------------------------------
print("This is ex7-4:")
prompt = "Please enter the toppings you want on your pizza: "
prompt += "\n(Enter 'quit' when you finished)"

while True:
    message = raw_input(prompt)   
    if message == 'quit':
        break
    else:
        print("Now I'll add " + message.title() + " to your pizza.")



# ----------------------------------------------------------------------------
# 7-5. Movie Tickets: A movie theater charges different ticket prices depending 
# on a person’s age. If a person is under the age of 3, the ticket is free; if 
# they are between 3 and 12, the ticket is $10; and if they are over age 12,  
# the ticket is $15. Write a loop in which you ask users their age, and then 
# tell them the cost of their movie ticket.
# ----------------------------------------------------------------------------
# 7-6. Three Exits: Write different versions of Exercise 7-5 that do each of  
# the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.
# ----------------------------------------------------------------------------
print("\nThis is ex7-5 and ex7-6:")
prompt = "Please tell us your age: "

while True:
    age = raw_input(prompt)
    if age == 'quit':
        break
    
    if int(age) < 3:
        print("You can have a ticket for free.")
        continue
    elif int(age) < 12:
        print("You have to pay your ticket for $10.")
        continue
    else:
        print("You have to pay your ticket for $15.")
        continue
 
# ----------------------------------------------------------------------------
# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of 
# various sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
# ----------------------------------------------------------------------------
print("This is ex7-8: ")
sandwich_orders = ['tuna', 'chicken', 'potato', 'apple', 'pepper']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made your " + current_order.title() + " sandwich.")
    
    finished_sandwiches.append(current_order)
    
print("\nI have made the following sanwiches: ")
for sandwiches in finished_sandwiches:
    print("- " + sandwiches.title())



# ----------------------------------------------------------------------------
# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.
# ----------------------------------------------------------------------------
print("\nThis is ex7-8: ")
sandwich_orders = ['tuna', 'chicken', 'pastrami', 'apple', 'pastrami',
                   'pastrami', 'tuna', 'pastrami']
print("The sandwich orders are: " + str(sandwich_orders))
print("\nThe Deli has run out of pastrami.") 

finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made your " + current_order.title() + " sandwich.")
    
    finished_sandwiches.append(current_order)
    
print("\nI have made the following sanwiches: ")
for sandwiches in finished_sandwiches:
    print("- " + sandwiches.title())
                 
# ----------------------------------------------------------------------------
# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the 
# world, where would you go? Include a block of code that prints the results
# of the poll. 
# ----------------------------------------------------------------------------
print("\nThis is ex7-9: ")
results = {}

polling_active = True

while polling_active:
    name = raw_input("\nWhat's your name: ")
    prompt = "If you could visit one place in the world, "
    prompt += "where would you go? "
    place = raw_input(prompt)
    
    results[name] = place
    repeat = raw_input("Would you like to let another person respond?" 
                       + "(yes/ no) ")
    if repeat == 'no':
        polling_active = False
 
print("\n--- Poll Results ---")  
for name,place in results.items():
    print(name.title() + " would like to visit " + place.title() + " someday.")     


