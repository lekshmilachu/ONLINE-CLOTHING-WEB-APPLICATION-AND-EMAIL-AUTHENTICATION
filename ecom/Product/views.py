from django.shortcuts import render,redirect
from .forms import ProductAddform
from django.contrib import messages
from .models import ProductDetails
from django.contrib.auth.decorators import login_required
# Create your views here.


def AddProduct(request):
    form = ProductAddform()
    if request.method =="POST":
        form = ProductAddform(request.POST,request.FILES)
        if form.is_valid():
            Product = form.save()
            Product.Merchant= request.user
            Product.save()
            messages.info(request,"Product added to list")
            return redirect('AddProduct')
    
    return render(request,'addproduct.html',{"form":form})

def ProductViewMerchant(request):
    products = ProductDetails.objects.all()
    context ={
        "products":products
    }
    return render(request,"productlist.html",context)

def DeleteProduct(request,pk):
    product = ProductDetails.objects.get(Product_Id = pk)
    product.Product_Image.delete()
    product.delete()
    messages.info(request,"Product deleted")
    return redirect("ProductViewMerchant")

def UpdateProduct(request,pk):
    product =ProductDetails.objects.filter(Product_Id = pk)
    if request.method=="POST":
        
        pname = request.POST["pname"] 
        pbrand = request.POST["pbrand"] 
        pdes = request.POST["pdes"]
        pprice = request.POST["pprice"]
        pcat = request.POST["pcat"]
        pimg = request.FILES["pimg"]

        item =ProductDetails.objects.get(Product_Id = pk)

        item.Product_Name =pname
        item.Product_Brand =pbrand
        item.Product_Description =pdes
        item.Product_Price =pprice
        item.Product_Category =pcat
        item.Product_Image.delete()
        item.Product_Image = pimg
        item.save()

        messages.info(request,"Item Updated")
        return redirect("UpdateProduct" ,pk=pk)
    context ={
        "product" : product
    }
    return render(request,"updateproduct.html",context)


def ProductViewCustomer(request,pk):
    product =ProductDetails.objects.filter(Product_Id = pk)   
    context ={
        "product":product
    }
    return render(request,"productviewcustomer.html",context)


