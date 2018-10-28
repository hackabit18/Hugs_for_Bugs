from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class College(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=20,default="")
    state = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:index')

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='category_image', default='category_image/default-category.png', blank=True, null=True)

    def __str__(self):
        return self.category_name


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE, blank=False, null=True)
    phone = models.CharField(max_length=20)
    img = models.ImageField(upload_to='user_image', default='user_image/user.ico', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=50)
    descripton = models.CharField(max_length=250)
    img = models.ImageField(upload_to='product_image', null=True, default = 'category_image/default-category.png', blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="seller")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="buyer")
    sell = models.BooleanField(default=False)
    price = models.FloatField(default=0.0)
    day_of_return = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.name + '-' + self.category.category_name

    def get_absolute_url(self):
        return reverse('product:index') #user_page

class Wisher(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

class ReportedAd(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product.name

class Buy(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)