# ----------------------------------------------------------------------------
# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
#   • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
#   • Use a loop to print the name of each river included in the dictionary.
#   • Use a loop to print the name of each country included in the dictionary.
# ----------------------------------------------------------------------------
print("This is ex6-5: ")
rivers = {
          'nile': 'egypt',
          'yangtze river': 'china',
          'amazon river': 'brazil'
          }
          
for river,country in rivers.items():
    print("The " + river.title() + " runs through " +
          country.title() + ".")

print("\nThe following rivers have been mentioned: ")
for river in rivers.keys():
    print(river.title())

print("\nThe following countries have been mentioned: ")    
for country in rivers.values():
    print(country.title())
          
# ----------------------------------------------------------------------------          
# 6-6. Polling: Use the code in favorite_languages.py (page 104).
#    • Make a list of people who should take the favorite languages poll. 
# Include some names that are already in the dictionary and some that are not.
#    • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.          
# ----------------------------------------------------------------------------          
print("\nThis is ex6-6: ")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',                      
                      }

pool_list = ['sarah', 'luke', 'phil', 'alex', 'joe']

for name in pool_list:
    if name in favorite_languages.keys():
        print(name.title() + ", thank you for taking the poll.")
    else:
        print(name.title() + ", please take the poll.")

# ----------------------------------------------------------------------------
# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. 
# As you loop through the list, print everything you know about each person.
# ----------------------------------------------------------------------------
print("This is ex6-7: ")
person_0 = {
            'first_name': 'kingsley',
            'last_name': 'king',
            'age': '25',
            'city': 'hongkong',
            }

person_1 = {
            'first_name': 'lily',
            'last_name': 'tuker',
            'age': '12',
            'city': 'new york',
            }

person_2 = {
            'first_name': 'alex',
            'last_name': 'jordan',
            'age': '20',
            'city': 'london',
            }
            
people = [person_0, person_1, person_2]

for person in people:
    print(person)
            
# ----------------------------------------------------------------------------
# 6-8. Pets: Make several dictionaries, where the name of each dictionary is 
# the name of a pet. In each dictionary, include the kind of animal and the 
# owner’s name. Store these dictionaries in a list called pets. Next, loop  
# through your list and as you do print everything you know about each pet.
# ----------------------------------------------------------------------------
print("\nThis is ex6-8: ")
bobby = {
         'animal_kind': 'dog',
         'owner_name': 'cam',
         }

kitty = {
         'animal_kind': 'cat',
         'owner_name': 'alex',
         }         

stella = {
         'animal_kind': 'dog',
         'owner_name': 'jay',
         }

pets = [bobby, kitty, stella]

for pet in pets:
    print(pet)
         
# ----------------------------------------------------------------------------
# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of 
# three names to use as keys in the dictionary, and store one to three 
# favorite places for each person. To make this exercise a bit more  
# interesting, ask some friends to name a few of their favorite places. Loop  
# through the dictionary, and print each person’s name and their favorite 
# places.
# ----------------------------------------------------------------------------
print("\nThis is ex6-9: ")
favorite_places = {
    'jay': ['london', 'new york'],
    'manny':['pairs'],
    'alex': ['china', 'canada', 'bali'],    
}

for name,places in favorite_places.items():
    if len(places) == 1:
        print(name.title() + "'s favorite place is: " + places[0])
    else:
        print(name.title() + "'s favorite places are: ")
        for place in places:
            print("- " + place)

# ----------------------------------------------------------------------------
# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.
# ----------------------------------------------------------------------------
print("\nThis is ex6-10: ")
favorite_numbers = {
    'jay': [3, 5, 7],
    'alex':[2, 4, 6, 8],
    'manny':[1, 2],
    'lily':[3, 4], 
}

for name,numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print(number)

# ----------------------------------------------------------------------------
# 6-11. Cities: Make a dictionary called cities. Use the names of three cities 
# as keys in your dictionary. Create a dictionary of information about each 
# city and include the country that the city is in, its approximate population, 
# and one fact about that city. The keys for each city’s dictionary should be
# something like country, population, and fact. Print the name of each city 
# and all of the information you have stored about it.
# ----------------------------------------------------------------------------
print("\nThis is ex6-11: ")
cities = {
    'beijing': {
        'country': 'china',
        'population': '12 million',
        'fact': 'beautiful place' ,           
                },
    'new york': {
        'country': 'amarica',
        'population': '3 million',
        'fact': 'busy city' ,           
                },
    'paris': {
        'country': 'france',
        'population': '1 million',
        'fact': 'romantic place' ,           
                },                    
          }
for city,city_info in cities.items():
    print("Here is something about " + city.title() + ": ")
    print(city_info)
        
# ----------------------------------------------------------------------------
# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example 
# programs from this chapter, and extend it by adding new keys and values, 
# changing the context of the program or improving the formatting of the 
# output.
# ----------------------------------------------------------------------------



