def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n): # return Fibonacci series up to n
	"""this is my codewrithin"""
	result = []
	a, b = 0, 1
	while a < n:
        	result.append(a)    # see below
        	a, b = b, a+b
     	print result        #here we give "print" option so it show result if we give "return option then it don't show result

