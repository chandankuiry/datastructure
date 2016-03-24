class parentclass:
	var1="i am var1"
	var2="i am var2"
class childclass(parentclass):
	pass
parentobject=parentclass
childobject=childclass
print parentobject.var1
print childobject.var1
print "here we show that childobject access the parentobject property"
