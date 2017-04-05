# ----------------------------------------------------------------------------
# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing 
# different albums. Print each return value to show that the dictionaries are 
# storing the album information correctly.
#     Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for 
# the number of tracks, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of tracks on an album.
# ----------------------------------------------------------------------------
# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have 
# that information, call make_album() with the user’s input and print the 
# dictionary that’s created. Be sure to include a quit value in the while loop.
# ----------------------------------------------------------------------------
print("This is ex8-7 and ex8-8: ")

def make_album(artist_name, album_title, track_num=''):
    """Return a dictionary describing a music album """
    album_info = {'artist name': artist_name, 'album title': album_title,}
    if track_num:
        album_info['number of tracks'] = track_num
    return album_info
    
while True:
    print("(enter 'q' at any time to quit)")
    
    ar_name = raw_input("\nTell me the artist's name: ")
    if ar_name == 'q':
        break

    al_name = raw_input("\nWhat's the album's name: ")
    if al_name == 'q':
        break
    tr_num = raw_input("\nDo you know the number of tracks on that album? ")
    if tr_num == 'q':
        break

print("Here is something about an album: ")
album = make_album(ar_name, al_name, tr_num)
print(album)


# ----------------------------------------------------------------------------
# 8-12. Sandwiches: Write a function that accepts a list of items a person 
# wants on a sandwich. The function should have one parameter that collects as 
# many items as the function call provides, and it should print a summary of 
# the sandwich that is being ordered. Call the function three times, using a 
# different number of arguments each time.
# ----------------------------------------------------------------------------
print("This is ex8-12: ")

def make_sandwich(*items):
    """Make a sandwich with the given items."""   
    print("\nI'll make you a great sandwich: ")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")
    
make_sandwich('cheese', 'roast beef', 'lettcue')
make_sandwich('turkey', 'extra cheese', 'honey dijon', 'apple slice')
make_sandwich('strawberry jam', 'peanut butter')

# ----------------------------------------------------------------------------
# 8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
# a profile of yourself by calling build_profile(), using your first and last 
# names and three other key-value pairs that describe you.
# ----------------------------------------------------------------------------
print("\nThis is ex8-13: ")

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('alex', 'dumphy',
                             location='new york',
                             field='physics')
print(user_profile)
# ----------------------------------------------------------------------------
# 8-14. Cars: Write a function that stores information about a car in a 
# dictionary. The function should always receive a manufacturer and a model 
# name. It should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value 
# pairs, such as a color or an optional feature. Your function should work for 
# a call like this one:
# --------------------------------------------------------------------------
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# --------------------------------------------------------------------------
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.
# ----------------------------------------------------------------------------
print("\nThis is ex8-14: ")

def make_car(make, model, **options):
    """Make a dictionary representing a car."""
    car_info = {
    'manufacturer': make.title(), 
    'model': model.title(),
    }
    for option, value in options.items():
        car_info[option] = value

    return car_info

my_tesla = make_car('tesla', 's', color='silver', year=2017)
print(my_tesla)

