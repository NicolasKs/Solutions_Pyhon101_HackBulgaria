import sys

class Bill:

	def __init__(self,amount):
		if amount <= 0 :
			raise ValueError('Money must be positive yo')
		if type(amount) != int:
			raise TypeError('Only full cash no stotinki')
		self.amount = amount

	def __str__(self):
		return f'A {self.amount}$ bill.'

	def __repr__(self):
		return f'A {self.amount}$ bill.'

	def __int__(self):
		return self.amount

	def __eq__(self,other):
		return self.amount == other.amount


	def __hash__(self):
		return hash(self.amount)


class BillBatch:

	def __init__(self,list_bills):
		self.list_bills = list_bills


	def __len__(self):
		return len(self.list_bills)


	def __getitem__(self, position):
		return self.list_bills[position]


	def total(self):
		return sum([int(bill) for bill in self.list_bills])


class CashDesk:


	def __init__(self):
		self.desk = []


	def __getitem__(self, position):
		return self.desk[position]


	def take_money(self,bills):
		if type(bills) == Bill:
			self.desk.append(bills)
		elif type(bills) == BillBatch:
			self.desk += bills
		else:
			raise TypeError('Given data is not in Bills or Batch')

	def total(self):
		return sum([int(bills) for bills in self.desk])

	def inspect(self):
		bill_amounts = {}

		for bills in self.desk:
			if bills not in bill_amounts:
				bill_amounts[bills] = 1
			elif bills in bill_amounts:
				bill_amounts[bills] += 1

		for bills,nums in bill_amounts.items():
			print(bills,nums)

		


def main():
	pass
	# desk = CashDesk()

	# desk.take_money(Bill(10))




if __name__ == '__main__':
	main()