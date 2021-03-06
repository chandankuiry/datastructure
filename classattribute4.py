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

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
print hasattr(emp1, 'salary')    # Returns true if 'age' attribute exists
print getattr(emp1, 'salary')    # Returns value of 'salary' attribute it access the attribute
setattr(emp1, 'salary', 8000) # Set attribute 'age' at 8
print emp1.salary
setattr(emp1,"name","chandan")
print emp1.name
emp1.displayEmployee()
delattr(emp1, "name")
delattr(emp1,"salary")    # Delete attribute 'age' and delattr have only two arguments 
print emp1.name
print emp1.salary#after delattr operation displayEmployee has no attribute of self.name and self.salary so 



