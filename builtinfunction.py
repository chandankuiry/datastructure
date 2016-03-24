#There are three built-in functions that are very useful when used with lists: filter(), map(), and reduce().
def f(x):
	return x%3==0 or x%5==0
print filter(f,range(2,50))
def cube(y):
	return y*y*y
print map(cube, range(1, 11))
#More than one sequence may be passed;
seq=range(9)
def add(f,g):
	return f+g
print map(add, seq, seq) 
def sum(seq):
	def add(x,y): return x+y
	return reduce(add, seq,5)#if seq is empty then default argument  0 is returned
print sum(range(1))#here return 5
print sum(range(1,50))
print sum([])
#don't use sum() because sum is builtin function
