from django.db import models
from .entites import Category, Coin, Account, TypeAccount

class ModelCoin(models.Model):
    coin = models.CharField(max_length=50, verbose_name='Moeda', unique=True)
    country = models.CharField(max_length=3, verbose_name='País', unique=True)
    symbol = models.CharField(max_length=3, verbose_name='Símbolo', unique=True)

    class Meta:
        verbose_name_plural = 'Moeda'
        ordering = ['coin']
        db_table = 'coin'
    
    def __str__(self):
        return self.coin
    
    def save(self):
        coin = Coin(self.coin, self.country, self.symbol)
        self.coin = coin.coin
        self.country = coin.country
        self.symbol = coin.symbol
        return super().save()


class ModelTypeAccount(models.Model):
    type = models.CharField(max_length=50, verbose_name='Tipo da Conta', unique=True)
    description = models.TextField(max_length=200, verbose_name='Descrição', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tipo de conta'
        ordering = ['type']
        db_table = 'tipo_conta'
    
    def __str__(self):
        return self.type

    def save(self):
        typeAccont = TypeAccount(self.type, self.description)
        self.type = typeAccont.type
        self.description = typeAccont.description
        return super().save()


class ModelAccount(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Nome')
    coin = models.ForeignKey(ModelCoin, on_delete=models.CASCADE, verbose_name='Moeda', 
                             related_name='coins_account')
    number = models.IntegerField(verbose_name='Número')
    type = models.ForeignKey(ModelTypeAccount, on_delete=models.CASCADE, verbose_name='Tipo de Conta')
    operation = models.CharField(max_length=50, verbose_name="Operação", choices=Account.type_operation())
    description = models.TextField(max_length=200, verbose_name='Descrição', blank=True, null=True)

    class Meta:
        ordering = ['operation']
        verbose_name_plural = 'Contas'
        db_table='contas'
    
    def __str__(self):
        return self.name
    
    def save(self):
        account = Account(self.name, self.coin, self.number, 
                          self.type, self.operation, self.description)
        self.name = account.name
        self.coin = account.coin
        self.number = account.number
        self.type = account.type
        self.operation = account.operation
        self.description = account.description
        return super().save()
    
class ModelCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Categoria')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categoria'
        db_table ='Category'

    def __str__(self):
        return self.name
    
    def save(self):
        cat = Category(self.name)
        self.name = cat.name
        return super().save()