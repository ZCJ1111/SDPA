import car
import customer


class Rentalshop:

    def __init__(self):
        '''The list which stores the car information'''
        self.inventory = [{'type': 'SUV', 'price1': 100, 'price2': 90, 'stock': 3, 'status':
                           'available'}, {'type': 'sedan', 'price1': 50, 'price2': 40, 'stock': 4, 'status':
                                          'available'}, {'type': 'Hatchbeck', 'price1': 30, 'price2': 25, 'stock': 3, 'status':
                                                         'available'}]

    def rentalPool(self):

        # the method is used for checking the car information
        print(self.inventory)

    def availabitilty(self):
        for i in self.inventory:
            if i['status'] == 'available':
                # to tell customers whether the car they want is available
                print('The car is available.')
            else:
                print('The car is out of stock')

    def totalPrice(self, user):                   # show the total price

        total_price = user.get_bill()
        return total_price
