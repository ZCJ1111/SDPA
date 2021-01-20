class Car:
    '''This class is created for customers to check the information of car. '''

    def __init__(self, price_of_car=None, type_of_car=None, time_of_renting=None):

        self.price = price_of_car
        self.type = type_of_car
        self.time = time_of_renting

    def car_info(self, type_of_car=None):

        selection = str(input(
            "select the car which you want to rent:\n 1. SUV \n 2. Hatchbeck \n 3.sedan "))

        if selection == '1':

            self.type = 'SUV'
            self.price_info()
        elif selection == '2':
            self.type = 'Hatchbeck'
            self.price_info()

        elif selection == '3':
            self.type = 'sedan'
            self.price_info()
        else:
            print("the number you enter is not valid, please enter again.")

    def price_info(self, price_of_car=None):

        time_of_renting = int(
            input("How many days do you want to rent your car?"))
        if time_of_renting <= 7:
            if self.type == 'SUV':
                price_of_car = 100
                print(
                    "if you choocse ro rent {} car for {} days, the price will be {} pounds per one day!".format(self.type, time_of_renting, price_of_car))
            if self.type == 'Hatchbeck':
                price_of_car = 30
                print(
                    "if you choocse ro rent {} car for {} days, the price will be {} pounds per one day!".format(self.type, time_of_renting, price_of_car))
            if self.type == 'sedan':
                price_of_car = 50
                print(
                    "if you choocse ro rent {} car for {} days, the price will be {} pounds per one day!".format(self.type, time_of_renting, price_of_car))
        else:
            if self.type == 'SUV':
                price_of_car = 90
                print(
                    "if you choocse ro rent {} car for {} days, the price will be {} pounds per one day!".format(self.type, time_of_renting, price_of_car))
            if self.type == 'Hatchbeck':
                price_of_car = 25
                print(
                    "if you choocse ro rent {} car for {} days, the price will be {} pounds per one day!".format(self.type, time_of_renting, price_of_car))
            if self.type == 'sedan':
                price_of_car = 40
                print(
                    "if you choocse ro rent {} car for {} days, the price will be {} pounds per one day!".format(self.type, time_of_renting, price_of_car))
