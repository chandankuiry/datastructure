class company:
	"company has many employee"
	#here we assign class variable
	empcount=0
	#here method is created
#"here __init__ is important"
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		company.empcount +=1
		#here we use class variable if you want to access class variable inside or outside the class you have to write classname.variable.
	def employeecount(self):
		print "total employee %d" % company.empcount
	def displayemployee(self):
		print "name:",self.name, ", salary : ",self.salary
"this would create first object "
emp1=company("chandan",9000)
"this would create second object"
emp2=company("meghnad",4000)
emp1.displayemployee()
emp2.displayemployee()
print "total employee %d"% company.empcount



