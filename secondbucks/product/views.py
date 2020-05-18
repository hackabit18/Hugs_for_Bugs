from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, State, Product, UserDetails, Wisher, ReportedAd
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import UserSignupForm, UserDetailsForm, SellProductRegistrationForm, ShareProductRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .serializers import StateSerializer
from django.core import serializers
import json
from datetime import datetime, timedelta

def index(request):
    if request.method == 'POST':
        state_name = request.POST.get("myCountry")
        state_id = State.objects.get(name=state_name)
        return redirect('product:categories', state_id=state_id.pk)

    states = State.objects.all()
    return render(request, 'index.html', {'states': states})


def category_list(request, state_id):
    categories = Category.objects.all()
    state = State.objects.get(pk=state_id)
    return render(request, 'category/categories.html', {'categories': categories, 'state': state})


def category_wise(request, state_id, category_id):
    state = State.objects.get(pk=state_id)
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(state=state, category=category)
    return render(request, 'category/category_wise.html', {'products': products, 'state': state, 'category': category})


def product_details(request, state_id, category_id, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product/product_details.html', {'product': product})
    

class RegisterState(CreateView):
        model = State
        fields = ['name', 'city', 'state']


def add_product(request):
    return render(request, 'product/add_product.html')

def RegisterSellProduct(request):
    form = SellProductRegistrationForm()

    if request.method == 'GET':
        return render(request, 'product/product_form.html', {'form': form})
    
    if request.method =='POST':
        form = SellProductRegistrationForm(request.POST)
        if form.is_valid():
            temp = Product()
            temp.img = form.cleaned_data['img']
            temp.name = form.cleaned_data['name']
            temp.descripton = form.cleaned_data['descripton']
            temp.category = form.cleaned_data['category']
            temp.state = form.cleaned_data['state']
            temp.price = form.cleaned_data['price']
            temp.sell = True
            temp.user = request.user
            temp.save()
            wish_user = Wisher.objects.filter(state=temp.state, category=temp.category)
            for users in wish_user:
                mail_id = users.user.email
                send_mail("Product Added",
                'A new product of your interest is added. Do checkout',
                'secondbucksstate@gmail.com',
                [mail_id])
                users.delete()
            return redirect('product:product_details', state_id = temp.state.pk,category_id=temp.category.pk,product_id=temp.pk)
        
        else:
            return HttpResponse(form['img'].errors)

def RegisterShareProduct(request):
    form = ShareProductRegistrationForm()

    if request.method == 'GET':
        return render(request, 'product/product_form.html', {'form': form})
    
    if request.method =='POST':
        form = ShareProductRegistrationForm(request.POST)
        if form.is_valid():
            temp = Product()
            temp.name = form.cleaned_data['name']
            temp.descripton = form.cleaned_data['descripton']
            temp.category = form.cleaned_data['category']
            temp.state = form.cleaned_data['state']
            temp.img = form.cleaned_data['img']
            temp.day_of_return = form.cleaned_data['day_of_return']
            temp.user = request.user
            temp.save()
            wish_user = Wisher.objects.filter(state=temp.state, category=temp.category)
            for users in wish_user:
                mail_id = users.user.email
                send_mail("Product Added",
                'A new product of your interest is added. Do checkout',
                'secondbucksstate@gmail.com',
                [mail_id])
                users.delete()
            return redirect('product:product_details', state_id = temp.state.pk,category_id=temp.category.pk,product_id=temp.pk)
        
        else:
            return HttpResponse(form.errors)



def RegisterUserDetails(request):
    form = UserDetailsForm()
    if request.method == 'GET':
        curr_user = request.user
        try:
            u = UserDetails.objects.get(user=curr_user)
            return HttpResponse("You have already registered. You can Update previous Details")

        except UserDetails.DoesNotExist:
            return render(request, 'userdet_form.html' , {'form': form})
            
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            temp = UserDetails()
            temp.user = request.user
            temp.state = form.cleaned_data['state']
            temp.phone = form.cleaned_data['phone']
            temp.img = form.cleaned_data['img']
            temp.save() 
            return redirect('product:categories', state_id=temp.state.pk )
        else:
            return HttpResponse(form.errors)

#not  working
class UpdateUserDetails(UpdateView):
    model = UserDetails
    fields = ['state', 'phone', 'img']


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('product:index')



class UserFormView(View):
    form_class = UserSignupForm
    template_name = 'user_reg_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
 
            user=authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('product:register-userdetails')

        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('product:index')
            else:
                return render(request, 'login_form.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login_form.html', {'error_message': 'Invalid login'})
    return render(request, 'login_form.html')


def logout_user(request):
    logout(request)
    return redirect('product:index')


def ads(request):
    current_user = request.user
    ad = Product.objects.filter(user=current_user)
    return render(request, 'product/ads.html', {'ads': ad})

@login_required
def notify(request, state_id, category_id):
    wisher = Wisher()
    wisher.state=State.objects.get(pk=state_id)
    wisher.category=Category.objects.get(pk=category_id)
    wisher.user = request.user
    wisher.save()
    return render(request, 'notified.html', {'category': wisher.category} )

@login_required
def report(request, product_id):
    ad = ReportedAd()
    ad.product=Product.objects.get(pk=product_id)
    ad.user = request.user
    ad.save()
    return  render(request, 'report.html')

def view_user(request, user_id):
    u = User.objects.get(pk=user_id)
    try:
        user_det = UserDetails.objects.get(user=u)
    except UserDetails.DoesNotExist:
        user_det = None
    return render(request, 'view_user_details.html',{'userdetail': user_det, 'u': u})

@login_required
def send_reminder(request):
    if request.user.is_superuser:
        today = datetime.today()
        today = today + timedelta(days = 2)
        products = Product.objects.all()
        for product in products:
            mail_id = product.user.email
            d = product.day_of_return
            if d.day == today.day:
                if d.month == today.month:
                    if d.year == today.year:
                        send_mail("Collect Product",
                    'Your product is to be taken back after 2 days',
                    'secondbucksstate@gmail.com',
                    [mail_id])
        return HttpResponse("Email Sent to the concerned Users")
    else:
        return HttpResponse("You are not a Superuser")
