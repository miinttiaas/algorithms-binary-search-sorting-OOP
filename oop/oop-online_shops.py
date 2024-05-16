class Shop():
    def __init__(self, shop_name, shop_type,number_of_units = 0):
        self.shop_name = shop_name
        self.number_of_units = number_of_units
        self.shop_type = shop_type
    def describe_shop(self):
        print(self.shop_name, self.shop_type)
    def set_number_of_units(self, number_of_units):
        self.number_of_units = number_of_units
        print(self.number_of_units)
    def increment_number_of_units(self, number_of_increments):
        self.number_of_units += number_of_increments


class Discount(Shop):
    def __init__(self, shop_name, store_type,discount_products = []):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products

    def get_discounts_ptoducts(self):
        print(self.discount_products)

store_discount = Discount("Bobby", 2)

store_discount.set_number_of_units(400)

store_discount.discount_products = ['Bobby', 'Jack']

store_discount.get_discounts_ptoducts()


# rozetka = Shop('Rozetka', shop_type='online_shop')
# rozetka.describe_shop()
#
# jabko = Shop('Jabko', shop_type='electronic_devices_shop')
# jabko.describe_shop()
#
# anika = Shop('Anika', shop_type='electronic_devices_shop')
# anika.describe_shop()
#
# store =Shop('Store', shop_type='electronic_devices_shop', number_of_units=500)
# print(store.number_of_units)
# anika.set_number_of_units(700)
# anika.increment_number_of_units(500)
# print(anika.number_of_units)