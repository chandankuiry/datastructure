import time 
def sumOfn3(n):
   start=time.time()
   s= (n*(n+1))/2
   end=time.time()
   return s ,end-start 
   


for i in range(5):
	print "Sum is %d required %10.7f seconds"%sumOfn3(1000)

