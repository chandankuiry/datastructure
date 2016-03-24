class parent:
	var1="chandan"
	var2="kuiry"
class child(parent):
	var2="toast"
parentobject=parent()
childobject=child()
print childobject.var1
print childobject.var2
#here we show that childobject inherit the property of parent object but it also overwrite that ,here child object overwrite "var2"
