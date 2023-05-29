from django.db import models
from django.utils.html import format_html
# Create your models here.


class categories(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='category_image/')
    def img_return(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px border-radius:70%" />'.format(self.img))
    
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
    product = models.ForeignKey(
        products, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='ProductImage')
