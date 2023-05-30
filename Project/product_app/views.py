from django.shortcuts import render, redirect
from .models import products, categories, cart
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.


def login(request):

    return render(request, 'login.html')


def index(request):
    prod = products.get_product()
    print(prod)
    return render(request, 'index.html', {'pro': prod})


def single_product(request, pro_id):
    single = products.objects.filter(pro_id=pro_id)
    return render(request, 'single.html', {'single': single})


def category(request):
    # Category name nit retun so it not displayed cat name in category page
    cat = categories.get_category()
    print(cat)
    return render(request, 'category.html', {'cat': cat})

from django.shortcuts import  get_object_or_404

def cart(request, product_id):
    product = get_object_or_404(product, id=product_id)
    cart_item, created = cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return render(request, 'cart.html')


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
        return redirect(login)  # Redirect to the login page after successful registration

    # Render the registration form
    return render(request, 'reg.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'index' with the appropriate URL name for your index page
        else:
            message = 'Invalid email or password'
            return render(request, 'login.html', {'message': message})
    else:
        return render(request, 'login.html')
