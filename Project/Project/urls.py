"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from product_app.views import login, category, single_product, cart,index,register_page

from contact_us_app.views import contact_us


# agar multiple views mathi url import karavna hoy ne error aave toh product app n jem  import kari deva

urlpatterns = [
    path('admin/', admin.site.urls),
    # Use the login view from product_app
    path('Login/', login, name='login'),
    path('', index, name='index'),
    path('Register', register_page),
    path('contact/', contact_us, name='contact_us'),
    path('category', category),
    path('single/<int:pro_id>/', single_product, name='single_product'),
    path('cart/<int:product_id>/',cart, name='cart'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
