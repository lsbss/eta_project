from src.models.ice_cream_stand import IceCreamStand
from unittest import TestCase


class TestIceCreamStand(TestCase):

    def test_flavors_available(self):
        result = '\nNo momento temos os seguintes sabores de sorvete disponíveis:\n\t- Morango\n\t- Uva\n\t- Tamarindo'

        ic_stand = IceCreamStand('Sol de Verao', 'paleta', ['Morango', 'Uva', 'Tamarindo'])

        found_result = ic_stand.flavors_available()
        self.assertEqual(result, found_result)

    def test_flavors_available_not_found(self):
        result = 'Estamos sem estoque atualmente!'
        ic_stand = IceCreamStand('Sol de Verao', 'paleta', [])

        found_result = ic_stand.flavors_available()
        self.assertEqual(result, found_result)

    def test_find_flavor(self):
        flavor = 'Morango'
        result = f"Temos {flavor} no momento!"

        ic_stand = IceCreamStand('Sol de Verao', 'paleta', ['Morango', 'Uva', 'Tamarindo'])

        found_result = ic_stand.find_flavor(flavor=flavor)
        self.assertEqual(result, found_result)

    def test_find_flavor_not_found(self):
        flavor = 'Jaca'
        result = f'Não temos {flavor} no momento!'

        ic_stand = IceCreamStand('Sol de Primavera', 'paleta', ['Morango', 'Uva', 'Tamarindo'])

        found_result = ic_stand.find_flavor(flavor=flavor)
        self.assertEqual(result, found_result)

    def test_find_flavor_not_stock(self):
        flavor = 'Jaca'
        result = 'Estamos sem estoque atualmente!'

        ic_stand = IceCreamStand('Sol de Verao', 'paleta', [])

        found_result = ic_stand.find_flavor(flavor=flavor)
        self.assertEqual(result, found_result)

    def test_add_flavor(self):
        flavor = 'Jaca'
        result = f'{flavor} adicionado ao estoque!'

        ic_stand = IceCreamStand('Sol de Verao', 'paleta', ['Morango', 'Uva', 'Tamarindo'])

        found_result = ic_stand.add_flavor(flavor=flavor)
        self.assertEqual(result, found_result)

    def test_add_flavor_existing_flavor(self):
        flavor = 'Uva'
        result = '\nSabor já disponivel!'

        ic_stand = IceCreamStand('Sol de Verao', 'paleta', ['Morango', 'Uva', 'Tamarindo'])

        found_result = ic_stand.add_flavor(flavor=flavor)
        self.assertEqual(result, found_result)

    def test_add_flavor_no_stock(self):
        flavor = 'Uva'
        result = f'{flavor} adicionado ao estoque!'

        ic_stand = IceCreamStand('Sol de Verao', 'paleta', [])

        found_result = ic_stand.add_flavor(flavor=flavor)
        self.assertEqual(result, found_result)

    def test_add_flavor_no_flavor_value(self):
        flavor = ''
        result = '\nValor inválido!'

        ic_stand = IceCreamStand('Sol de Verao', 'paleta', [])

        found_result = ic_stand.add_flavor(flavor=flavor)
        self.assertEqual(result, found_result)
