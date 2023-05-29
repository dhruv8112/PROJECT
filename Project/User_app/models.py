from django.db import models

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
