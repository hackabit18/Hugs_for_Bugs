from django.contrib import admin
from .models import Category, State, Product, UserDetails,Wisher,ReportedAd,Buy
# Register your models here.

admin.site.register(Category)
admin.site.register(State)
admin.site.register(Product)
admin.site.register(UserDetails)
admin.site.register(Wisher)
admin.site.register(ReportedAd)
admin.site.register(Buy)