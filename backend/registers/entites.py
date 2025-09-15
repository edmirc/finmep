
class Category:

    def __init__(self, name: str):
        name = name.title().strip()
        self.name = name

    def getName(self):
        return self.name


class Coin:

    def __init__(self, coin: str, country: str, symbol: str):
        self.coin = coin.title().strip()
        self.country = country.upper().strip()
        self.symbol = symbol.upper().strip()


class TypeAccount:

    def __init__(self, type: str, description: str):
        self.type = type.title()
        self.description = description.title()


class Account:

    def __init__(self, name: str, coin: Coin, number: int, 
                 type: TypeAccount, operation: str, descriptrion: str):
        self.name = name.title()
        self.coin = coin
        self.number = number
        self.type = type
        self.operation = operation
        self.description = descriptrion.title()
    
    @classmethod
    def type_operation(sefl) -> tuple:
        return (('ativos', 'Ativos'), 
              ('despesas', 'Despesas'),
               ('receitas', 'Receitas'), 
               ('passivos', 'Passivos'))
