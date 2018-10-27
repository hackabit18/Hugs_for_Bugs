from django.shortcuts import render
from django.http import HttpResponse





def index(request):
    if request.method == 'POST':
        college_id = request.POST.get("college_name")
        return redirect('product:categories', college_id=college_id)

    colleges = College.objects.all()
    return render(request, 'index.html', {'colleges': colleges})


def category_list(request, college_id):
    categories = Category.objects.all()
    college = College.objects.get(pk=college_id)
    return render(request, 'category/categories.html', {'categories': categories, 'college': college})


def category_wise(request, college_id, category_id):
    college = College.objects.get(pk=college_id)
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(college=college, category=category)
    return render(request, 'category/category_wise.html', {'products': products, 'college': college, 'category': category})


def product_details(request, college_id, category_id, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product/product_details.html', {'product': product})
    

class RegisterCollege(CreateView):
        model = College
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
            temp.name = form.cleaned_data['name']
            temp.descripton = form.cleaned_data['descripton']
            temp.category = form.cleaned_data['category']
            temp.college = form.cleaned_data['college']
            temp.price = form.cleaned_data['price']
            temp.sell = True
            temp.user = request.user
            temp.save()
            wish_user = Wisher.objects.filter(college=temp.college, category=temp.category)
            for users in wish_user:
                mail_id = users.user.email
                send_mail("Product Added",
                'A new product of your interest is added. Do checkout',
                'secondbuckscollege@gmail.com',
                [mail_id])
                users.delete()
            return redirect('product:product_details', college_id = temp.college.pk,category_id=temp.category.pk,product_id=temp.pk)
        
        else:
            return HttpResponse(form.errors)

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
            temp.college = form.cleaned_data['college']
            temp.no_of_days = form.cleaned_data['no_of_days']
            temp.user = request.user
            temp.save()
            wish_user = Wisher.objects.filter(college=temp.college, category=temp.category)
            for users in wish_user:
                mail_id = users.user.email
                send_mail("Product Added",
                'A new product of your interest is added. Do checkout',
                'secondbuckscollege@gmail.com',
                [mail_id])
                users.delete()
            return redirect('product:product_details', college_id = temp.college.pk,category_id=temp.category.pk,product_id=temp.pk)
        
        else:
            return HttpResponse(form.errors)



def RegisterUserDetails(request):
    form = UserDetailsForm()

    if request.method == 'GET':
        return render(request, 'userdet_form.html' , {'form': form})
    
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            temp = UserDetails()
            temp.user = request.user
            temp.college = form.cleaned_data['college']
            temp.phone = form.cleaned_data['phone']
            temp.img = form.cleaned_data['img']
            temp.save() 
            return HttpResponse("Done")
        else:
            return HttpResponse(form.errors)

#not  working
class UpdateUserDetails(UpdateView):
    model = UserDetails
    fields = ['college', 'phone', 'img']


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


