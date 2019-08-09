"""E_Commerce_Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('productdetails/<int:id>', views.productdetails, name='product_details'),
    path('checkout/', views.checkout, name='checkout'),
    path('placeorder/', views.placeorder, name='placeorder'),
    path('updateproduct/<int:id>', views.updateproduct, name='updateproduct'),
    path('updatecategory/<int:id>', views.updatecategory, name='updatecategory'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('productlist/', views.productlist, name='productlist'),
    path('buyerprofile/', views.buyerprofile, name='buyerprofile'),
    path('historydetails/<int:id>/', views.historydetails, name='historydetails'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('categorylist/', views.categorylist, name='categorylist'),
    path('deletecategory/<int:id>', views.deletecategory, name='deletecategory'),
    path('deleteproduct/<int:id>', views.deleteproduct, name='deleteproduct'),

]
