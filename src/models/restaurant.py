class Restaurant:
    """Model de restaurante simples."""

# Adicionando novos parametros ao construtor
    def __init__(self, restaurant_name, cuisine_type, number_served=0, is_open=True):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        self.open = is_open

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        #Trocando print -> return
        #ajuste na mensagem de retorno
        msg = f"Esse restaturante se chama {self.restaurant_name} e serve comida {self.cuisine_type}." \
              f"\nEsse restaturante está servindo {self.number_served} consumidores desde que está aberto."
        return msg

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            #Trocar False por True
            self.open = True
            # alteracao de number_served para 0
            self.number_served = 0
            # Trocando print -> return
            return f"{self.restaurant_name} agora está aberto!"
        else:
            # Trocando print -> return
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            #self.number_served = 0
            # Trocando print -> return
            return(f"{self.restaurant_name} agora está fechado!")
        else:
            # Trocando print -> return
            return(f"{self.restaurant_name} já está fechado!")

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
        else:
            # Trocando print -> return
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            #Troca atribuicao por incremento
            self.number_served = self.number_served + more_customers
        else:
            # Trocando print -> return
            return f"{self.restaurant_name} está fechado!"
