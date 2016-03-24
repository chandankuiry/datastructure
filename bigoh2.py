import time
def foo(tom):
    start=time.time()
    fred = 0

    for bill in range(1,tom+1):
       barney = bill
       fred = fred + barney
    end=time.time()
    return fred,end-start
# here we calculate the value five times because we want to see the value changes and we want average calculation
for i in range(5):
    print "sum is %d and time taken for this %10.7f"%foo(1000) 



