from django.forms import ModelForm
from .models import ProductDetails

class ProductAddform(ModelForm):
    class Meta:
        model = ProductDetails
        fields = ["Product_Name","Product_Brand","Product_Description","Product_Price","Product_Stock","Product_Category","Product_Image"]
