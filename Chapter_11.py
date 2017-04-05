# ----------------------------------------------------------------------------
# City, Country: Write a function that accepts two parameters: a city 
# name and a country name. The function should return a single string of the 
# form City, Country, such as Santiago, Chile. Store the function in a module 
# called city_functions.py.
# ----------------------------------------------------------------------------

def city_country(city, country, population=0):
    
    if population:
        """Return a string like 'Santiago, Chile - population 5000000'."""
        return(city.title() + ", " + country.title() + " - population "
               + str(population)) 
    else:
        """Return a string like 'Santiago, Chile'."""
        return(city.title() + ", " + country.title()) 

# ----------------------------------------------------------------------------
# 11-1. City, Country: Write a function that accepts two parameters: a city 
# name and a country name. The function should return a single string of the 
# form City, Country, such as Santiago, Chile. Store the function in a module 
# called city_functions.py.
# Create a file called test_cities.py that tests the function you just wrote
# (remember that you need to import unittest and the function you want to 
# test). Write a method called test_city_country() to verify that calling your 
# function with values such as 'santiago' and 'chile' results in the correct 
# string. Run test_cities.py, and make sure test_city_country() passes.
# ----------------------------------------------------------------------------
# 11-2. Population: Modify your function so it requires a third parameter,
# population. It should now return a single string of the form City, Country –
# population xxx, such as Santiago, Chile – population 5000000. Run
# test_cities.py again. Make sure test_city_country() fails this time.
# Modify the function so the population parameter is optional. Run
# test_cities.py again, and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that verifies
# you can call your function with the values 'santiago', 'chile', and
# 'population=5000000'. Run test_cities.py again, and make sure this new test
# passes.
# ----------------------------------------------------------------------------
import unittest
from City_Functions import city_country as cc

class CitiesTestCase(unittest.TestCase):
    """Tests for 'City_Function.py'."""
    
    def test_city_country(self):
        """Does a simple city and country pair work?"""
        pair_name = cc('Santiago', 'Chile')
        self.assertEqual(pair_name, 'Santiago, Chile')
        
    def test_city_country_population(self):
        """Can I include a population argument?"""
        pair_names = cc('Santiago', 'Chile', 5000000)
        self.assertEqual(pair_names, 'Santiago, Chile - population 5000000')
        
unittest.main()


# ----------------------------------------------------------------------------
# 11-3. Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of 
# these as attributes. Write a method called give_raise() that adds $5000 to 
# the annual salary by default but also accepts a different raise amount.
# Write a test case for Employee. Write two test methods, test_give_
# default_raise() and test_give_custom_raise(). Use the setUp() method so
# you don’t have to create a new employee instance in each test method. Run
# your test case, and make sure both tests pass.
# ----------------------------------------------------------------------------

class Employee(object):
    """A class to represent an employee."""
    
    def __init__(self, f_name, l_name, salary):
        """Initialize an employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary
        
    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount
        
        
import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for module Employee"""
    
    def setUp(self):
        """Make an employee to use in the tests."""
        self.haley = Employee('haley', 'dumphy', 3000)
        
    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.haley.give_raise()
        self.assertEqual(self.haley.salary, 8000)
        
    def test_give_custom_raise(self):
        """Test that a arbitrary raise works correctly."""
        self.haley.give_raise(10000)
        self.assertEqual(self.haley.salary, 13000)

unittest.main()
