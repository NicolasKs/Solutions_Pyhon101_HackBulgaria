import sys
import unittest
from cashdesk import Bill, BillBatch, CashDesk


class TestBill(unittest.TestCase):


	def test_if_bill_is_non_negative_or_zero(self):
		err = None

		try:
			bill1 = Bill(-5)
		except Exception as exc:
			err = exc
		
		self.assertIsNotNone(err)
		self.assertEqual(str(err),'Money must be positive yo')


	def test_if_bill_is_integer(self):
		err = None

		try:
			bill1 = Bill(1.5)
		except Exception as exc:
			err = exc

		self.assertIsNotNone(err)
		self.assertEqual(str(err),'Only full cash no stotinki')


	def test_if_str_representataion_is_as_expected(self):
		bill1 = Bill(10)
		bill2 = Bill(5)


		self.assertEqual(str(bill1),'A 10$ bill.')
		self.assertEqual(str(bill2),'A 5$ bill.')


	def test_if_int_representation_is_as_expected(self):
		bill1 = Bill(15)


		self.assertEqual(int(bill1),15)


	def test_if_two_values_are_equal(self):
		bill1 = Bill(5)
		bill2 = Bill(5)

		self.assertTrue(bill1 == bill2,'Values are not equal')


	def test_if_hash_representataion_is_as_expected(self):
		bill1 = Bill(5)
		bill2 = Bill(5)

		
		self.assertEqual(hash(bill1),hash(bill2))

class TestBillBatch(unittest.TestCase):


	def test_len_of_bills_in_batch(self):
		ls = [10,20,50,100]
		bills = [Bill(value) for value in ls]

		batch = BillBatch(bills)

		self.assertEqual(len(batch),4)

	def test_if_batch_is_iterable_in_for_loop(self):
		ls = [10,20,50,100]
		bills = [Bill(value) for value in ls]

		batch = BillBatch(bills)

		self.assertTrue([i for i in batch])


	def test_if_totall_batch_is_working(self):
		ls = [10,20,50,100]
		bills = [Bill(value) for value in ls]
		exp = 180


		batch = BillBatch(bills)
		res = batch.total()

		self.assertEqual(res,exp)

class TestCashDesk(unittest.TestCase):


	def test_if_bills_are_taken_from_desk(self):
		desk = CashDesk()

		ls = [10,20,50,100]
		bills = [Bill(value) for value in ls]

		batch = BillBatch(bills)

		desk.take_money(Bill(10))
		desk.take_money(batch)

		self.assertEqual(str(desk[0]),'A 10$ bill.')
		self.assertEqual(str(desk[3]),'A 50$ bill.')


	def test_if_totall_sum_is_right(self):
		desk = CashDesk()
		exp = 190
		ls = [10,20,50,100]
		bills = [Bill(value) for value in ls]

		batch = BillBatch(bills)

		desk.take_money(Bill(10))
		desk.take_money(batch)
		res = desk.total()


		self.assertEqual(res, exp)


	def test_if_inspection_works(self):
		desk = CashDesk()
		ls = [10,20,50,100]
		bills = [Bill(value) for value in ls]

		batch = BillBatch(bills)

		desk.take_money(Bill(10))
		desk.take_money(batch)

		desk.inspect()








if __name__ == '__main__':
	unittest.main()