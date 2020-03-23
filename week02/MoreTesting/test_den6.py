import unittest
from den6 import my_sort, validate_input, check_tuple, sorting_alg_tup_list, sorting_alg_dict


class TestValidateInput(unittest.TestCase):


	def test_if_input_iterable_is_list_or_tuple(self):
		iterable = 12345
		exc = None

		try:
			validate_input(iterable)
		except Exception as err:
			exc = err


		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Input has to be list or tuple')


	def test_if_input_ascending_is_True_or_False(self):
		inputs = 'kaval'
		exc = None

		try:
			validate_input(ascending = inputs)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Input has to be True or False')


	def test_if_all_values_in_iterable_are_same(self):
		iterable = [1,2,3,4,'kaval']
		exc = None

		try:
			validate_input(iterable)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Values in iterable cannot be sorted because they are not of one type')


	def test_if_key_was_given_if_iterable_was_list_of_dicitionaries(self):
		iterable = [{'name': 'Ivan','age' : 23}, {'name': 'Dragan','age' : 1}, {'name': 'Kazan','age' : 54}]
		exc = None

		try:
			validate_input(iterable)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'A list of dictionaries was given but no key to sort them')

	def test_if_key_is_present_in_all_given_dictionaries(self):
		iterable = [{'name': 'Ivan','age' : 23}, {'name': 'Dragan','age' : 1}, {'name': 'Kazan'}]
		exc = None

		try:
			validate_input(iterable,key = 'age')
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Not all dictionaries have the given key')




class TestCheckTuple(unittest.TestCase):


	def test_if_vals_in_list_are_same_as_vals_in_given_tuple(self):
		iterable = (1,6,3,2,1,6,9,4,2,5,79)

		result, type_it = check_tuple(iterable)

		ls = [1,6,3,2,1,6,9,4,2,5,79]
		type_expected = tuple

		self.assertEqual(result,ls)
		self.assertEqual(type_it,type_expected)



class TestSortingAlgTupleList(unittest.TestCase):


	def test_if_iterable_is_sorted(self):
		iterable = [5,2,9,1,20,40,1]

		result = sorting_alg_tup_list(iterable,True,key = None)

		sorted_iterable = [1,1,2,5,9,20,40]

		self.assertEqual(result,sorted_iterable)


	def test_if_iterable_is_sorted_by_val_of_ascending(self):
		iterable = [5,2,9,1,20,40,1]

		result = sorting_alg_tup_list(iterable,False,key = None)

		sorted_iterable = [40,20,9,5,2,1,1]

		self.assertEqual(result,sorted_iterable)


class TestSortingAlgDictionary(unittest.TestCase):


	def test_if_dictionary_is_sorted_by_given_key(self):
		iterable = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]

		result = sorting_alg_dict(iterable,True,key = 'age')

		sorted_dic = [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]

		self.assertEqual(result,sorted_dic)


class TestMySort(unittest.TestCase):


	def test_if_given_iterable_is_empty(self):
		iterable = []

		result = my_sort(iterable)

		expected_output = []

		self.assertEqual(result,expected_output)


	def test_if_function_is_called_empty(self):

		result = my_sort()

		self.assertEqual(result,None)



if __name__ == '__main__':
	unittest.main()