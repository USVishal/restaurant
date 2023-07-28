"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from proapp1 import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index),
    path('login/',views.login),
    path('loginaccount/',views.loginaccount),
    path('createaccount/',views.createaccount),
    path('newaccount/',views.newaccount),
    path('homeadmin/',views.homeadmin),
    path('addrest/',views.addrest),
    path('addrestdb/',views.addrestdb),
    path('viewrest/',views.viewrest),
    path('updaterest/',views.updaterest),
    path('updaterest1/<int:id>',views.updaterest1),


    path('deleterest1/<int:id>',views.deleterest1),

    

    path('updaterestdb/<int:id>',views.updaterestdb),
    path('viewoffer/',views.viewoffer),

    path('publichome/',views.publichome),
    path('homerestaurant/',views.homerestaurant),
    path('createaccount/',views.createaccount),
    path('sfeedback/',views.sfeedback),
    path('createrestaccount/',views.createrestaccount),
    path('newrestaurant/',views.newrestaurant),

    path('offers/',views.offers),
    path('offeradd/',views.offeradd),
    path('updateoffer/<int:id>',views.updateoffer),
    path('update_offerdb/<int:id>',views.update_offerdb),
    path('deleteoffer/<int:id>',views.deleteoffer),
    path('useroffer/',views.useroffer),



    path('viewfeedback/',views.viewfeedback),

    path('reshome/',views.reshome),
    path('addfoodmenu/',views.addfoodmenu),
    path('foodmenu/',views.foodmenu),

    path('fooditem/',views.fooditem),
    path('addfooditem/',views.addfooditem),
    path('foodview/',views.foodview),
    

    path('update_delete/',views.update_delete),
    path('menu_up_del/<int:id>',views.menu_up_del),
    path('menu_update/<int:id>',views.menu_update),
    path('menu_delete/<int:id>',views.menu_delete),

    path('menuview/',views.menuview),
    path('foodUpdate/',views.foodUpdate),
    path('foodupdatepage/<int:id>',views.foodupdatepage),
    path('foodupdatedb/<int:id>',views.foodupdatedb),

    path('foodDelete/<int:id>',views.foodDelete),


    path('indexmenu/',views.indexmenu),
    path('indexfood/',views.indexfood),
    path('indexoffer/',views.indexoffer),
    path('indexrestaurant/',views.indexrestaurant),
    path('indexfeedback/',views.indexfeedback),

    path('adminfeedback/',views.adminfeedback),
    path('userfeedback/',views.userfeedback),
    path('restfeedback/',views.restfeedback),
    path('usermenu/',views.usermenu),
    path('userfoodview/',views.userfoodview),
    path('userviewrest/',views.userviewrest),

    path('indexhome/',views.indexhome),
    path('indexabout/',views.indexabout),

    path('userhome/',views.userhome),
    path('userabout/',views.userabout),

    path('adminhome/',views.adminhome),


    path('reshome/',views.reshome),
    path('logout/',views.logout),
    path('display/<int:id>', views.display, name='display'),
    path('displayfood/<int:id>',views.displayfood, name='displayfood'),
    path('cart/<int:id>', views.cart, name='cart'),
    path('addcart/',views.addcart,name='addcart'),
    path('viewcart/',views.viewcart,name='viewcart'),
    
    

    
   
]
