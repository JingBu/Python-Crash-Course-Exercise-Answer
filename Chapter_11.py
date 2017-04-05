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
