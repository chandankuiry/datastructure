class classname:
	def createname(self,name):
	 	self.name=name
	def displayname(self):
		return self.name
	def saying(self):
		print "hello %s" %self.name
print classname
first=classname()
second=classname()
first.createname("chandan")
second.createname("kuiry")
print first.displayname()
print second.displayname()
first.saying()
second.saying()
#here we learn "self is a temporary placeorder for a objectname here "first" and "second is a  objectname
