from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('account/', views.account, name="account"),


    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('bag/', views.bag, name="bag"),
    path('checkout/', views.checkout, name="checkout"),



    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

]
