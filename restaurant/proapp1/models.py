from django.db import models

# Create your models here.
class tbl_user(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    class Meta:
        db_table="tbl_user"

class tbl_restaurant(models.Model):
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    restaurantName=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    typeOfShop=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    noOfStaff=models.IntegerField()
    authPerson=models.CharField(max_length=200)
    pEmail=models.EmailField()
    pContact=models.IntegerField()
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    class Meta:
        db_table="tbl_restaurant"

class tbl_feedback(models.Model):
    fId=models.CharField(max_length=200)
    CustomerId=models.CharField(max_length=200)
    feedback=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    class Meta:
        db_table="tbl_feedback"

class tbl_restAdmin(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    restName=models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    restId=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    class Meta:
        db_table="tbl_restAdmin"

class tbl_foodMenu(models.Model):
    restName=models.CharField(max_length=200)
    menuName=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    cuisine=models.CharField(max_length=200)
    origin=models.CharField(max_length=200)
    class Meta:
        db_table="tbl_foodMenu"

class tbl_foodItem(models.Model):
    restName=models.CharField(max_length=200)
    menuName=models.CharField(max_length=200)
    menuItemName=models.CharField(max_length=200)
    quantity=models.IntegerField()
    price=models.IntegerField()
    type=models.CharField(max_length=200)
    cookingTime=models.TimeField()
    status=models.CharField(max_length=200)
    class Meta:
        db_table="tbl_foodItem"

class tbl_offer(models.Model):
    restId=models.CharField(max_length=200)
    menuItemName=models.CharField(max_length=200)
    offer=models.CharField(max_length=200)
    startDate=models.CharField(max_length=200)
    endDate=models.CharField(max_length=200)
    details=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    class Meta:
        db_table="tbl_offer"

class tbl_cart(models.Model):
     username=models.CharField(max_length=200)
     restName=models.CharField(max_length=200)
     foodItemName=models.CharField(max_length=200)
     quantity=models.IntegerField()
     price=models.IntegerField()
     status=models.CharField(max_length=200)
     class Meta:
        db_table="tbl_cart"
class tbl_order(models.Model):
    username=models.CharField(max_length=200)
    restName=models.CharField(max_length=200)
    totalPrice=models.IntegerField()
    status=models.CharField(max_length=200)
    class Meta:
        db_table="tbl_order"




