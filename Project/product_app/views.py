from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import products, categories, cart
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.


def login(request):

    return render(request, 'login.html')

def index(request):
    product_list = products.get_product()
    print(product_list,products)
    return render(request, 'index.html', {'products': product_list})


def single_product(request, pro_id):
    single = products.objects.filter(pro_id=pro_id)
    return render(request, 'single.html', {'single': single})


def category(request):
    # Category name nit retun so it not displayed cat name in category page
    cat = categories.get_category()
    print(cat)
    return render(request, 'category.html', {'cat': cat})


# Create your models here.
def index(request):
    return render(request, 'index.html')


def register_page(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        upass = request.POST.get('password')
        ucon_password = request.POST.get('confirm_password')
        uaddress = request.POST.get('address')

        # Check if the user with the same username already exists
        if User.objects.filter(username=uname).exists():
            # User with the same username already exists
            # Handle the appropriate logic (e.g., display an error message)
            return HttpResponse('Username already exists')

        # Create a new user
        my_user = User.objects.create_user(uname, uemail, upass)
        my_user.save()
        # Redirect to the login page after successful registration
        return redirect(login)

    # Render the registration form
    return render(request, 'reg.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('user_name')
        password = request.POST.get('user_password')
        print(email, password)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            return redirect('index')
        # Replace 'index' with the appropriate URL name for your index page
        else:
            message = 'Invalid email or password'
            print(message)
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


def cart(request, product_id):

    product = get_object_or_404(product, id=product_id)
    cart_item, created = cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return render(request,'cart.html')
