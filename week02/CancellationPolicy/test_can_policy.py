import unittest
from can_policy import validate_conditions, ensure_conditions, group_conditions


class TestValidateConditions(unittest.TestCase):


	def test_gives_error_if_hours_is_bigger_than_24(self):
		#ARRANGE
		conditions = [{'hours' : 28, 'percent': 20}, {'hours': 20, 'percent' : 30}, {'percent' : 50}]
		exc = None

		#ACT
		try:
			validate_conditions(conditions)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Hours cannot be more than 24')


	def test_gives_error_if_more_than_one_hours_condition_has_value_zero(self):
		#ARRANGE
		conditions = [{'hours' : 22, 'percent': 20}, {'hours': 20, 'percent' : 30}, {'percent' : 50}, {'percent' : 50}]
		exc = None

		#ACT
		try:
			validate_conditions(conditions)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Invalid conditions')


	def test_gives_error_if_all_hours_conditions_have_values_different_than_zero(self):
		#ARRANGE
		conditions = [{'hours' : 22, 'percent': 20}, {'hours' : 21,'percent' : 30}]
		exc = None

		#ACT
		try:
			validate_conditions(conditions)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Invalid conditions')		


class TestEnsureConditions(unittest.TestCase):


	def test_gives_error_if_not_all_conditions_have_hours(self):
		#ARRANGE
		conditions = [{'hours' : 22, 'percent': 20}, {'hours': 20, 'percent' : 30}, {'percent' : 50}]

		#ACT
		ensure_conditions(conditions)

		#ASSERT
		self.assertTrue(all(['hours' in condition for condition in conditions]))


	def test_gives_error_if_more_than_one_hours_condition_has_value_zero(self):
		#ARRANGE
		conditions = [{'hours' : 0, 'percent': 20}, {'hours': 0, 'percent' : 30}, {'hours': 0, 'percent' : 50}, {'hours': 0, 'percent' : 50}]
		exc = None

		#ACT
		try:
			ensure_conditions(conditions)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Invalid conditions')


class TestGroupConditions(unittest.TestCase):


	def test_gives_error_if_conditions_arent_arranged(self):
		#ARRANGE
		conditions = [{'hours' : 23, 'percent': 20}, {'hours': 7, 'percent' : 30}, {'hours': 14, 'percent' : 50}, {'hours': 2, 'percent' : 50}]
		err = None

		group_conditions(conditions)


		for condition in range(len(conditions)):
			try:
				if conditions[condition].get('hours') <= conditions[condition + 1].get('hours'):
					err = 
					
			except:
				pass 



if __name__ == '__main__':
	unittest.main()