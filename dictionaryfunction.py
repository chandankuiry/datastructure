def cart(**items):
	print items
cart(apples=4,peaches=10,beef=9)
def profile(firstname,lastname,*ages,**items):
	print firstname,lastname
	print ages
	print items
profile("chandan","kuiry",42,43,44,45,46,apples=4,banana=80)
#when you enter multiple items then that is tuple,and you use equal sign "ex-banana=10" then  python understand this is dictionary  
