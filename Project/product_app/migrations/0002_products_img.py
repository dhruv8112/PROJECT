# Generated by Django 4.1.5 on 2023-05-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImage'),
        ),
    ]
