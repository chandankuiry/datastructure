import os,time,sys
a=0
b=1
temp=0
pid=1
def child(a,b):
	print a+b
print "enter the range of fibonacci series"
i=int(input())
while i>0 and pid:
	temp=a
	a=b
	b==temp+b
	pid=os.fork()
	if pid:
		i=i-1
		os.wait()
		continue
	else:
		child(a,b)
		break

