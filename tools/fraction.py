from math import gcd
class Fraction:
	def __init__(self, molecular, denominator, mode='deploy'):
		if denominator < 0:
			molecular *= -1
			denominator *= -1 
		gcdnum = gcd(molecular, denominator)
		self.mode = mode
		self.m = molecular // gcdnum
		self.d = denominator // gcdnum
	
	def __str__(self):
		gcdnum = gcd(self.m, self.d)
		if (self.d == 1 or self.d // gcdnum == 1 ) and self.mode == 'deploy':
			return str(self.m)
		return str(self.m // gcdnum) + '/' + str(self.d // gcdnum)
	
	def __neg__(self):
		return Fraction(-self.m, self.d)

	def __add__(self, other):
		if self.d == other.d:
			return Fraction(self.m + other.m, self.d)
		lcmDen = (self.d * other.d) // gcd(self.d, other.d)
		return Fraction(self.m * lcmDen // self.d + other.m * lcmDen // other.d, lcmDen)

	def __sub__(self, other):
		if self.d == other.d:
			return Fraction(self.m - other.m, self.d)
		lcmDen = (self.d * other.d) // gcd(self.d, other.d)
		return Fraction(self.m * lcmDen // self.d - other.m * lcmDen // other.d, lcmDen)

	def __mul__(self, other):
		return Fraction(self.m * other.m, self.d * other.d)

	def __truediv__(self, other):
		return Fraction(self.m * other.d, self.d * other.m)

	def __eq__(self, o: object) -> bool:
		return self.m == o.m and self.d == o.d

	def assign(self, value):
		if value.d < 0:
			value.d *= -1
			value.m *= -1
		self.m = value.m
		self.d = value.d