
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
        
