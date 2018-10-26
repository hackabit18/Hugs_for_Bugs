from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        college_id = request.POST.get("college_name")
        return redirect('product:categories', college_id=college_id)

    colleges = College.objects.all()
    return render(request, 'index.html', {'colleges': colleges})
