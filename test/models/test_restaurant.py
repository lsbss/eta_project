from src.models.restaurant import Restaurant
from unittest import TestCase


class TestRestaurant(TestCase):

    def test_describe_restaurant(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 1000
        is_open = True
        result = f'Esse restaturante se chama {restaurant} e serve comida {cuisine_type}.' \
                 f'\nEsse restaturante está servindo {number_served} consumidores desde que está aberto.'

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        found_result = restaurant.describe_restaurant()

        self.assertEqual(result, found_result)

    def test_open_restaurant(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 1000
        is_open = False
        result = f'{restaurant} agora está aberto!'

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        found_result = restaurant.open_restaurant()

        self.assertEqual(result, found_result)

    def test_open_restaurant_validate_change_status(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 1
        is_open = False
        result = True

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        restaurant.open_restaurant()
        found_result = restaurant.open

        self.assertEqual(result, found_result)

    def test_open_restaurant_validate_number_server(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 123
        is_open = False
        result = 0

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        restaurant.open_restaurant()
        found_result = restaurant.number_served

        self.assertEqual(result, found_result)

    def test_open_restaurant_is_open(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 1000
        is_open = True
        result = f'{restaurant} já está aberto!'

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        found_result = restaurant.open_restaurant()

        self.assertEqual(result, found_result)

    def test_close_restaurant(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 1000
        is_open = True
        result = f'{restaurant} agora está fechado!'

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        found_result = restaurant.close_restaurant()

        self.assertEqual(result, found_result)

    def test_close_restaurant_closed(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 1000
        is_open = False
        result = f'{restaurant} já está fechado!'

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        found_result = restaurant.close_restaurant()

        self.assertEqual(result, found_result)

    def test_close_restaurant_validate_status(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 1000
        is_open = True
        result = False

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        restaurant.close_restaurant()

        found_result = restaurant.open

        self.assertEqual(result, found_result)

    def test_set_number_served(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 1000
        new_number_served = 1002
        is_open = True
        result = 1002

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        restaurant.set_number_served(new_number_served)

        found_result = restaurant.number_served

        self.assertEqual(result, found_result)

    def test_set_number_served_close_restaurant(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 1000
        new_number_served = 1002
        is_open = False
        result = f'{restaurant} está fechado!'

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        found_result = restaurant.set_number_served(new_number_served)

        self.assertEqual(result, found_result)

    def test_increment_number_served(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 1000
        increment = 10
        is_open = True
        result = 1010

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        restaurant.increment_number_served(increment)

        found_result = restaurant.number_served

        self.assertEqual(result, found_result)

    def test_increment_number_served_close_restaurant(self):
        restaurant = 'Comida De Mainha'
        cuisine_type = 'baiana'
        number_served = 1000
        increment = 10
        is_open = False
        result = f'{restaurant} está fechado!'

        restaurant = Restaurant(restaurant, cuisine_type, number_served, is_open)

        found_result = restaurant.increment_number_served(increment)

        self.assertEqual(result, found_result)
