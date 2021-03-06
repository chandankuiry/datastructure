from gcd import gcd
class Fraction:
	def __init__(self,top,bottom):
		self.num=top
		self.den=bottom
	def __str__(self):
		return str(self.num) + '/' +str(self.den)
	def __add__(self,otherfraction):
		newnum=self.num*otherfraction.den +self.den *otherfraction.num
		newden=self.den *otherfraction.den
		common=gcd(newnum,newden)
		return Fraction(newnum/common,newden/common)
f1=Fraction(3,9)
f2=Fraction(3,18)
f3=f1+f2
print f3
