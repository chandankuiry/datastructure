import time
def sumof(n):
	start=time.time()
	sum=0
	for i in range(n+1):
		sum = sum +i
	end=time.time()
	return sum,end-start
# here we calculate the value five times because we want to see the value changes and we want average calculation
for i in range(5):
	print "Sum is %d required %10.7f seconds"%sumof(1000)

