<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User,AbstractUser
import datetime


# Create your models here.
class Laptop(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    date=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Laptop'
        verbose_name_plural = 'Laptop'
class Desktop(models.Model):
    name=models.CharField(max_length=50)
    prices=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    date=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Desktop'
        verbose_name_plural = 'Desktop'
class Monitor(models.Model):
    name=models.CharField(max_length=50)
    pricess=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    date=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Monitor'
        verbose_name_plural = 'Monitor'
class SmartTV(models.Model):
    name=models.CharField(max_length=50)
    pricesss=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    date=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'SmartTV'
        verbose_name_plural = 'SmartTV'
class Others(models.Model):
    name=models.CharField(max_length=50)
    pricesx=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    dates=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Others'
        verbose_name_plural = 'Others'
class AllInOne(models.Model):
    name=models.CharField(max_length=50)
    pricex=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    date=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'AllInOne'
        verbose_name_plural = 'AllInOne'
class Testimony(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media')
    text = models.CharField(max_length=100)
    profession=models.CharField(max_length=50,  default=False)


    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Testimony'
=======
from django.db import models
from django.contrib.auth.models import User,AbstractUser
import datetime


# Create your models here.
class Laptop(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    date=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Laptop'
        verbose_name_plural = 'Laptop'
class Desktop(models.Model):
    name=models.CharField(max_length=50)
    prices=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    date=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Desktop'
        verbose_name_plural = 'Desktop'
class Monitor(models.Model):
    name=models.CharField(max_length=50)
    pricess=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    date=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Monitor'
        verbose_name_plural = 'Monitor'
class SmartTV(models.Model):
    name=models.CharField(max_length=50)
    pricesss=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    date=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'SmartTV'
        verbose_name_plural = 'SmartTV'
class Others(models.Model):
    name=models.CharField(max_length=50)
    pricesx=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    dates=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Others'
        verbose_name_plural = 'Others'
class AllInOne(models.Model):
    name=models.CharField(max_length=50)
    pricex=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media', default='default.jpg',)
    date=models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'AllInOne'
        verbose_name_plural = 'AllInOne'
class Testimony(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media')
    text = models.CharField(max_length=100)
    profession=models.CharField(max_length=50,  default=False)


    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Testimony'
>>>>>>> 5e59e769f249e9ade78b6cfbba69e48ad1ad9dd1
        verbose_name_plural = 'Testimonies'