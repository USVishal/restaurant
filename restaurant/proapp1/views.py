from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from proapp1.models import tbl_restaurant,tbl_user,tbl_feedback,tbl_restAdmin,tbl_offer,tbl_foodMenu,tbl_foodItem,tbl_cart
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
# Create your views here.
# def index(request):
#     return render(request,"index.html")
def login(request):
    return render(request,"login.html")

def logout(request):
   
    del request.session['username']
    return redirect('/')


def loginaccount(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    data=authenticate(username=username,password=password)
    request.session['username']=username
    
    
    if data is not None and data.is_superuser ==1:
         return redirect('/adminhome/')
                 
    elif data is not None and data.is_superuser==0 :
        a1=tbl_user.objects.get(username=username) # checking user account table
        if a1 is not None and a1.status=="user": # checking user type
            return redirect('/userhome/')
        elif a1 is not None and a1.status=="RestAdmin": 
            
            return redirect('/reshome/') 
    else:
         return HttpResponse("User does not exist")
    


def reshome(request):
    b= request.session['username']
    
    b1=tbl_user.objects.get(username=b)
    
    a="Fault"
    
    return render(request,"homerestaurant.html",{"a1":a})  



def createaccount(request):
    return render(request,"createaccount.html") 
def newaccount(request):
        if request.method == 'POST':
            p1=User()
            p2=tbl_user()
            p1.first_name=request.POST.get('firstname')
            p1.last_name=request.POST.get('lastname')
            p1.username=request.POST.get('username')
            p1.email=request.POST.get('email')
            password=request.POST.get('password')
            p1.set_password(password)
            
            
            p2.first_name=request.POST.get('firstname')
            p2.last_name=request.POST.get('lastname')
            p2.gender=request.POST.get('gender')
            p2.phone=request.POST.get('phone')
            p2.email=request.POST.get('email')
            p2.address=request.POST.get('address')
            p2.district=request.POST.get('district')
            p2.state=request.POST.get('state')
            p2.username=request.POST.get('username')
            p2.status='user'
            p2.save()
            p1.save()
            return render(request,"index.html") 
def homeadmin(request):
    return render(request,"homeadmin.html")
# def homeuser(request):
#     return render(request,"homeuser.html")
def addrest(request):
    return render(request,"addrestaurant.html")
def addrestdb(request):
    r=tbl_restaurant()
    r1=User()
    r2=tbl_user()

    r.firstName=request.POST.get('firstName')
    r.lastName=request.POST.get('lastName')
    r.restaurantName=request.POST.get('restaurantName')
    r.location=request.POST.get('location')
    r.typeOfShop=request.POST.get('typeOfShop')
    r.email=request.POST.get('email')
    r.phone=request.POST.get('phone')
    r.noOfStaff=request.POST.get('noOfStaff')
    r.authPerson=request.POST.get('authPerson')
    r.pEmail=request.POST.get('pEmail')
    r.pContact=request.POST.get('pContact')
    r.username=request.POST.get('username')
    r.password=request.POST.get('password')
    r.status='restaurant'

    r1.first_name=request.POST.get('firstName')
    r1.last_name=request.POST.get('lastName')
    r1.username=request.POST.get('username')
    r1.email=request.POST.get('email')
    password=request.POST.get('password')
    r1.set_password(password)

    r2.firstname=request.POST.get('firstName')
    r2.lastname=request.POST.get('lastName')
    r2.gender="None"
    r2.phone=request.POST.get('phone')
    r2.email=request.POST.get('email')
    r2.address=request.POST.get('location')
    r2.district=request.POST.get('location')
    r2.username=request.POST.get('username')
    r2.typeOfShop=request.POST.get('typeOfShop')
    r2.email=request.POST.get('email')
    r2.state="Kerala"
    r2.status="RestAdmin"



    r.save()
    r1.save()
    r2.save()
    return redirect('/adminhome/')
def viewrest(request):
    t3=tbl_restaurant.objects.all()
    return render(request,"viewrestaurant.html",{'data':t3})  
def userviewrest(request):
    t3=tbl_restaurant.objects.all()
    return render(request,"userrestaurant.html",{'data':t3}) 
def indexrestaurant(request):
    t3=tbl_restaurant.objects.all()
    return render(request,"indexrestaurant.html",{'data':t3})  

def updaterest(request):
    t3=tbl_restaurant.objects.all()
    return render(request,"updaterest.html",{'data':t3})

def updaterest1(request,id):
   u1=tbl_restaurant.objects.get(id=id)
   return render(request,"updaterestaurant.html",{'data':u1}) 
   
def updaterestdb(request,id):
    r=tbl_restaurant.objects.get(id=id)
    t3=tbl_restaurant.objects.all()
    
    r.firstName=request.POST.get('firstName')
    r.lastName=request.POST.get('lastName')
    r.restaurantName=request.POST.get('restaurantName')
    r.location=request.POST.get('location')
    r.typeOfShop=request.POST.get('typeOfShop')
    r.email=request.POST.get('email')
    r.phone=request.POST.get('phone')
    r.noOfStaff=request.POST.get('noOfStaff')
    r.authPerson=request.POST.get('authPerson')
    r.pemail=request.POST.get('pemail')
    r.pContact=request.POST.get('pContact')
    r.save()
    t3=tbl_restaurant.objects.all()
    return render(request,"updaterest.html",{'data':t3}) 
   
def deleterest1(request,id):
    d1=tbl_restaurant.objects.get(id=id)
    d1.delete()
    t3=tbl_restaurant.objects.all()
    return render(request,"updaterest.html",{'data':t3})
 
def homeadmin(request):
    return render(request,"homeadmin.html")

def publichome(request):
    return render(request,"publichome.html")
def homerestaurant(request):
    return render(request,"homerestaurant.html")

def createaccount(request):
    return render(request,"createaccount.html")

def sfeedback(request):
    f=tbl_feedback()
    f.fId=request.POST.get('fId')
    f.CustomerId=request.POST.get('CustomerId')
    f.feedback=request.POST.get('feedback')
    f.status=request.POST.get('status')
    f.save()
    return redirect("/userhome/")
def createrestaccount(request):
    return render(request,"restaccount.html")
def newrestaurant(request):
    ra=tbl_restAdmin()
    p1=User()
    ra.username=request.POST.get('username')
    password="****"
    ra.restName=request.POST.get('restName')
    ra.email=request.POST.get('email')
    ra.restId=request.POST.get('restId')
    ra.status="restaurant"

    p1.username=request.POST.get('username')
    password=request.POST.get('password')
    p1.set_password(password)
    p1.email=request.POST.get('email')
    p1.is_staff= 1

    ra.save()
    p1.save()
    return render(request,"homeadmin.html")

def offers(request):
    b= request.session['username']
    data=tbl_foodMenu.objects.filter(restName=b)

    return render(request,"offer.html",{'offer':b, 'menu':data})

def offeradd(request):
    offer=tbl_offer.objects.all()
    to=tbl_offer()
    

    to.restId=request.POST.get('restId')
    to.menuItemName=request.POST.get('menuItemName')
    to.offer=request.POST.get('offer')
    to.startDate=request.POST.get('startDate')
    to.endDate=request.POST.get('endDate')
    to.details=request.POST.get('details')
    to.status=request.POST.get('status')
    to.save()
    return render(request,"viewoffer.html",{"offer": offer})
def index(request):
    offer=tbl_offer.objects.all()
    return render(request, 'index.html', {'offer': offer})

def viewoffer(request):
    b= request.session['username']
    off=tbl_offer.objects.filter(restId=b)
    return render(request,"viewoffer.html",{"offer": off}) 
def useroffer(request):
    off=tbl_offer.objects.all()
    return render(request,"useroffer.html",{"offer": off}) 
def indexoffer(request):
    off=tbl_offer.objects.all()
    return render(request,"indexoffer.html",{"offer": off}) 

def updateoffer(request,id):
    uo=tbl_offer.objects.get(id=id)
    return render(request,"offerupdate.html",{'offer':uo})

def update_offerdb(request,id):
    off=tbl_offer.objects.all()
    uo=tbl_offer.objects.get(id=id)
    uo.restId=request.POST.get('restId')
    uo.menuItemName=request.POST.get('menuItemName')
    uo.offer=request.POST.get('offer')
    uo.startDate=request.POST.get('startDate')
    uo.endDate=request.POST.get('endDate')
    uo.details=request.POST.get('details')
    uo.status=request.POST.get('status')
    uo.save()
    return render(request,"viewoffer.html",{"offer": off}) 

def deleteoffer(request,id):
    off=tbl_offer.objects.all()
    od=tbl_offer.objects.get(id=id)
    od.delete()
    return render(request,"viewoffer.html",{"offer": off}) 


def viewfeedback(request):
    fb=tbl_feedback.objects.all()
    return render(request, 'viewfeedback.html', {'fb': fb}) 

def indexfeedback(request):
    fb=tbl_feedback.objects.all()
    return render(request, 'indexfeedback.html', {'fb': fb})  
def adminfeedback(request):
    fb=tbl_feedback.objects.all()
    return render(request, 'adminfeedback.html', {'fb': fb})  
def userfeedback(request):
    fb=tbl_feedback.objects.all()
    return render(request, 'userfeedback.html', {'fb': fb}) 
def restfeedback(request):
    fb=tbl_feedback.objects.all()
    return render(request, 'restfeedback.html', {'fb': fb}) 
    
def reshome(request):
    return render(request,'homerestaurant.html',)  

def addfoodmenu(request):
    b= request.session['username']
    return render(request,'addfoodmenu.html',{'d':b}) 

def foodmenu(request):
    b= request.session['username']
    
    b1=tbl_user.objects.get(username=b)
   
     
    m=tbl_foodMenu()
    m.restName=request.POST.get('restName')
    m.menuName=request.POST.get('menuName')
    m.type=request.POST.get('type')
    m.cuisine=request.POST.get('cuisine')
    m.origin=request.POST.get('origin')
    m.save()
    return render(request,"homerestaurant.html",{"a1":b1}) 
def fooditem(request):
    b= request.session['username']
    data=tbl_foodMenu.objects.filter(restName=b)
    return render(request,'addfooditem.html',{'d':data,'d1':b})    
def addfooditem(request):
    f=tbl_foodItem()
    f.restName=request.POST.get('restName')
    f.menuName=request.POST.get('menuName')
    f.menuItemName=request.POST.get('menuItemName')
    f.quantity=request.POST.get('quantity')
    f.price=request.POST.get('price')
    f.type=request.POST.get('type')
    f.cookingTime=request.POST.get('cookingTime')
    f.status=request.POST.get('status')
    f.save()
    return render(request,'addfooditem.html',)          

def foodview(request):
    b= request.session['username']
    items=tbl_foodItem.objects.filter(restName=b)
    return render(request,"foodview.html",{"menu": items}) 
def userfoodview(request):
    items=tbl_foodItem.objects.all()
    return render(request,"userfooditem.html",{"menu": items}) 

def update_delete(request):
    b= request.session['username']
    ud=tbl_foodMenu.objects.filter(restName=b)
    return render(request,"MenuUpdateDelete.html",{'data':ud})


def menu_up_del(request,id):
    ud=tbl_foodMenu.objects.get(id=id)
    # b= request.session['username']
    return render(request,"menu_up_del.html",{'data':ud})


def menu_update(request,id):
   b= request.session['username']
   db=tbl_foodMenu.objects.filter(restName=b)
   
   ud=tbl_foodMenu.objects.get(id=id)
   ud.restName=request.POST.get('restName')
   ud.menuName=request.POST.get('menuName')
   ud.type=request.POST.get('type')
   ud.cuisine=request.POST.get('cuisine')
   ud.origin=request.POST.get('origin')
   ud.save()
   return render(request,"MenuUpdateDelete.html",{'data':db})

def menu_delete(request,id):
    b= request.session['username']
    db=tbl_foodMenu.objects.filter(restName=b)
    dlte=tbl_foodMenu.objects.get(id=id)
    dlte.delete()
    return render(request,"MenuUpdateDelete.html",{'data':db})

def menuview(request):
    b= request.session['username']
    im=tbl_foodMenu.objects.filter(restName=b)
    return render(request,"menu.html",{"menu": im}) 
def usermenu(request):
    im=tbl_foodMenu.objects.all()
    return render(request,"usermenuitem.html",{"menu": im}) 

def foodUpdate(request):
    b= request.session['username']
    fu=tbl_foodItem.objects.filter(restName=b)
    return render(request,"foodUpdate.html",{'data':fu})
def foodupdatepage(request,id):
    ud=tbl_foodItem.objects.get(id=id)
    return render(request,"food_update.html",{'data':ud})

def foodupdatedb(request,id):
    b= request.session['username']
    food=tbl_foodItem.objects.filter(restName=b)

    ud=tbl_foodItem.objects.get(id=id)
    ud.restName=request.POST.get('restName')
    ud.menuName=request.POST.get('menuName')
    ud.menuItemName=request.POST.get('menuItemName')
    ud.quantity=request.POST.get('quantity')
    ud.price=request.POST.get('price')
    ud.type=request.POST.get('type')
    ud.cookingTime=request.POST.get('cookingTime')
    ud.status=request.POST.get('status')
    ud.save()
    return render(request,"foodUpdate.html",{'data':food})

def foodDelete(request,id):
    fu=tbl_foodItem.objects.all()
    fd=tbl_foodItem.objects.get(id=id)
    fd.delete()
    return render(request,"foodUpdate.html",{'data':fu})

def indexmenu(request):
    im=tbl_foodMenu.objects.all()
    return render(request,"indexmenu.html",{'menu':im})
def indexfood(request):
    im=tbl_foodItem.objects.all()
    return render(request,"indexfood.html",{'menu':im})

def indexhome(request):
    return render(request,'index.html')
def indexabout(request):
    return render(request,'index.html')

def userhome(request):
    b= request.session['username']
    
    a1=tbl_user.objects.get(username=b)
    return render(request,"homeuser.html",{"a1":a1})
def userabout(request):
    return render(request,'homeuser.html')

def adminhome(request):
    b= request.session['username']
    
    a1=User.objects.get(username=b)
    return render(request,"homeadmin.html",{"data":a1}) 

# add to cart



def display(request,id):  
    crt = tbl_foodMenu.objects.get(id=id)
    return render(request, "addtocart.html", {'data': crt})

def displayfood(request,id):  
    crt = tbl_foodItem.objects.get(id=id)
    return render(request, "displayfood.html", {'data': crt})

# def cart(request,id):
#     b= request.session['username']
    
#     crt=tbl_foodItem.objects.get(id=id)
#     return render(request,'cart.html', {'data':crt,'name':b})

from decimal import Decimal

def cart(request, id):
    b = request.session['username']
    crt = tbl_foodItem.objects.get(id=id)
   
    
    return render(request, 'cart.html', {'data': crt, 'name': b})





def addcart(request): 
    crt = tbl_foodItem.objects.get(id=id)
    total=request.POST.get('price') * request.POST.get('quantity')

    if request.method == 'POST':
        
        m = tbl_cart()
        m.restName = request.POST.get('restName')
        m.username = request.POST.get('username')
        m.foodItemName = request.POST.get('foodItemName')
        m.quantity = request.POST.get('quantity')
        m.price = request.POST.get('price')
        m.status = request.POST.get('status')
        m.save()
        b = request.session['username']
        a1 = tbl_user.objects.get(username=b)
        return render(request, "homeuser.html", {"a1": a1, 'tot':total,'ct':crt})
    else:
        return HttpResponse("Something went wrong")







def viewcart(request):
    return render(request,"viewcart.html")
    



