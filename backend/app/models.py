from django.db import models


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

class ModelTypeAccount(models.Model):
    type = models.CharField(max_length=50, verbose_name='Tipo da Conta', unique=True)
    description = models.TextField(max_length=200, verbose_name='Descrição', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tipo de conta'
        ordering = ['type']
        db_table = 'tipo_conta'
    
    def __str__(self):
        return self.type

class ModelAccount(models.Models):
    CONTAS = (('ativos', 'Ativos'), 
              ('despesas', 'Despesas',
               'receitas', 'Receitas', 
               'passivos', 'Passivos'))
    
    name = models.CharField(max_length=100, verbose_name='Nome')
    coin = models.ForeignKey(ModelCoin, on_delete=models.CASCADE, verbose_name='Moeda', 
                             related_name='coins')
    number = models.IntegerField(verbose_name='Número')
    type = models.ForeignKey(ModelTypeAccount, on_delete=models.CASCADE, verbose_name='Tipo de Conta')
    operation = models.CharField(max_length=50, verbose_name="Operação", choices=CONTAS)
    description = models.TextField(max_length=200, verbose_name='Descrição', blank=True, null=True)

    class Meta:
        ordering = ['operation']
        verbose_name_plural = 'Contas'
        db_table='contas'
    
    def __str__(self):
        return self.name
    
class ModelCategory(models.model):
    name = models.CharField(max_length=50, verbose_name='Categoria')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categoria'
        db_table ='Category'

    def __str__(self):
        return self.name
    
class ModelOperations(models.Model):
    name = models.CharField(max_length=70, verbose_name='Nome')
    accont_origin = models.ForeignKey(ModelAccount, on_delete=models.CASCADE, 
                                      verbose_name='Conta origem', related_name='origin')
    accont_destination = models.ForeignKey(ModelAccount, on_delete=models.CASCADE, 
                                           verbose_name='Conta destino', related_name='destination')
    date = models.DateTimeField(verbose_name='Data')
    value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')
    coin = models.ForeignKey(ModelCoin, on_delete=models.CASCADE,
                             verbose_name='Moeda', related_name='coins')
    category = models.ForeignKey(ModelCategory, on_delete=models.CASCADE, 
                                 verbose_name='Categoria', related_name='categorys')
    invoice = models.DateField(verbose_name='Data da Fatura')
    note = models.IntegerField(verbose_name='Numero da Nota')
    
    
class Imagens
    
