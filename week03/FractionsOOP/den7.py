from math import gcd

class Fraction:

	def __init__ (self,numerator,denominator):
		if denominator < 1:
			raise ValueError('Denominator can`t be zero or negative')

		self.numerator = numerator
		self.denominator = denominator


	def __str__ (self):
		return f'{self.numerator}/{self.denominator}'


	def __repr__(self):
		return f'{self}' 

	def __eq__(self, other):
		return self.numerator/ self.denominator == other.numerator / other.denominator

	def __add__(self,other):
		numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
		denominator = self.denominator * other.denominator

		return Fraction(numerator,denominator).simplification()

	def __lt__(self,other):
		return self.numerator/self.denominator < other.numerator/other.denominator

	def simplification(self):
		greatest_div = gcd(self.numerator,self.denominator)

		return Fraction(self.numerator/greatest_div,self.denominator/greatest_div)


def sorting(ls):
	lis = []

	while ls:
		first = ls[0]
		for val in ls:
			if val < first:
				first = val
		lis.append(first)
		ls.remove(first)

	return lis


def main():
	f1 = Fraction(1,4)
	f2 = Fraction(3,9)

	print(f2.simplification())

	f3 = f1 + f2

	print(f3)

	ls = [f1,f2,f3]
	print(sorting(ls))

if __name__ == '__main__':
	main()