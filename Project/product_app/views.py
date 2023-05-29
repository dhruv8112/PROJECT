from django.shortcuts import render
from .models import products, categories

# Create your views here.


def login(request):
    
    return render(request, 'login.html')


def index(request):
    prod = products.get_product()
    print(prod)
    return render(request, 'index.html', {'pro': prod})


def single_product(request,pro_id):
    single=products.objects.filter(pro_id=pro_id)
    return render(request,'single.html',{'single': single})

def category(request):
    # Category name nit retun so it not displayed cat name in category page
    cat = categories.get_category()
    print(cat)
    return render(request, 'category.html', {'cat': cat})
