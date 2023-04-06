from django.urls import path
from .import views

urlpatterns = [
    path("CartView",views.CartView,name="CartView"),
    path("AddCart/<int:pk>",views.AddCart,name="AddCart"),
    path('DeleteCart/<int:pk>',views.DeleteCart,name="DeleteCart"),
    path('PlaceOrder',views.PlaceOrder,name="PlaceOrder"),
    path('paymenthandler',views.paymenthandler,name='paymenthandler'),
    path("CustomerOrders",views.CustomerOrders,name="CustomerOrders")
]