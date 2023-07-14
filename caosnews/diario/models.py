from django.db import models
# Create your models here.

class AreaCategoria(models.Model):
    idCategoria         = models.AutoField(db_column='idCategoria', primary_key=True) 
    nombreCategoria     = models.CharField(max_length=30, blank=False, null=False)

    def str(self):
        return str(self.nombreCategoria)
    
   
    
class noticias(models.Model):
    idCategoria      = models.ForeignKey('AreaCategoria',on_delete=models.CASCADE, db_column='idCategoria', verbose_name='idCategoria') 
    codigo           = models.CharField(primary_key=True, max_length=6, verbose_name='codigo')
    nombre           = models.CharField(max_length=50, verbose_name='nombre')
    fecha            = models.CharField(max_length=10, null=True, verbose_name='fecha')
    titulo           = models.CharField(max_length=50, verbose_name='titulo')
    cuerpo           = models.CharField(max_length=600, verbose_name='Cuerpo')
    Img              = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='img')

    def str(self):
        return str(self.nombre)
    class Meta:
        ordering = ['nombre']

    def delete(self, using=None, keep_parents=False):
        self.Img.storage.delete(self.Img.name)
        return super().delete()