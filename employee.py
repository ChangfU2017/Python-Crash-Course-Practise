class Employee ():
	def __init__(self,first,last,annual_salary):
		self.first = first
		self.last = last
		self.salary = annual_salary
		
	def give_raise(self, amount = 5000):
			self.salary += amount
		
		