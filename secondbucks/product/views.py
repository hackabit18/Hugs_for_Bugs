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















def index(request):
    return HttpResponse("Working")