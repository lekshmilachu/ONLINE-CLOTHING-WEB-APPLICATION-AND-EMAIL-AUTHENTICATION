from django.db import models
from django.contrib.auth.models import User


class ProductDetails(models.Model):


    option =(
        ("Men","Men"),
        ("Women","Women"),
        ("Kids","Kids")
    )

    Product_Id = models.AutoField(primary_key=True)
    Product_Name = models.CharField(max_length=255)
    Product_Brand = models.CharField(max_length=255)
    Product_Description = models.CharField(max_length=1000)
    Product_Price = models.IntegerField()
    Product_Category = models.CharField(max_length=255,choices=option)
    Product_Image = models.ImageField(upload_to="product_image")
    Product_Stock = models.PositiveIntegerField()
    Merchant = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
