from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.http import HttpResponse

def Admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == None:
            return view_func(request,*args,**kwargs)
        if group == "customer":
            return view_func(request,*args,**kwargs)
        if group == "merchant":
           return redirect('AdminIndex')
    return wrapper_func


def unauthenticate_user(views_fun):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('Index')
        else:
            return views_fun(request,*args,**kwargs)
    return wrapper_func


#def allowed_user(view_func):
 #    return wrapper_func

def allowed_users(allowed_rolls = []):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.groups.all().exists():
                group = request.user.groups.all()[0].name
            if group in allowed_rolls:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("You are not autherize to view this page")
        
        return wrapper_func
    return decorator
