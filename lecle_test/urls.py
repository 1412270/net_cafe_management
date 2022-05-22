"""lecle_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from net_shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add_funds', views.add_funds, name='add_funds'),
    path('computers', views.computer_list, name='computer_list'),
    path('customers', views.get_customers, name='customer_list'),
    path('bills', views.bill_list, name='bill_list'),
    path('new_computer', views.new_computer, name='new_computer'),
    path('new_customer', views.new_customer, name='new_customer'),
    path('new_bill', views.new_bill, name='new_bill'),
]
