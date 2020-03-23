import unittest
from den6_2 import validate_input_for_simplify_fractions, simplify_fraction, greatest_div, validate_input_for_collect_and_sort_fractions, sum_them_up, collect_fractions, find_simplest_one, sorter_alg


class TestValidateInputForSimplifyFractions(unittest.TestCase):


	def test_if_len_of_input_is_two(self):
		inputs = (3,5,6)
		exc = None

		try:
			validate_input_for_simplify_fractions(inputs)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Input only two numbers')


	def test_if_values_in_input_are_integers(self):
		inputs = (23.4,123)
		exc = None

		try:
			validate_input_for_simplify_fractions(inputs)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Input two integers divided by a coma')


	def test_if_values_are_in_a_tuple(self):
		inputs = [4,5]
		exc = None

		try:
			validate_input_for_simplify_fractions(inputs)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Values must be in tuple')


	def test_if_secound_value_is_zero(self):
		inputs = (4,0)
		exc = None

		try:
			validate_input_for_simplify_fractions(inputs)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Cannot divide by zero or less')



class TestGreatestDiv(unittest.TestCase):


	def test_if_returns_greatest_divisor(self):
		inputs = (64,32)

		res = greatest_div(inputs)

		expected = 32

		self.assertEqual(res,expected)



class TestFindSimplestOne(unittest.TestCase):


	def test_if_input_is_simplified(self):
		inpts = (462,63)

		res = find_simplest_one(inpts)

		expected = (22,3)

		self.assertEqual(res,expected)




class TestValidateInputForCollectFractions(unittest.TestCase):



	def test_check_if_list_of_tuples_is_given(self):
		inputs = [(3,4),'kaval']
		err = None

		try:
			validate_input_for_collect_and_sort_fractions(inputs)
		except Exception as exc:
			err = exc

		self.assertIsNotNone(err)
		self.assertEqual(str(err),'Input must be a list of tuples with values')



	def test_if_all_values_in_tuple_are_integers(self):
		inputs = [(3,4),(2.4,5)]
		err = None 


		try:
			validate_input_for_collect_and_sort_fractions(inputs)
		except Exception as exc:
			err = exc

		self.assertIsNotNone(err)
		self.assertEqual(str(err),'All values in the tuples must be integers')


	def test_if_all_values_are_greater_than_zero(self):
		inputs = [(3,4),(5,-3)]
		err = None

		try:
			validate_input_for_collect_and_sort_fractions(inputs)
		except Exception as exc:
			err = exc

		self.assertIsNotNone(err)
		self.assertEqual(str(err),'All denominators cannot be less than 1')


	def test_if_each_tuple_has_exactly_two_values(self):
		inputs = [(3,4),(5,3,3)]
		err = None

		try:
			validate_input_for_collect_and_sort_fractions(inputs)
		except Exception as exc:
			err = exc

		self.assertIsNotNone(err)
		self.assertEqual(str(err),'Input two integers divided my a coma')

class TestSumThemUp(unittest.TestCase):


	def test_if_summing_is_right(self):
		inputs = [(1,7),(2,6)]

		res = sum_them_up(inputs)

		expected = (20,42)

		self.assertEqual(res,expected)



class TestCollectFractions(unittest.TestCase):


	def test_if_fractions_are_collected_and_simplifed(self):
		inputs = [(1,4),(1,2),(4,5)]

		res = collect_fractions(inputs)

		expected = (31,20)

		self.assertEqual(res,expected)



class TestSorterAlg(unittest.TestCase):


	def testi_if_sorting_correctly(self):
		inputs = [(5,6),(22,7),(22,78),(7,8),(9,6),(15,32)]

		res = sorter_alg(inputs)

		expected = [(22,78),(15,32),(5,6),(7,8),(9,6),(22,7)]

		self.assertEqual(res,expected)

if __name__ == '__main__':
	unittest.main()