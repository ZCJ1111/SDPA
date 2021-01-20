import os
import sys
import customer
import car
import rentalshop
import VIP


def main():
    # create instance of Customer class, that is user.
    user = customer.Customers()
    # create instance of Car class, that is car.
    car_instance = car.Car()
    # create instance of VIP class, thta is vip.
    vip = VIP.VIP()
    # set customer is not VIP as default.
    vip_customer = False
    # create instance of Rentalshop class, that is shop_instance.
    shop_instance = rentalshop.Rentalshop()

    while(True):
        print("  USE NUMBER TO SELECT ANY THING FROM MENU ")
        print("                                           ")
        print("\t 1.CHECK NUMBER OF TIMES A CAR HAS       ")
        print("\t   BEEN RENTED, AND MONEY MADE FROM IT   ")
        print("\t 2.CHECK THE AVAILABILITY OF CARS        ")
        print("\t 3.RENT A CAR                            ")
        print("\t 4.RETURN THE CAR BACK                    ")
        print("\t 9. I AM VIP                              ")
        print("\t 0.Exit                                   ")

        #prompting user to select one of the menu

        selection = input("Select menu with using number: ")

        if selection == '1':
            user.inquire_info(car_instance)

        elif selection == '2':
            shop_instance.availabitilty()

        elif selection == '3':
            user.rent_car()
        elif selection == '4':
            if vip_customer:
                vip.give_back()
                vip.get_bill()
            else:
                user.give_back()
                user.get_bill()
        elif selection == '9':
            vip.VIP_price()
            vip_customer = True
        elif selection == '0':
            exit_this()
        else:
            #if user doesn't  choose any of above numbers
            print("NO CHOICE WE HAVE THAT LOOK LIKE THAT")
        os.system('pause')


def exit_this():
    exit("THANK YOU FOR USING THIS SOFTWARE SEE YOU!!!")


if __name__ == '__main__':
    main()
