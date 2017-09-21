import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		first = 'Jack'
		last = 'Brown'
		annual_salary = 5000
		self.my_test = Employee(first,last, annual_salary)
	
	def test_give_default_raise(self):
		self.my_test.give_raise()
		self.assertEqual(self.my_test.salary, 10000)
	
	def test_give_custom_raise(self):
		self.my_test.give_raise(4000)
		self.assertEqual(self.my_test.salary, 9000)
	
unittest.main()
	