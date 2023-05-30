from django.contrib import admin
from .models import categories, products, Images,user


class CatAdmin(admin.ModelAdmin):
    list_display = ('img_return','cat_name', 'cat_desc', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pro_name', 'pro_cat', 'brand_name',
                    'price', 'Pro_Description','size',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('img', 'product',)


class userAdmin(admin.ModelAdmin):
    list_display = ['age','address','contact','last','First','country',]
    
    
admin.site.register(user,userAdmin)
admin.site.register(categories, CatAdmin)
admin.site.register(products, ProductAdmin)
admin.site.register(Images, ImageAdmin)
