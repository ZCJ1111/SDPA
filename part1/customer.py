import car
import rentalshop
shop_instance = rentalshop.Rentalshop()


class Customers:
    '''create Customers class include property and behaviour of customer.'''

    def __init__(self, car=None, days=None, price=None, quantity=None):
        self.quantity = quantity
        self.days = days
        self.price = price
        self.car = car

    def all_cars(self):                   # this shows the information of all cars
        print(shop_instance.rentalPool())

    def rent_car(self):

        print('we provide 3 types of car: SUV, sedan and Hatchbeck.')
        while(True):
            # ask user to input the car they want to rent
            get_car = input(
                'please enter which type of car you want to rent:\n')
            all_car_type = ["SUV", "sedan", "Hatchbeck"]
            if get_car not in all_car_type:
                print('Sorry, we have not found the car you want.')
                continue
            self.car = get_car
            for i in shop_instance.inventory:
                if i['type'] == get_car:
                    if i['status'] == 'available':
                        # ask the user input the number of cars they want to rent
                        self.quantity = int(
                            input('How many {} cars you want to rent?'.format(get_car)))
                        if i['stock'] < self.quantity:
                            print("cars are not enough")
                        elif i['stock'] == self.quantity:
                            print("you have successfully rented {} cars".format(
                                self.quantity))
                            # update status of car if there is nothing left
                            i['status'] = 'out of stock'
                        else:
                            print("you have successfully rented {} cars".format(
                                self.quantity))
                            i['stock'] -= self.quantity

                        # ask the user to input the renting days they need
                        self.days = int(
                            input('How many days you want to rent?'))

                        if self.days <= 7:  # price is set to be different for different period
                            self.price = i['price1']
                        else:
                            self.price = i['price2']
                        print("You have rented {} {} cars for {} days. \n You will be charged {} pounds per one day, We hope that you enjoy our service."
                              .format(self.quantity, self.car, self.days, self.price))

                    else:
                        print('Your car is currently out of stock')
            break

    def give_back(self):  # update the status and stock of cars when customer return them

        for i in shop_instance.inventory:
            if i['type'] == self.car:
                if i['status'] == 'out of stock':
                    i['status'] = 'available'
                    i['stock'] += self.quantity

                else:
                    i['stock'] += self.quantity
                print("you have successfully returned the {} car.".format(self.car))

    def get_bill(self):  # show customer the bill when they return the cars

        bill = self.days*self.quantity*self.price
        print("Total payment is £{}".format(bill))
        return bill
