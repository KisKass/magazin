"""
URL configuration for magazin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/cat/<int:cat_id>', views.catalog, name='cat'),
    path('item/<int:id>', views.item, name='item'),
    path('order/<int:id>', views.order, name='order'),

    path('profile/', views.profile, name='profile'),#
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('login', views.login_v, name="login"),
    path('logout', views.logout_v, name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
