num=list()
while True:
	inp=raw_input("enter a number")
	if inp=='done':
		break
	value=float(inp)
	num.append(value)
average=sum(num)/len(num)
print average
