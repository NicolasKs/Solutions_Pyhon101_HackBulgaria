import sys


def validate_input_for_simplify_fractions(fraction):
	if len(fraction) != 2:	
		raise ValueError('Input only two numbers')

	if any((type(i) != int for i in fraction)):
		raise ValueError('Input two integers divided by a coma')

	if type(fraction) != tuple:
		raise ValueError('Values must be in tuple')

	if fraction[1] < 1:
		raise ValueError('Cannot divide by zero or less')


def validate_input_for_collect_and_sort_fractions(fractions):
	if type(fractions) != list or any(type(i) != tuple for i in fractions):
		raise ValueError('Input must be a list of tuples with values')

	for tups in fractions:
		if len(tups) != 2:
			raise ValueError('Input two integers divided my a coma')

		if any((type(vals) != int for vals in tups)):
			raise ValueError('All values in the tuples must be integers')

		if tups[1] < 1:
			raise ValueError('All denominators cannot be less than 1')


def greatest_div(fraction):
	n = fraction[0]
	d = fraction[1]
	while d != 0:
		t = d
		d = n%d
		n = t
	return n


def sum_them_up(fractions):
	n = 0
	d = 0
	for tups in fractions:
		if n == 0 and d == 0:
			n = tups[0]
			d = tups[1]
			continue
		n = n * tups[1] + d * tups[0]
		d *= tups[1]

	return (int(n),int(d))


def find_simplest_one(fraction):
	greatest = greatest_div(fraction)

	nom = fraction[0] / greatest
	denom = fraction[1] / greatest

	return (int(nom),int(denom))


def sorter_alg(fraction):
	sorted_fractions = []

	while fraction:
		first = fraction[0]
		for tup in fraction:
			if tup[0] / tup[1] < first[0] / first[1]:
				first = tup
		sorted_fractions.append(first)
		fraction.remove(first)

	return sorted_fractions


def simplify_fraction(fraction):
	validate_input_for_simplify_fractions(fraction)

	return find_simplest_one(fraction)


def collect_fractions(fractions):
	validate_input_for_collect_and_sort_fractions(fractions)

	summed = sum_them_up(fractions)

	return find_simplest_one(summed)


def sort_fractions(fractons):
	validate_input_for_collect_and_sort_fractions(fractions)

	return sorter_alg(fractions)


def main():
	print(simplify_fraction((462,63)))
	print(collect_fractions([(1,7),(2,6)]))
	print(sort_fractions([(5,6),(22,7),(22,78),(7,8),(9,6),(15,32)]))


if __name__ == '__main__':
	main()