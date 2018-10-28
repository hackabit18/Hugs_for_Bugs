from django.contrib import admin
from .models import Category, College, Product, UserDetails,Wisher,ReportedAd,Buy
# Register your models here.

admin.site.register(Category)
admin.site.register(College)
admin.site.register(Product)
admin.site.register(UserDetails)
admin.site.register(Wisher)
admin.site.register(ReportedAd)
admin.site.register(Buy)