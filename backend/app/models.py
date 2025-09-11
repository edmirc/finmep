from django.db import models
from registers.models import ModelAccount, ModelCoin, ModelCategory

    
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
    
    
class ModelImagens(models.Model):
    operation = models.ForeignKey(ModelOperations, on_delete=models.CASCADE, 
                                  verbose_name='Operação', related_name='photos')
    image = models.ImageField(upload_to='note/', verbose_name='Imagnes')

    class Meta:
        verbose_name_plural = 'Imagens'
        db_table = 'imagens'
    
    def __str__(self):
        return self.operation.name

    
    
