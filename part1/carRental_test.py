import unittest
import customer


class Test(unittest.TestCase):
    '''Test the customer class'''

    def setUp(self):
        self.user = customer.Customers()
        if self.user.price == None:
            self.user.price = 10
        if self.user.days == None:
            self.user.days = 5
        if self.user.quantity == None:
            self.user.quantity = 8

    def test_rent_car(self):  # test rent_car method
        self.assertEqual(self.user.rent_car(), None,
                         "The test of the function of rent_car fail!")

    def test_return_car(self):  # test the give_back method
        self.assertEqual(self.user.give_back(), None,
                         "The test of the function of return_car fail!")

    def test_get_bill(self):  # test the get_bill method
        self.assertEqual(self.user.get_bill(), self.user.days*self.user.quantity*self.user.price,
                         "The test of the function of return_car fail!")


if __name__ == '__main__':
    unittest.main()
