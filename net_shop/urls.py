from django.urls import path
from net_shop import views

urlpatterns = [
    path("", views.index, name='home'),
    # path("login", views.login, name='login'),
    # path("logout", views.logout, name='logout'),
    # path("register", views.register, name='register'),
]
