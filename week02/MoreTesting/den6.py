import sys


def validate_input(iterable = None ,ascending = True, key = None):

	if not(type(iterable) == list or type(iterable) == tuple or iterable is None):
		raise ValueError('Input has to be list or tuple')

	if not(ascending == True or ascending == False):
		raise ValueError('Input has to be True or False')

	if not(all(type(element) == type(iterable[0]) for element in iterable)):
		raise ValueError('Values in iterable cannot be sorted because they are not of one type')

	if type(iterable) == list and type(iterable[0]) == dict and key == None:
		raise ValueError('A list of dictionaries was given but no key to sort them')

	if type(iterable) == list and type(iterable[0]) == dict and key != None:
		for val in iterable:
			if not(key in val):
				raise ValueError('Not all dictionaries have the given key')


def check_tuple(iterable):
	if type(iterable) == tuple:
		ls = []
		for val in iterable:
			ls.append(val)
		return ls, type(iterable)
	else:
		return iterable, type(iterable)
		

def sorting_alg_tup_list(iterable,ascending,key):
	sorted_iterable = []

	while iterable:
		first = iterable[0]
		for val in iterable:
			if not(ascending):
				if val > first:
					first = val
			else:
				if val < first:
					first = val
		sorted_iterable.append(first)
		iterable.remove(first)

	return sorted_iterable

def sorting_alg_dict(iterable,ascending,key):

	sorted_iterable = []

	while iterable:
		first = iterable[0]
		for vals in iterable:
			if not(ascending):
				if vals[key] > first[key]:
					first = vals
			else:
				if vals[key] < first[key]:
					first = vals
		sorted_iterable.append(first)
		iterable.remove(first)

	return sorted_iterable



def my_sort(iterable = None ,ascending = True, key = None):

	if not iterable:
		return iterable

	validate_input(iterable,ascending,key)

	iterable, type_it = check_tuple(iterable)

	if type(iterable[0]) == dict:
		result = sorting_alg_dict(iterable,ascending,key)
	else:
		result = sorting_alg_tup_list(iterable,ascending,key)

	return type_it(result)



def main():
	print(my_sort())
	

if __name__ == '__main__':
	main()