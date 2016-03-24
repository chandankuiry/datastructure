#!/usr/bin/python

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
emp1=Employee("chandan","5000")
emp2=Employee("meghnad","8000")
print emp1.name
print emp2.name

print "Employee.__doc__:", Employee.__doc__#return class documentation string define classes namespace here print "Common base class for all employee
print "Employee.__name__:", Employee.__name__#here print class name and that is employee
print "Employee.__module__:", Employee.__module__#here it print module name where class is defined here print __main__
print "Employee.__bases__:", Employee.__bases__#it return empty tuple containing the base classes
print "Employee.__dict__:", Employee.__dict__#dictionary contain classes name space here it return "{'__module__': '__main__', 'displayCount': <function displayCount at 0x7f999f53f758>, 'empCount': 0, 'displayEmployee': <function displayEmployee at 0x7f999f53f7d0>, '__doc__': 'Common base class for all employees', '__init__': <function __init__ at 0x7f999f53f6e0>}

