from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserAddForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import Admin_only,unauthenticate_user,allowed_users
from Product.models import ProductDetails
from django.template.loader import render_to_string  

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def Contact(request):
    return render(request,'contact.html')

def ContactCus(request):
    return render(request,'cuscontact.html')


@Admin_only
def Index(request):
    product = ProductDetails.objects.all()
    context = {
        "Product":product
    }
    return render(request,'index.html',context)

@allowed_users(allowed_rolls = ["merchant"])
def AdminIndex(request):
    return render(request,"adminhome.html")

@unauthenticate_user
def SignIn(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["pswd"]
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect("Index")
        else:
            messages.info(request,"Username or password is incorrect")
    return render(request,'login.html')

def activateemail(request ,user,to_email):
    messages.success(request,f'Dear {user} please go to your email {to_email} inbox and click on received activation link to confirm and complete the registration.Chck your spam folder.')

@unauthenticate_user
def SignUp(request):
    form = UserAddForm()
    if request.method =="POST":
        form = UserAddForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")

            if User.objects.filter(username = username).exists():
                messages.info(request,"User Name Already exists")
                return redirect('SignUp')
            else:
                user = form.save(commit=False)  
                user.is_active = False  
                user.save()
                message = render_to_string('email.html', {
                    'user': user,
                    'pk':user.id,  
                 
                })  

                send_mail(
                    'hy',
                    message,
                    'settings.EMAIL_HOST_USER', 
                    [email] )
                messages.success(request,"User Created")
                pk=user.id
                return redirect('log',pk)
            

    context = {"form":form}
    return render(request,'register.html',context)

def SignOut(request):
    logout(request)
    return redirect('Index')

def log(request,pk):
    user=User.objects.get(id=pk)
    check=user.is_active
    context ={
        'check':check
    }

    return render(request,'log.html',context)

def activate(request,pk):
    user=User.objects.get(id=pk)
    user.is_active = True
    user.save()  

    return redirect('SignIn') 

