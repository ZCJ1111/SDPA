from customer import Customers
import rentalshop
shop_instance = rentalshop.Rentalshop()


class VIP(Customers):
    '''create a VIP class, which inherits from Custmers class'''

    def __init__(self, car=None, days=None, price=None, quantity=None):

        # inherit property from class Custmore
        super().__init__(car, days, price, quantity)

    def VIP_price(self):

        # set the VIP price  and update this into inventory
        for i in shop_instance.inventory:
            if i['type'] == 'SUV':
                self.price = 80
                i['price1'] = i['price2'] = self.price
            if i['type'] == 'sedan':
                self.price = 35
                i['price1'] = i['price2'] = self.price
            if i['type'] == 'Hetchback':
                self.price = 20
                i['price1'] = i['price2'] = self.price
        update_inventory = shop_instance.inventory

        print('we provide 3 types of car: SUV, sedan and Hatchbeck.')
        while(True):
            get_car = input(
                'please enter which type of car you want to rent:\n')
            all_car_type = ["SUV", "sedan", "Hatchbeck"]
            if get_car not in all_car_type:
                print('Sorry, we have not found the car you want.')
                continue
            self.car = get_car
            for i in update_inventory:
                if i['type'] == get_car:
                    if i['status'] == 'available':
                        self.quantity = int(
                            input('How many {} cars you want to rent?'.format(get_car)))
                        if i['stock'] < self.quantity:
                            print("cars are not enough")
                        elif i['stock'] == self.quantity:
                            print("you have successfully rented {} cars".format(
                                self.quantity))
                            i['status'] = 'out of stock'
                        else:
                            print("you have successfully rented {} cars".format(
                                self.quantity))
                            i['stock'] -= self.quantity

                        self.days = int(
                            input('How many days you want to rent?'))

                        if self.days <= 7:
                            self.price = i['price1']
                        else:
                            self.price = i['price2']
                        print("You have rented {} {} cars for {} days. \n You will be charged {} pounds per one day, We hope that you enjoy our service."
                              .format(self.quantity, self.car, self.days, self.price))

                    else:
                        print('Your car is currently out of stock')
            break

    def give_back(self):  # The give_back and get_bill methods are the same as customer class
        super().give_back()

    def get_bill(self):
       super().get_bill()
