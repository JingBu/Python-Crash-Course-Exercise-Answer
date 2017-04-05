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
