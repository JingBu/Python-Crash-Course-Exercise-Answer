# ----------------------------------------------------------------------------
# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message 
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.
# ----------------------------------------------------------------------------
print("This is ex9-1: ")

class Restaurant(object):
    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and suisine type attributes."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Display a summary about the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)
    
    def open_restaurant(self):
        """Display a message indicating that the restaurant is open."""
        print(self.name + " is open. Come on in!")
        
my_restaurant = Restaurant('cukalo','pizza')
print(my_restaurant.name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


# ----------------------------------------------------------------------------
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.
# ----------------------------------------------------------------------------
print("\n\nThis is ex9-2: ")

your_restaurant = Restaurant('mango thai','thai food')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

print("\n")
his_restaurant = Restaurant('hadami','sea food')
his_restaurant.describe_restaurant()
his_restaurant.open_restaurant()

# ----------------------------------------------------------------------------
# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically 
# stored in a user profile. Make a method called describe_user() that prints a 
# summary of the user’s information. Make another method called greet_user() 
# that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.
# ----------------------------------------------------------------------------
print("\n\nThis is ex9-3: ")

class User(object):
    
    def __init__(self, first_name, last_name, sex, age):
        """Initialize first_name, last_name, sex and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
    
    def describe_user(self):
        """Print the infoemation about the user."""
        full_name = self.first_name + " " + self.last_name
        print("The user's name is " + full_name.title() + ".")
        print(full_name.title() + " is a " + self.sex + ".")
        print(full_name.title() + " is " + str(self.age) + " years old.")
        
    def greet_user(self):
        """Print personalized greeting to the user."""
        full_name = self.first_name + " " + self.last_name
        print("Hello, " + full_name.title() + "!")
        
user1 = User('alex', 'dumphy', 'women', 17)
user1.describe_user()
user1.greet_user()

print("\n")
user2 = User('joe', 'prichet', 'man', 8)
user2.describe_user()
user2.greet_user()


# ----------------------------------------------------------------------------
# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
#   Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
#   Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.
# ----------------------------------------------------------------------------
print("This is ex9-4: ")

class Restaurant(object):
    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and suisine type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Print information abour a restaurant."""
        print("The name of the restaurant is " + self.name.title() + ".")
        print("The cuisine type of the restaurant is " + 
              self.cuisine_type.title() + ".")
    
    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print("The " + self.name.title() + " restaurant is open!")
        
    def read_number_served(self):
        """Print a statement showing the number of customers the restaurant
           has served."""
        print("The restaurant has served " + str(self.number_served) + 
                " customers.")
    
    def set_number_served(self, number):
        """Set the served number"""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't roll back the number of served customers.")
    
    def increment_number_served(self, nums):
        """Add the given amount to the number served."""
        if nums >=0:
            self.number_served += nums  
        else:
            print("You can't roll back the number of served customers.")
            
            
res = Restaurant('kalalo', 'chinese')
res.describe_restaurant()
res.set_number_served(20)
res.read_number_served()

print("\n")
res.increment_number_served(10)
res.read_number_served()

# ----------------------------------------------------------------------------
# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was 
# incremented properly, and then call reset_login_attempts(). 
# Print login_attempts again to make sure it was reset to 0.
# ----------------------------------------------------------------------------
print("\n\nThis is ex9-5: ")

class User(object):
    
    def __init__(self, first_name, last_name, sex, age):
        """Initialize first_name, last_name, sex and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        """Print the infoemation about the user."""
        full_name = self.first_name + " " + self.last_name
        print("The user's name is " + full_name.title() + ".")
        print(full_name.title() + " is a " + self.sex + ".")
        print(full_name.title() + " is " + str(self.age) + " years old.")
        
    def greet_user(self):
        """Print personalized greeting to the user."""
        full_name = self.first_name + " " + self.last_name
        print("Hello, " + full_name.title() + "!")
        
    def read_login_attempts(self):
        """Print a statement showing the number of login attempts."""
        print("Now the value of login_attempts is: " + str(self.login_attempts) 
              + ".")

    def increment_login_attempts(self, number):
        """Add the given amount to login attempts."""
        if number >=0:
            self.login_attempts += number
        else:
            print("You can't roll back the login numbers!")
            
    def reset_login_attempts(self):
        """Reset the login attempts numbers to 0."""
        self.login_attempts = 0
    
user = User('haley', 'dumphy', 'women',23)
user.describe_user()
user.increment_login_attempts(3)
user.read_login_attempts()
print("\nThen we have to reset the value of login attempts.")
user.reset_login_attempts()
user.read_login_attempts()

# ----------------------------------------------------------------------------
# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class 
# you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either 
# version of the class will work; just pick the one you like better.
#   Add an attribute called flavors that stores a list of ice cream flavors.  
# Write a method that displays these flavors. Create an instance of
# IceCreamStand, and call this method.
# ----------------------------------------------------------------------------
print("This is ex9-6: ")

class Restaurant(object):
    
    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and suisine type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Print information abour a restaurant."""
        print("The name of the restaurant is " + self.name.title() + ".")
        print("The cuisine type of the restaurant is " + 
              self.cuisine_type.title() + ".")
    
    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print("The " + self.name.title() + " restaurant is open!")
        
    def read_number_served(self):
        """Print a statement showing the number of customers the restaurant
           has served."""
        print("The restaurant has served " + str(self.number_served) + 
                " customers.")
    
    def set_number_served(self, number):
        """Set the served number"""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't roll back the number of served customers.")
    
    def increment_number_served(self, nums):
        """Add the given amount to the number served."""
        if nums >=0:
            self.number_served += nums  
        else:
            print("You can't roll back the number of served customers.")
            
class IceCreamStand(Restaurant):
    """Represent aspect of a restaurant, specific to icecream stand."""
    
    def __init__(self, name, cuisine_type='ice_cream'):
        super(IceCreamStand, self).__init__(name, cuisine_type)
        self.flavors = []
        
    def display_flavors(self):
        """Display the icecream flavors of the icecream stand."""
        print("We have the following flavors: ")
        for flavor in self.flavors:
            print("- " + flavor.title())

my_icecream = IceCreamStand('dairy queen')
my_icecream.describe_restaurant()
my_icecream.flavors = ['oreo', 'vanilla', 'chocolate', 'black cherry']
my_icecream.display_flavors()


            
# ----------------------------------------------------------------------------
# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set 
# of privileges. Create an instance of Admin, and call your method.
# ----------------------------------------------------------------------------
class User(object):
    
    def __init__(self, first_name, last_name, sex, age):
        """Initialize first_name, last_name, sex and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        """Print the information about the user."""        
        full_name = self.first_name + " " + self.last_name
        print("The user's name is " + full_name.title() + ".")
        print(full_name.title() + " is a " + self.sex + ".")
        print(full_name.title() + " is " + str(self.age) + " years old.")
        
    def greet_user(self):
        """Print personalized greeting to the user."""
        full_name = self.first_name + " " + self.last_name
        print("Hello, " + full_name.title() + "!")
        
    def read_login_attempts(self):
        """Print a statement showing the number of login attempts."""
        print("Now the value of login_attempts is: " + str(self.login_attempts) 
              + ".")

    def increment_login_attempts(self, number):
        """Add the given amount to login attempts."""
        if number >=0:
            self.login_attempts += number
        else:
            print("You can't roll back the login numbers!")
            
    def reset_login_attempts(self):
        """Reset the login attempts numbers to 0."""
        self.login_attempts = 0


class Admin(User):
    """Reprensent aspect of user, specific to administrator."""
    
    def __init__(self, first_name, last_name, sex, age):
        super(Admin, self).__init__(first_name, last_name, sex, age)
        self.privileges = Privileges()
          
# ----------------------------------------------------------------------------
# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 
# 9-7. Move the show_privileges() method to this class. Make a Privileges 
# instance as an attribute in the Admin class. Create a new instance of Admin 
# and use your method to show its privileges.
# ----------------------------------------------------------------------------
print("\nThis is ex9-7 and ex9-8: ")

class Privileges(object):
    """A class to store an admin's privileges."""
    
    def __init__(self, privileges = ['can add post', 'can delete post', 
                'can ban user']):
        self.privileges = privileges
    
    def show_privileges(self):
        """Showing the privileges of adaministrator."""
        print("Here is the privileges of an administrator: ")
        for privilege in self.privileges:
            print("- " + privilege.title())

admin_1 = Admin('haley', 'dumphy', 'women', 22)
admin_1.describe_user()
admin_1.privileges.show_privileges()

# ----------------------------------------------------------------------------
# 9-9. Battery Upgrade: Use the final version of electric_car.py from this 
# section. 
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.
# ----------------------------------------------------------------------------
print("\nThis is ex9-9: ")

class Car(object):
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """Print a statement showing the car's milage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
           Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
            
        
class ElectricalCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
        """
        super(ElectricalCar, self).__init__(make, model, year)
        self.battery = Battery()

class Battery(object):
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
            
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Check the battery size and set the capacity to 85 if it 
           isn't already.
        """
        if self.battery_size != 85:
            self.battery_size = 85
            print("Upgraded the battery to 85-kwh")
        else:
            print("The battery size is already upgraded to 85-kwh.")


my_tesla = ElectricalCar('tesla', 'model s', 2017) 
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print("\n")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



