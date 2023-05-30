from django.db import models
from django.utils.html import format_html
# Create your models here.


class categories(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='category_image/')
    def img_return(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px border-radius:70%" />'.format(self.img))
    
    def __str__(self):
        return self.cat_name
    
    def get_category():
        return categories.objects.all()
    

class products(models.Model):
    brand_name = models.CharField(max_length=110, null=True)
    pro_id=models.IntegerField(null=True,unique=True)
    pro_name = models.CharField(max_length=200)
    Pro_Description = models.CharField(max_length=2000, default='Default description')
    size = models.IntegerField(null=True)
    pro_cat = models.ForeignKey(categories, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    img = models.ImageField(upload_to='ProductImage',null=True, blank=True)
    
    def get_product():
        return products.objects.all()


class Images(models.Model):
    Imag_name=models.ForeignKey(categories, on_delete=models.CASCADE, related_name='pro_name' , null=True)
    product = models.ForeignKey(
        products, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='ProductImage')


class cart(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    
class user(models.Model):
    COUNTRY_CHOICES = (
        ('USA', 'United States'),
        ('CAN', 'Canada'),
        ('UK', 'United Kingdom'), ('IND', 'INDIA')
        # Add more country choices as needed
    )

    First = models.CharField(max_length=35)
    last = models.CharField(max_length=35)
    contact = models.IntegerField(null=False)
    Password = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    age = models.IntegerField()
    # Set default value manually
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES,default='')


