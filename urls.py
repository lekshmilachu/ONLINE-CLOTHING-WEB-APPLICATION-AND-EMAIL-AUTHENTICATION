
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from Public import views
from Public import urls

import Public
from Product import urls
import Product
from Cart import urls
import Cart


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(Public.urls)),
    path('product/',include(Product.urls)),
    path('cart/',include(Cart.urls)),
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)