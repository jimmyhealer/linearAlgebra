class Martix:
	def __init__(self, numbers, isextend=False):
		self.numbers = numbers
		self.isextend = isextend
		self.rank = len(numbers)

	def __str__(self):
		row = ""
		if self.isextend:
			for item in self.numbers:
				for i in range(self.rank // 2):
					row.join(str(item[i]) + ' ')
				row.join('| ')
				for i in range(self.rank // 2, self.rank):
					row.join(str(item[i]) + ' ')
				row.join('\n')
		else:
			for i in range(self.rank):
				row += str(self.numbers[i]) + ' '
		return row

	def __getitem__(self, key):
		return self.numbers[key]
	
	def getitem(self, key):
		return self.numbers[key]

	def __add__(self, otehr):
		temp = []
		if type(otehr) == Martix:
			for i in range(self.rank):
				temp.append(self[i] + otehr[i])
		else:
			for i in range(self.rank):
				temp.append(self[i] + otehr)
		return Martix(temp, isextend=self.isextend)

	def __mul__(self, other):
		temp = []
		for i in range(self.rank):
			temp.append(self[i] * other)
		return Martix(temp, isextend=self.isextend)

	def __ne__(self, other):
		for i in range(self.rank):
			if not self.numbers[i] == other.numbers[i]:
				return 1
		return 0

	def __print__(self):
		for i in self:
			print(i)
	
	def assign(self, other):
		self.numbers = other.numbers
		self.isextend = other.isextend
		self.rank = other.rank

	def extend(self, value):
		self.numbers.extend(value)
		self.rank += len(value)
		