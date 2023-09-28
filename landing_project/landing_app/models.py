from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name='User ismi')
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=500, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name="foydalanuvchi"


class Sardor(models.Model):
    ism = models.CharField(max_length=255, verbose_name='Ismi')
    description = models.TextField(verbose_name="Ma'lumot")



# Create your models here.
