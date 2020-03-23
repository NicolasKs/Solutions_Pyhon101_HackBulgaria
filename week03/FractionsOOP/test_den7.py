import unittest 
from den7 import Fraction, sorting




class TestFraction(unittest.TestCase):


	def test_err_if_denominator_is_zero_or_negative(self):
		exc = None

		try:
			Fraction(1,0)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Denominator can`t be zero or negative')


	def test_if_representation_is_as_expected(self):
		fraction1 = Fraction(1,3)
		

		self.assertEqual(str(fraction1),'1/3')


	def test_if_fraction_is_simplified(self):
		fraction1 = Fraction(1,3)
		fraction2 = Fraction(3,9)

		self.assertEqual(fraction1.simplification(),fraction2.simplification())


	def test_if_fractions_are_equal(self):
		fraction1 = Fraction(1,3)
		fraction2 = Fraction(1,3)

		self.assertEqual(fraction1,fraction2)

	def test_if_addition_fraction_works(self):
		fraction1 = Fraction(1,5)
		fraction2 = Fraction(2,5)
		fraction3 = Fraction(1,7)
		fraction4 = Fraction(2,5)

		result = fraction1 + fraction2 
		result1 = fraction3 + fraction4

		self.assertEqual(result.numerator,3)
		self.assertEqual(result.denominator,5)
		
		self.assertEqual(result1.numerator,19)
		self.assertEqual(result1.denominator,35)


class TestSorting(unittest.TestCase):


	def test_if_sorting_works(self):

		fraction1 = Fraction(1,5)
		fraction2 = Fraction(2,5)
		fraction3 = Fraction(3,5)

		ls = [fraction3,fraction1,fraction2]

		res = sorting(ls)

		expected = [fraction1,fraction2,fraction3]	

		self.assertEqual(res,expected)






if __name__ == '__main__':
	unittest.main()