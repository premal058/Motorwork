from django.db import models

# Create your models here.
class Category(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    otp = models.IntegerField(default=999)
    # otp = models.CharField(max_length=50,null=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True, blank=False)
    updated_at=models.DateTimeField(auto_now_add=True, blank=False)

         

class Foreman(models.Model):
    Category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    Foreman_name=models.CharField(max_length=30)
    Foreman_jdate=models.DateField(blank=False,auto_now_add=True)
    # Foreman_salary=models.IntegerField(max_length=30,blank=False)
    # Foreman_type=models.CharField(max_length=30)
    Foreman_worktime=models.IntegerField(default=6)
    Foreman_address=models.CharField(max_length=30,default="")
    # Serviceid=models.ForeignKey(Service, on_delete=models.CASCADE)
    # Servicevehicleid=models.ForeignKey(Servicevehicle, on_delete=models.CASCADE)
    Foreman_contact=models.IntegerField()
    Foreman_email=models.EmailField(max_length=30)
    Foreman_password=models.CharField(max_length=20,blank=False,default="")
    Foreman_gender=models.CharField(max_length=30)
    Foreman_photo=models.ImageField(upload_to='main_app/static/main_app/img/foreman', default='main_app/static/main_app/img/avtar.jpg')

    




class User(models.Model):
    Category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    username=models.CharField(max_length=30)
    userpass=models.CharField(max_length=30)
    usergender=models.CharField(max_length=30)
    usermail=models.EmailField(max_length=30)
    useraddress=models.CharField(max_length=100)
    userremservice=models.IntegerField(default=0)
    userphone=models.IntegerField(default=999)
    userphoto=models.ImageField(upload_to='main_app/static/main_app/img/user', default='main_app/static/main_app/img/avtar.jpg')
    # servicevid= models.ForeignKey(Service, on_delete=models.CASCADE)
    # usedvid=models.ForeignKey(Usedvehicle, on_delete=models.CASCADE)
#   orderid=models.ForeignKey(Order, on_delete=models.CASCADE)
   
    


class Servicevehicle(models.Model):
    service_vehregno=models.CharField(max_length=10, primary_key=True)
    service_vehname=models.CharField(max_length=30)
    service_vehtype=models.CharField(max_length=30)
    service_vehcom=models.CharField(max_length=30)
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    foremanid= models.ForeignKey(Foreman, on_delete=models.CASCADE)

class appointment(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_number=models.CharField(max_length=10)
    vehicle_year=models.IntegerField()
    vehicle_type=models.CharField(max_length=10)
    vehicle_mileage=models.IntegerField()
    vehicle_appdate=models.DateField()
    vehicle_apptime=models.TimeField()
    vehicle_need=models.CharField(max_length=500) 
    vehicle_username=models.CharField(max_length=20)
    vehicle_useremail=models.EmailField()
    vehicle_info=models.CharField(max_length=50)
    vehicle_status=models.CharField(max_length=10)
    vehicle_address=models.CharField(max_length=30,default="")
    vehicle_contact=models.IntegerField(default=00000)
    vehicle_mode=models.CharField(max_length=10,default="")
    

class serviceaccept(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    veh_number=models.CharField(max_length=10)
    veh_year=models.IntegerField()
    veh_type=models.CharField(max_length=10)
    veh_mileage=models.IntegerField()
    veh_appdate=models.DateField()
    veh_apptime=models.TimeField()
    veh_need=models.CharField(max_length=500) 
    veh_username=models.CharField(max_length=20)
    veh_useremail=models.EmailField()
    veh_info=models.CharField(max_length=50)
    veh_status=models.CharField(max_length=10)
    veh_address=models.CharField(max_length=30,default="")
    veh_contact=models.IntegerField(default=0000)
    veh_mode=models.CharField(max_length=10,default="")
    veh_pdstatus = models.CharField(max_length=10,default="")
    
   


class servicereject(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    rej_number=models.CharField(max_length=10)
    rej_year=models.IntegerField()
    rej_type=models.CharField(max_length=10)
    rej_mileage=models.IntegerField()
    rej_appdate=models.DateField()
    rej_apptime=models.TimeField()
    rej_need=models.CharField(max_length=500) 
    rej_username=models.CharField(max_length=20)
    rej_useremail=models.EmailField()
    rej_info=models.CharField(max_length=50)
    rej_status=models.CharField(max_length=10)
    rej_address=models.CharField(max_length=30,default="")
    rej_contact=models.IntegerField(default=0000)
    rej_mode=models.CharField(max_length=10,default="")

class pickup(models.Model):
    vehid = models.ForeignKey(serviceaccept, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=13,default="")
    forid = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

class Service(models.Model):
    service_vehregno=models.ForeignKey(Servicevehicle, on_delete=models.CASCADE)    
    service_appdate=models.DateField(blank= False)
    service_type= models.CharField(max_length=30)
    foremanid= models.ForeignKey(Foreman, on_delete=models.CASCADE,default=1)
    service_validity=models.CharField(max_length=30)
    service_info=models.CharField(max_length=300)
    service_estimatecost=models.IntegerField()
    service_status=models.CharField(max_length=30)
    service_approx_time=models.DateTimeField(blank= False)
    service_completion_time=models.DateTimeField(blank= False)
    service_cost=models.IntegerField()

class Servicedone(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    forid = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    ser_number=models.CharField(max_length=10,default="")
    ser_year=models.IntegerField(default=299)
    ser_type=models.CharField(max_length=10,default="")
    ser_mileage=models.IntegerField(default=299)
    ser_appdate=models.DateField(default="2020-11-03")
    ser_apptime=models.TimeField(default="11:03:PM")
    ser_need=models.CharField(max_length=500,default="") 
    ser_username=models.CharField(max_length=20,default="")
    ser_useremail=models.EmailField(default="")
    ser_info=models.CharField(max_length=50,default="")
    ser_status=models.CharField(max_length=10,default="")
    ser_address=models.CharField(max_length=30,default="")
    ser_contact=models.IntegerField(default=0000)
    ser_mode=models.CharField(max_length=10,default="")
    ser_pdstatus = models.CharField(max_length=10,default="")
    ser_details = models.CharField(max_length=250,default="")
    ser_payment = models.CharField(max_length=10,default="pending")
    ser_bill = models.IntegerField(default=1000)

class Usedvehicle(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    Usedvehicle_regno=models.CharField(max_length=30)
    Usedvehicle_type=models.CharField(max_length=30)
    Usedvehicle_company=models.CharField(max_length=30)
    Usedvehicle_modelname=models.CharField(max_length=30)
    Usedvehicle_regdate=models.DateField(blank=False)
    Usedvehicle_vehcolor=models.CharField(max_length=30)
    Usedvehicle_year=models.IntegerField()
    Usedvehicle_chasisno=models.CharField(max_length=30)
    Usedvehicle_km=models.IntegerField()
    Usedvehicle_price=models.IntegerField()
    Usedvehicle_email=models.EmailField()
    Usedvehicle_phone=models.IntegerField()
    Usedvehicle_info=models.CharField(default="", max_length=100)
    Usedvehicle_rcphoto=models.ImageField(upload_to='main_app/static/main_app/img/usedvehicles', default='patient_icon.png')
    Usedvehicle_photo=models.ImageField(upload_to='main_app/static/main_app/img/usedvehicles', default='patient_icon.png')
    Usedvehicle_verify = models.BooleanField(default="False")


class Vehiclebuyer(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    testslotdate=models.DateTimeField(blank= False)

class VehicleSeller(models.Model):
    Category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    # usedvehicleid=models.ForeignKey(usedvehicle, on_delete=models.CASCADE)
    vehicleseller_regdate=models.DateField(blank=False)


class Accesories(models.Model):
    Accesories_name=models.CharField(max_length=30)
    Accesories_type=models.CharField(max_length=30)
    Accesories_price=models.IntegerField()
    Accesories_description=models.CharField(max_length=100)
    Accesories_photo=models.ImageField(upload_to='main_app/img/accesories', default='patient_icon.png')
    Accesories_quantity=models.IntegerField()
    like = models.IntegerField(default=1)

class Cart(models.Model):
    Cart_date=models.DateField(blank=False)
    Accesories_id=models.ForeignKey(Accesories, on_delete=models.CASCADE)
    Serviceid=models.ForeignKey(Service, on_delete=models.CASCADE)
    Cart_itemqty=models.IntegerField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    Cart_price=models.IntegerField()
    Cart_description=models.CharField(max_length=30)
    
class Order(models.Model):
    Order_id= models.CharField(blank=False, max_length=10, primary_key=True)
    Order_date=models.DateField(blank=False)
    Order_status=models.CharField(max_length=30)
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    Accesories_id=models.ForeignKey(Accesories, on_delete=models.CASCADE)
    cart_id=models.ForeignKey(Cart, on_delete=models.CASCADE)
    Order_approxtime= models.IntegerField()
    

class Paymentstatus(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    Payment_type=models.CharField(max_length=30)
    Payment_price=models.IntegerField()
    Payment_status=models.CharField(max_length=30)
    Payment_recievedate=models.DateField(blank=False,auto_now_add=True)
    Card_type=models.CharField(max_length=30)
    Card_number=models.IntegerField()
    

class Chatbox(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    Chatbox_keyword=models.CharField(max_length=30)
    predefined_id=models.CharField(max_length=30)
    Chatbox_action=models.CharField(max_length=30)
    
class chat(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200,default="hii")
    answer = models.CharField(max_length=200,default="hii")
    time = models.DateTimeField(auto_now_add=True,blank=False)
    
class Feedback(models.Model):
    Feedback_name=models.CharField(max_length=20,default="")
    Feedback_email=models.EmailField(max_length=20,default="")
    Feedback_phono=models.IntegerField(default=99)
    Feedback_subject=models.CharField(max_length=500,default="")
    Feedback_info=models.CharField(max_length=500,default="")
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
   
class Member(models.Model):
    membership_type= models.CharField(max_length=10)
    membership_fname=models.CharField(max_length=10)
    membership_email=models.EmailField()
    membership_phno=models.IntegerField()
    membership_info=models.CharField(max_length=100)
    userid=models.ForeignKey(User, on_delete=models.CASCADE)


class CartTbl(models.Model):
    FkPID = models.ForeignKey(Accesories,on_delete=models.CASCADE)
    Qty = models.IntegerField()
    Total = models.IntegerField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)

class Cartx(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    FkPID = models.ForeignKey(Accesories,on_delete=models.CASCADE)
    Qty = models.CharField(max_length=20)
    Price = models.IntegerField(default=10)
    Total = models.CharField(max_length=20)
    Name=models.CharField(max_length=20,default="abc")
    Photo = models.ImageField(upload_to='main_app/img/cart', default='patient_icon.png')

    

class OrderMasterTbl(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=15,default="fname")
    lname = models.CharField(max_length=15,default="lname")
    cname = models.CharField(max_length=15,default="cname")
    Email = models.EmailField(default="abc@gmail.com")
    phone = models.IntegerField(default=11)
    add1 = models.CharField(max_length=100,default="add1")
    add2 = models.CharField(max_length=100,default="add2")
    city= models.CharField(max_length=20,default="city")
    state = models.CharField(max_length=20,default="state")
    postcode = models.IntegerField(default=11)
    CDate = models.DateTimeField(auto_now=True)
    BillTotal = models.IntegerField(default=11)


class OrderDetails(models.Model):
    FkOrderMasterID = models.ForeignKey(OrderMasterTbl,on_delete=models.CASCADE)
    product = models.CharField(max_length=20,default="abc")
    Qty = models.IntegerField()
    Total = models.IntegerField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=10,default="pending")
    created_at=models.DateTimeField(auto_now_add=True, blank=False)
#payemnt


class updates(models.Model):
    message = models.CharField(max_length=100)

class Transaction(models.Model):
    made_by = models.ForeignKey(Category, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)