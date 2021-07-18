from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to = 'products', default = 'no_picture.png')
    price = models.FloatField(help_text='in USD')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}-{self.created.strftime('%d/%m/%Y')}"
