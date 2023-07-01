from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            # Iniciando variavel msg
            msg = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                # Concatenando sabores ao msg
                msg = f"{msg}\n\t- {flavor}"
            # Troca print -> return
            return msg
        else:
            # Troca print -> return
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                #Troca print -> return / self.flavors -> flavor
                return f"Temos {flavor} no momento!"
            else:
                # Troca print -> return / self.flavors -> flavor
                return f"Não temos {flavor} no momento!"
        else:
            # Troca print -> return
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        #Adicionando validacao de obrigatoriedade de flavor
        if not flavor:
            return "\nValor inválido!"
        # Removido if self.flavors:
        if flavor in self.flavors:
                # Troca print -> return
            return "\nSabor já disponivel!"
        else:
            self.flavors.append(flavor)
               # Troca print -> return
            return f"{flavor} adicionado ao estoque!"
        #Removido o else:
