from django.shortcuts import render,HttpResponseRedirect,reverse, HttpResponse
from .models import *
from random import *
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.utils.html import strip_tags
from django.core.mail import send_mail

from django import db
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from .models import Transaction
from .checksum import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt

from django.template import Context 
from django.template.loader import get_template 
from django.utils.html import escape 
from xhtml2pdf import pisa 
from io import StringIO, BytesIO 


# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse
# from django.template.loader import render_to_string

# from weasyprint import HTML
# Create your views here.


#contact
#membership form


def IndexPage(request):
    return HttpResponseRedirect(reverse('homepage'))

def Blog(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "blog.html")    

def Emergency(request):
    # if 'email' in request.session and 'role' in request.session:
    return render(request, "need-help.html")
    # else:
        # return render(request, "login.html")

def Profilepic(request):
    if 'email' in request.session and 'role' in request.session:
        if request.method=="POST":
            print("===if===")
            pic = request.FILES['pc']
            print("======1=======")
            id = request.session['id']
            email = request.session['email']
            print("=== Mail : ====",email)
            user = User.objects.get(usermail=email)
            print("======2=======")
            user.userphoto = pic
            user.save()
            print("======3=======")
            return HttpResponseRedirect(reverse("userprofile"))
        else:
            print("===else===")
            return render(request,"userprofile.html")
    else:
        return render(request,"login.html")

def Userprofile(request):
    if 'email' in request.session and 'role' in request.session:
        Email =  request.session['email']
        all_user=User.objects.get(usermail=Email)

        print(all_user)
        
        return render(request,"userprofile.html",{'all_user':all_user})
    else:    
        return render(request,"login.html")

    return render(request,"userprofile.html")

def Passchange(request):
    if 'email' in request.session and 'role' in request.session:
        print("--==-=passchange")
        if request.method=="POST":
            Email =  request.session['email']
            user=Category.objects.get(email=Email)

            print(user)
            old = request.POST['oldpass']
            Pass = request.POST['pass']
            Cpass = request.POST['cpass']
            print("=====")
            op = user.password
        
            if old==op:
                if Pass==Cpass:
                    print("========================if=")
                    user.password = Pass
                    user.save()   
                    return render(request,"login.html")
                else:
                    message="Password and Confirm Password do not matches"
                    return render(request,"passchange.html",{'message':message})
            else:
                message=" old password is incorrect"
                return render(request,"passchange.html",{'message':message})
        
        
        else:
            return render(request, "passchange.html")
    else:
        return render(request,"login.html")

    return render(request, "passchange.html")

def Silverpage(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "silver.html")
    else:
        return render(request, "login.html")

def Goldpage(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "gold.html")
    else:
        return render(request, "login.html")

def Platinumpage(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "platinum.html")
    else:
        return render(request, "login.html")

def About(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "about.html")
    else:
        return render(request, "login.html")


def Team(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "team.html")

def Prize(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "price.html")

def Comingsoon(request):
    return render(request, "coming-soon.html")

def Project(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "project.html")

def Projectdetail(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "project-detail.html")

def Servicedetail(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "service-detail.html")

def Teamdetail(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "team-single.html")

def Testimonial(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "testimonials.html")

def Faq(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "faq.html")

# def Statustable(request):
#     return render(request, "statustable.html")
def Thanks(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request,"thanks.html")

def Comingsoon(request):
    return render(request, "coming-soon.html")

def Blogdetail(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "blog-detail.html")

def Errorpage(request):
    return render(request, "error-page.html")

def Shop(request):
    if 'email' in request.session and 'role' in request.session:
        all_acc = Accesories.objects.all()[:9]
        return render(request, "shop.html",{'all_acc':all_acc})
    else:
        return render(request,"login.html")


def Shop1(request):
    if 'email' in request.session and 'role' in request.session:
        all_acc = Accesories.objects.all()[9:18]
        return render(request, "shop.html",{'all_acc':all_acc})
    else:
        return render(request,"login.html")

def Shop2(request):
    if 'email' in request.session and 'role' in request.session:
        all_acc = Accesories.objects.all()[18:28]
        return render(request, "shop.html",{'all_acc':all_acc})
    else:
        return render(request,"login.html")

def Productdetails(request,pk):
    all_acc = Accesories.objects.get(id=pk)
    return render(request, "product_details.html",{'all_acc':all_acc})

def Like(request,pk):
    print("hoiii")
    all_acc = Accesories.objects.get(id=pk)
    all_acc.like +=1
    all_acc.save()

    return render(request, "product_details.html",{'all_acc':all_acc})

def Cancelorder(request,pk):
    print("====1====")
    order = OrderDetails.objects.get(id=pk)
    order.order_status = "Canceled"
    order.save()
    print(order)
    return HttpResponseRedirect(reverse('trackacc'))

def Cancelveh(request,pk):
    print("====1====")
    veh = Usedvehicle.objects.get(id=pk)
    
    veh.delete()
    print(veh)
    return HttpResponseRedirect(reverse('trackveh'))


@csrf_exempt
def Checkout(request):
    if 'email' in request.session and 'role' in request.session:
        if request.method == "POST":
            Fname = request.POST['fname']
            Lname = request.POST['lname']
            Cname = request.POST['cname']
            Email = request.POST['email']
            Phone = request.POST['phone']
            Add1 = request.POST['add1']
            Add2 = request.POST['add2']
            City = request.POST['city']
            State = request.POST['state']
            Postcode = request.POST['postcode']
            print(Fname)
            print(Phone)
            print("===========================")
            id = request.session['id']
            user = Category.objects.get(id=id)
            cust = User.objects.get(Category_id_id=id)
            print(user.id)
            all_prod = Cartx.objects.filter(userid_id=user.id)
            total = 0
            for t in all_prod:

                x = int(t.Price) * int(t.Qty)
                total += x 
            print("---------")
            neworder = OrderMasterTbl.objects.create(userid_id=cust.id,fname=Fname,lname=Lname,cname=Cname,Email=Email,phone=Phone,add1=Add1,add2=Add2,city=City,state=State,postcode=Postcode,BillTotal=total)    
        
            print("----",neworder.id)
            for prod in all_prod:    
                OrderDetails.objects.create(FkOrderMasterID=neworder,Qty=prod.Qty,Total=prod.Price,product=prod.Name,userid_id=user.id)
                prod.delete()

            return render(request, "cartpay.html",{'total':total})
        else:
            idx=request.session['id']
            user = User.objects.get(Category_id_id=idx)
            all_prod = Cartx.objects.filter(userid_id=user)
            total = 0
            for t in all_prod:
                x = int(t.Price) * int(t.Qty)
                total += x 

            return render(request, "checkout.html",{'total':total})
    else:
        return render(request,"login.html")


def Vehicleinfo(request,pk):
    if 'email' in request.session and 'role' in request.session:
        all_veh = Usedvehicle.objects.get(pk=pk)
        print("==========================")
        print(all_veh)
        return render(request, "vehicleinfo.html" ,{'all_veh':all_veh})    

def Cart(request):
    # print(id)
    if 'email' in request.session and 'role' in request.session:
        idx=request.session['id']
        user = User.objects.get(Category_id_id=idx)
        all_prod = Cartx.objects.filter(userid_id=user)
        total = 0
        for t in all_prod:

            x = int(t.Price) * int(t.Qty)
            t.Total = x
            t.Qty = t.Qty
            # t.Total.save()
            total += x 

        return render(request, "cart.html",{'all_prod':all_prod,'total':total})
    else:
        return render(request,"login.html")

def Sellpage(request):
    if 'email' in request.session and 'role' in request.session:
        all_sell = Usedvehicle.objects.filter(Usedvehicle_verify=True)
        return render(request, "sell.html", {'all_sell':all_sell})
    else:
        return render(request,"login.html")
# def Vehdetails(request):
#     return render(request, "vehdetails.html")

def Membershipform(request):
    if 'email' in request.session and 'role' in request.session:
        print("=============")
        if request.method == "POST":
            Name=request.POST['name']
            Email=request.POST['email'] 
            info=request.POST['info']
            Phone=str(request.POST['phone'])
            Type=request.POST['type']
            mail = request.session['email']
            user=User.objects.get(usermail=mail)
            print(user)
            if user:

                newmember=Member.objects.create(userid=user,membership_type=Type,membership_fname=Name,membership_email=Email,membership_phno=Phone,membership_info=info)                
                # memb=User.objects.get(userid=user)
                print("------------------------------")
                if(Type=="Silver"):
                    
                    print("---------------------1---------")
                    request.session['membership']="silver"
                    print("----------------------------2--")
                    print(request.session['membership'])
                    print("--------------------4----------")
                    total = 599
                    request.session['paid'] = total
                    return render(request, "cartpay.html",{'total':total})
                    
                    
                elif(Type=="Gold"):
                    print("=======gold====")
                    request.session['membership']="gold"
                    print(request.session['membership'])
                    total = 1599
                    request.session['paid'] = total
                    return render(request, "cartpay.html",{'total':total})   
                    
                elif(Type=="Platinum"):
                    user.userremservice+=5
                    request.session['membership']="platinum"
                    print(request.session['membership'])
                    total = 2599
                    request.session['paid'] = total
                    return render(request, "cartpay.html",{'total':total})
                    
                return HttpResponseRedirect(reverse('comingsoon'))
            else:

                return render(request, "login.html")
        else:
            request.session['membership']=""
            return render(request, "membershipform.html")
    else:
        return render(request, "login.html")
        
def AddToCart(request):
    if 'email' in request.session and 'role' in request.session:
        try:
            print("/n/n====",request.GET)
            idx=request.session['id']
            user = Category.objects.get(id=idx)
            pid = request.GET.get("pid")
            p_obj = Accesories.objects.get(pk=int(pid))
            print("=====1=======")
            qty = request.GET.get("qty")
            price = request.GET.get("price")
            total = int(qty) * int(price)
            print("=====2=======")
            cartitem = CartTbl.objects.create(
                FkPID = p_obj,
                Qty = qty,
                Total = total,
                userid = user  
            )
            print("=====3=======")
            return HttpResponse('1')
        except Exception as e:
            print("\n\nError ===",e)
            return HttpResponse('0')
    else:
        return render(request, "login.html")


def AddCart(request,pk):
    if 'email' in request.session and 'role' in request.session:
        item=Accesories.objects.get(pk=pk)
        x= int(item.Accesories_price)
        n= item.Accesories_name
        print("===" ,x)
        idx=request.session['id']
        pic = item.Accesories_photo
        price = item.Accesories_price
        q=1
        user = User.objects.get(Category_id_id=idx)
        print("------------------------------")
        print(item)
        newitem=Cartx.objects.create(FkPID = item,Qty =q,Total = x,userid = user,Name = n,Photo=pic,Price=price)
    
        return HttpResponseRedirect(reverse("shop"))
    else:
        return render(request,"login.html")

def DeleteProduct(request,pk):
    if 'email' in request.session and 'role' in request.session:
        print("--------------")
        p_obj = Cartx.objects.get(pk=pk)
        p_obj.delete()
        return HttpResponseRedirect(reverse("cart"))
    else:
        return render(request,"login.html")

def Updatecart(request,pk):
    if 'email' in request.session and 'role' in request.session:
        print("--------------")
        if request.method=="POST":
            print("=====POST : ====",request.POST)
            p_obj = Cartx.objects.get(pk=pk)
            print("-----")
            print("QT====",request.POST.get('qt'))
            p_obj.Qty=request.POST['qt']
            print("------qty=====",p_obj.Qty)
            p_obj.save()
            return HttpResponseRedirect(reverse("cart"))

        return HttpResponseRedirect(reverse("cart"))
    else:
        return render(request,"login.html")

def Cartpayment(request):
    if 'email' in request.session and 'role' in request.session:
        all_prod = Cartx.objects.all()
        total = 0
        for t in all_prod:

            x = int(t.Total)
            total += x 

        return render(request, "cartpay.html",{'total':total})
    else:
        return render(request,"login.html")
    

def Vehiclesell(request):
    if 'email' in request.session and 'role' in request.session:
        print("=============")
        if request.method == "POST":
            print("=============")
            Vregno=request.POST['regnp']
            Vname=request.POST['vname']
            Vtype=request.POST['vtype']
            Vcolor=request.POST['vcolor']
            Vcomp=request.POST['comp']
            Vemail=request.POST['mail']
            Vphno=request.POST['no']
            Vregd=request.POST['rdate']
            Vyear=request.POST['year']
            Vkm=request.POST['km']
            Vcno=request.POST['cno']
            Vprice=request.POST['price']
            Vrc=request.FILES['rc']
            Vpic=request.FILES['vpic']
            Vinfo=request.POST['info']
            email=request.session['email']
            user=User.objects.get(usermail=email)
            print(user)
            print("--------------")

            newsell = Usedvehicle.objects.create(userid=user,Usedvehicle_regno=Vregno,Usedvehicle_type= Vtype,Usedvehicle_company=Vcomp,
            Usedvehicle_modelname=Vname,Usedvehicle_regdate=Vregd,Usedvehicle_vehcolor=Vcolor,Usedvehicle_year=Vyear,
            Usedvehicle_chasisno=Vcno,Usedvehicle_km=Vkm,Usedvehicle_price=Vprice,Usedvehicle_email=Vemail,
            Usedvehicle_phone=Vphno,Usedvehicle_rcphoto=Vrc,Usedvehicle_photo=Vpic,Usedvehicle_info=Vinfo)

            # return HttpResponseRedirect(reverse('comingsoon'))
            
            print(Vregno)
            print(Vcno)
            print(Vemail)
            return HttpResponseRedirect(reverse('comingsoon'))
        else:
            return render(request, "sellerform.html")

    else:
        return render(request, "login.html")


def Contact(request):
    if 'email' in request.session and 'role' in request.session:
        print("=============")
        if request.method == "POST":
            print("=============")
            Fname=request.POST['username']
            Femail=request.POST['email']
            Fphone=request.POST['phone']
            Fsubject=request.POST['subject']
            Fmessage=request.POST['message']
            email=request.session['email']
            print("=============")
            user=User.objects.get(usermail=email)
            print(user)
            newfeedback=Feedback.objects.create(Feedback_name=Fname,Feedback_email=Femail,Feedback_info=Fmessage,Feedback_subject=Fsubject,userid=user)
            return HttpResponseRedirect(reverse('comingsoon'))
        else:
            return render(request, "contact.html")
    else:
        return render(request, "login.html")

def Changepass(request):
    
    if request.method == "POST":
        Otp = int(request.POST['otp'])
        Pass = request.POST['pass']
        Cpass = request.POST['cpass']
        mail = request.session['xmail']
        user = Category.objects.get(email=mail)
        print(user)
        print(user.otp)
        otp = int(user.otp)
        if Otp==otp:
            if Pass==Cpass:
                print("========================if=")
                user.password = Pass
                user.save()   
                return render(request,"login.html")
            else:
                message="Password and Confirm Password do not matches"
                return render(request,"changepass.html",{'message':message})

        else:
            message="otp is not true"
            return render(request,"changepass.html",{'message':message})

    else:
        return render(request,"changepass.html")

    # return render(request,"changepass.html")

def Forgotpassword(request):
    
        if request.method == "POST":
            mail=request.POST['email']
            try:
                user = Category.objects.get(email=mail)
                print(user)
                print(user.otp)
                otp = user.otp
                request.session['xmail']=mail
            
        # email=request.POST['email']

                html_message='''
                <html>
                <body>
                <p> Welcome %s and Link  is  : %s </p>
                </body>
                </html>

                '''%(mail,otp)

                plain_message=strip_tags(html_message)

                send_mail("my subject",plain_message,'motorworkexpert@gmail.com',[mail],html_message=html_message)
                return render(request, "changepass.html")
            except Exception as e:
                
                message = "Email doesn't Exist"
                return render(request, "forgotpassword.html",{'message':message})
        else:
            return render(request, "forgotpassword.html")

def Editprofile(request):
    if request.method=="POST":
        Name = request.POST['name']
      
        Phone = int(request.POST['phone'])
        Address = request.POST['address']
        Gender = request.POST['gender']
        print("Name",Name)
        
        print(Phone)
        print(Address)
        print(Gender)
        id = request.session['id']
        user = User.objects.get(Category_id=id)
        print(user)
        user.username= Name
        
        user.userphone = Phone
        user.useraddress = Address
        user.usergender = Gender
        user.save()
        return HttpResponseRedirect(reverse('userprofile'))

    else:
        id = request.session['id']
        user = User.objects.get(Category_id=id)
        print(user)
        return render(request, "editprofile.html",{'user':user})

def Email(request):
    
    uname="premal"
    pwd="123"
    email='premal058@gmail.com'
    html_message='''
    <html>
    <body>
    <p> Welcome %s and pass is %s</p>
    </body>
    </html>

    '''%(uname,pwd)

    plain_message=strip_tags(html_message)

    send_mail("my subject",plain_message,'motorworkexpert@gmail.com',[email],
        html_message=html_message)
        # ,fail_silently=True
    return render(request, "login.html")

def vehEmail(request,pk):
    if 'email' in request.session and 'role' in request.session:

        if request.method=="POST":
        
            idx=int(request.session['id'])
            print(idx)

            all_veh = Usedvehicle.objects.get(pk=pk)
            all_user= Category.objects.get(pk=idx)
            buy=User.objects.get(Category_id_id=all_user)
   
            email=all_veh.Usedvehicle_email
            Date = request.POST['date']
            Time = request.POST['time']
            print(Date)
            print(Time)
            html_message='''
            <html>
            <body>
            <h3>Regards someone showing interest to Your Registered Vehicle having Number %s</h3><br><h4> User details :</h4><br><br> <p>User Name: %s<br>User Email : %s <br>User Contact_No: %s 
            <br>Preferable testing Date : %s <br> Preferable testing Date : %s <br>
            </p>    
            <br>
            <br>
            <p>Your feedback about our services will be helpfull to us to give more better services to you in future..</p>
            <p>Thank you.</p>
            <p> Regards Motor Work Experts</p>
            </body>
            </html>

            '''%(all_veh.Usedvehicle_regno,buy.username,buy.usermail,buy.userphone,Date,Time)

            plain_message=strip_tags(html_message)

            send_mail("Interested Buyer Request",plain_message,'motorworkexpert@gmail.com',[email],
            html_message=html_message)


            print(buy.useraddress)
            print(buy.usermail)
            mal = buy.usermail
            xyz = all_veh.Usedvehicle_email
            seller = User.objects.get(usermail=xyz)
            print(seller.useraddress)
            html_message='''
            <html>
            <body>
            <h3>This mail is the confirmation of your showed interest in the vehicle %s..! </h3><br><h4> User details :</h4><br><br> <p>Your Name: %s<br>Seller Email : %s <br>Seller address: %s 
            <br>Preferable testing Date : %s <br> Preferable testing Date : %s <br>
            <br>
            <br>
            <h2>Notice:-You are requested to reach at the seller's given address at your given Date and time ..<br>
            Your co-opreation will make this deal faster and better..!</h2>
                </p>
            <br>
            <br>
            <p>Your feedback about our services will be helpfull to us to give more better services to you in future..</p>
            <p>Thank you.</p>
            <p> Regards Motor Work Experts</p>
            </body>
            </html>

            '''%(all_veh.Usedvehicle_regno,buy.username,seller.usermail,seller.useraddress,Date,Time)

            plain_message=strip_tags(html_message)

            send_mail("Test slot confirmed..!",plain_message,'motorworkexpert@gmail.com',[mal],
            html_message=html_message)
        
            return HttpResponseRedirect(reverse('comingsoon'))

        else:
            return render(request, "vehicleinfo.html" ,{'all_veh':all_veh})
    
    
        return render(request, "vehicleinfo.html" ,{'all_veh':all_veh})
    else:
        return render(request,"login.html")
    

def Appointment(request):

    if 'email' in request.session and 'role' in request.session:
        print("\n\n Method == ",request.method,"\n\n")
        if request.method == "POST":
            Year=request.POST['year']
            Type=request.POST['type']
            Mileage=request.POST['milg']
            Date=request.POST['date']
            Time=request.POST['time']
            Address=request.POST['address']
            Mil=request.POST.get('Mileage')
            Brk=request.POST.get('brake')
            eng=request.POST.get('Engine')
            Heat=request.POST.get('heat')
            Steering=request.POST.get('steering')
            Chain=request.POST.get('chain')
            Battery=request.POST.get('battery')
            Rservice=request.POST.get('rservice')
            Wash=request.POST.get('wash')
            Pvt=request.POST.get('pvt')
            Tire=request.POST.get('tire')
            Tires=request.POST.get('tires')
            Other=request.POST.get('other')
            Number=request.POST['number']
            Name=request.POST['name']
            Email=request.POST['email'] 
            info=request.POST['info']
            Phone=str(request.POST['phone'])
            Delivery=request.POST['delivery']

            email=request.session['email']
            user=User.objects.get(usermail=email)
            print(user)
            list = [Mil,Brk,eng,Heat,Steering,Chain,Battery,Rservice,Wash,Pvt,Tire,Tires,Other]
            newappointment=appointment.objects.create(vehicle_number=Number,vehicle_year=Year,vehicle_type=Type,vehicle_mileage=Mileage,vehicle_appdate=Date,vehicle_apptime=Time,vehicle_need=list,vehicle_username=Name,vehicle_useremail=Email,vehicle_address=Address,vehicle_mode=Delivery,vehicle_contact=Phone,vehicle_info=info,userid=user)        
            return HttpResponseRedirect(reverse('comingsoon'))

        else:
            return render(request,"appointment.html")
    else:
        return render(request,"login.html")

        # return HttpResponse(list)

    # return render(request,"appointment.html")

def services(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request,"services.html")
    else:
        return render(request,"login.html")

# def appointmentvehicle(request):
#     try:
#         if 
def Changepic(request):
    if 'email' in request.session and 'role' in request.session:
        if request.method=="POST":
            print("===if===")
            pic = request.FILES['pc']
            print("======1=======")
            id = request.session['id']
            email = request.session['email']
            print("=== Mail : ====",email)
            user = Foreman.objects.get(Foreman_email=email)
            print("======2=======")
            user.Foreman_photo = pic
            user.save()
            print("======3=======")
            return HttpResponseRedirect(reverse("fprofile"))
        else:
            print("===else===")
            return render(request,"fprofile.html")
    else:
        return render(request,"login.html")

def Verifyotp(request):

    if request.method == "POST":
        a = int(request.POST['otp'])
        x = request.session['xmail']
        print("User input====",a)
        cat = Category.objects.get(email=x)
        print(x)
        o = int(cat.otp)
        print(cat.otp)
        print(o)
        print("=========================")
        if(a==o):
            print("========================if=")
            cat.is_verified = True 
            cat.save()   
            del request.session['xmail']
            return render(request,"login.html")
        else:
            print("=========================else    ")
            return render(request,"verifyotp.html")

    else:
        return render(request,"verifyotp.html")

    return render(request,"verifyotp.html")


def Register(request):
    try:
        # print("kill start")
        # db.connections.close_all()
        # print("Kill")
        if request.POST['role']=="Customer":
            role = request.POST['role']
            name= request.POST['name']            
            password = request.POST['password']
            confirmpassword =request.POST['conpassword']
            gender = request.POST['gender']
            email =request.POST['email']
            mobile = str(request.POST['phone'])
            address = request.POST['address']
            # imagepic= request.FILES['image']

            print("===========1================")

            category = Category.objects.filter(email=email)
            print("============2===============")
            if category:
                message = "user already exists"
                return render(request,"login.html",{'message':message})
            else:
                if password!="" and password==confirmpassword:               
                    ran_num = randint(100000,999999)               
                    newcategory = Category.objects.create(email=email,password=password,role=role,otp=ran_num)                
                    newcustomer = User.objects.create(Category_id=newcategory,username=name,userpass=password,usergender=gender,useraddress=address,usermail=email,userphone=mobile)

                    html_message='''
                    <html>
                    <body>
                    <p> Welcome %s and OTP is %s</p>
                    </body>
                    </html>

                    '''%(name,ran_num)

                    plain_message=strip_tags(html_message)

                    send_mail("my subject",plain_message,'motorworkexpert@gmail.com',[email],
                        html_message=html_message)
                    print("12..........")
                    request.session['xmail']=email
                    print("12..........ww")
                    # return HttpResponseRedirect(reverse("verifyotp"))
                    return render(request,"verifyotp.html")
                    
                else:
                    message = "password does not match"
                    return render(request,"login.html",{'message':message})

        elif request.POST['role']=="Foreman":
            
            
            role = request.POST['role']
            name= request.POST['name']            
            password = request.POST['password']
            confirmpassword =request.POST['conpassword']
            gender = request.POST['gender']
            email =request.POST['email']
            mobile = str(request.POST['phone'])
            address = request.POST['address']

            category = Category.objects.filter(email=email)
            if category:
                message = "user already exists"
                return render(request,"login.html",{'message':message})
            else:
                if password==confirmpassword:
                    otp = randint(100000,999999)
                    newcategory = Category.objects.create(
                        email=email,password=password,role=role,otp=otp,is_active=False)
                    newforeman = Foreman.objects.create(Category_id=newcategory,Foreman_name=name,Foreman_gender=gender,Foreman_email=email,Foreman_contact=mobile,Foreman_password=password,Foreman_address=address)
                    html_message='''
                    <html>
                    <body>
                    <p> Welcome %s and OTP is %s</p>
                    <p> After verifying with OTP our Admin will approve or disaprove you
                    for further processes.</p>
                    <br>
                    <p>Kindly wait for the confirmation</p>
                    </body>
                    </html>

                    '''%(name,otp)

                    plain_message=strip_tags(html_message)

                    send_mail("my subject",plain_message,'motorworkexpert@gmail.com',[email],
                        html_message=html_message)
                    print("12..........")
                    request.session['xmail']=email
                    print("12..........ww")
                    return HttpResponseRedirect(reverse("verifyotp"))
                    

                else:
                    message = "password does not match"
                    return render(request,"login.html",{'message':message})
        else:
            message = "Please Select roll"
            return render(request,"login.html",{'message':message})            
        #patient    

    except Exception as e:
        print("\n\n================Error===",e)
    # except Category.DoesNotExist:
        # message= '
        return render(request,"login.html")
        # ",{'message':message}

def Logout(request): 
    if 'email' in request.session and 'role' in request.session:
        # e = request.session['email']
        # print(request.session['email'] )
        del request.session['email'] 
        del request.session['role'] 
        del request.session['username'] 
        del request.session['id']
        return HttpResponseRedirect(reverse('register')) 
    else:
        return render(request, "login.html")
    # else:
    #     return HttpResponseRedirect(reverse('register')) 

def xx(request):
    return render(request,"xx.html")

def LoginUser(request):
    if request.method=="POST":
        email= request.POST['mail']
        password= request.POST['password']
        try:
            category=Category.objects.get(email=email)
            if category.role=="Customer":
                # email= request.POST['mail']
                # password= request.POST['password']

                # category=Category.objects.get(email=email)
                if(category.is_verified==True):
                    print(category)
                    print("user 1-------------")
                    if category:
                        if category.password==password and category.role=="Customer":
                            customer = User.objects.get(Category_id=category)
                            request.session['email']=category.email
                            request.session['username']=customer.username
                            request.session['role']=category.role
                            request.session['id']=category.id
                            request.session['membership']="1"
                            request.session['bill']=0
                            request.session['vid']=0

                            print("user 2-------------")
                            return HttpResponseRedirect(reverse('homepage'))
                        else:
                            message1="Your password is incorrect or user do not exist"
                            return render(request,"login.html",{'message1':message1})
                    else:
                        message1=" user do not exist or Password is incorrect"
                        return render(request,"login.html",{'message1':message1})

                else:
                    request.session['xmail']=email
                    return HttpResponseRedirect(reverse("verifyotp"))

            elif category.role=="Foreman":
                # email= request.POST['mail']
                # password= request.POST['password']

                # category=Category.objects.get(email=email)
                print("Foreman -------------")
                if(category.is_verified==True):
                    print(category)
                    print("user 1-------------")
                    if category and category.is_active==True:
                        if category.password==password and category.role=="Foreman":
                            foreman = Foreman.objects.get(Category_id=category)
                            request.session['email']=category.email
                            request.session['username']=foreman.Foreman_name
                            request.session['role']=category.role
                            request.session['id']=category.id

                            return HttpResponseRedirect(reverse('homepage'))
                        else:
                            message1="Your password is incorrect or user do not exist"
                            return render(request,"login.html",{'message1':message1})
                    else:
                        message1=" user do not exist or check your password  or wait till Admin Confirmation"
                        return render(request,"login.html",{'message1':message1})
                else:
                    message="You are not yet verified"
                    request.session['xmail']=email
                    return HttpResponseRedirect(reverse("verifyotp"))

            # elif request.POST['role']=="Admin":
                    # id= "premal058@gmail.com"
                # pass = "123"
                # email= request.POST['mail']
                # password= request.POST['password']  
                # role=request.POST['role']
            
                # print("admin -------------")

            elif category.role=="Admin": 
                if password=="Premal@123" and email=="premal058@gmail.com":
                    request.session['email']=email
                    request.session['username']="premal"
                    request.session['role']="Admin"
                    request.session['id']="03"
                    return HttpResponseRedirect(reverse('homepage'))


                else:
                    message1=" user do not exist"
                    return render(request,"login.html",{'message1':message1})

            else:
                message1=" user do no exist"
                return render(request,"login.html",{'message1':message1})
                # return render(request,"login.html")
                # if email=="premal3@gmail.com" and    
                #  
        except Exception as e:

            print("\n\n================Error===",e)
        # except Category.DoesNotExist:
            message1= 'User does not exist'
            return render(request,"login.html",{'message1':message1})

def homepage(request):
    if 'email' in request.session and 'role' in request.session:
        if request.session['role']=="Customer":
            # all_customer = User.objects.all()
            # all_foreman = Foreman.objects.all()
            # return HttpResponse(email)
          
            return render(request,"index.html")
            # {'all_customer':all_customer,'all_foreman':all_forem,an})
        elif request.session['role']=="Foreman":
            # all_foreman = Foreman.objects.all()
            all_vehicle = appointment.objects.all()
            acc = serviceaccept.objects.all().count()
            done =  Servicedone.objects.all().count()
            upd = updates.objects.all().count()
            picku = pickup.objects.filter(status="pending")
            pick = 0
            for i in picku:
                pick += 1
        
            return render(request, "findex.html",{'acc':acc,'done':done,'upd':upd,'pick':pick})
            # return render(request, "findex.html")
            # return render(request,"foremanvehicle.html",{'all_vehicle':all_vehicle})

        elif request.session['role']=="Admin":
            x = User.objects.all()
            le = len(x)
            order = OrderDetails.objects.all().count()
            print(order)
            amt = Transaction.objects.all()
            total=0
            for i in amt:
                total += i.amount

            print(total)
            feedback = Feedback.objects.all().count()

            used = Usedvehicle.objects.all().count()
            done = Servicedone.objects.all().count()
            acc = serviceaccept.objects.all().count()
            rej= servicereject.objects.all().count()
            app = appointment.objects.all().count()
            x = done + acc + rej + app

            acc = Accesories.objects.all().count()
            auser = OrderMasterTbl.objects.all().count()
            order1 = OrderDetails.objects.all()
            sold = 0
            for j in order1:
                sold += j.Qty 

            return render(request,"adminpanel.html",{'le':le,'order':order,'total':total,'feedback':feedback,'used':used,'done':done,'x':x,'acc':acc,'auser':auser,'sold':sold})
            # return render(request,"foremanvehicle.html")
    else:
        
        message=" user do no exist"
        return render(request,"login.html",{'message':message})


#foreman			
def foremanvehicle(request):
    if 'email' in request.session and 'role' in request.session:
        all_vehicle = appointment.objects.all()
            
        return render(request,"foremanvehicle.html",{'all_vehicle':all_vehicle})
    else:
        return render(request,"login.html")

def Foremanindex(request):
    if 'email' in request.session and 'role' in request.session:
        print(request.session['email'])
        acc = serviceaccept.objects.all().count()
        done =  Servicedone.objects.all().count()
        upd = updates.objects.all().count()
        picku = pickup.objects.filter(status="pending")
        pick = 0
        for i in picku:
            pick += 1
        
        return render(request, "findex.html",{'acc':acc,'done':done,'upd':upd,'pick':pick})
    else:
        return render(request,"login.html")

def Forcard(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "forcard.html")
    else:
        return render(request, "login.html")

def Facc(request):
    if 'email' in request.session and 'role' in request.session:
        id="accept"
        all_vehicle = appointment.objects.filter(vehicle_status=id)
        return render(request,"accept.html",{'all_vehicle':all_vehicle})
    else:
        return render(request,"login.html")

def Aacc(request):
    if 'email' in request.session and 'role' in request.session:
        all_vehicle = serviceaccept.objects.all()
        return render(request,"aacc.html",{'all_vehicle':all_vehicle})	
    else:
        return render(request,"login.html")

def Frej(request):
    if 'email' in request.session and 'role' in request.session:
        id="reject"
        all_vehicle = appointment.objects.filter(vehicle_status=id)
        return render(request,"reject.html",{'all_vehicle':all_vehicle})
    else:
        return render(request,"login.html")

def Fprofile(request):
    if 'email' in request.session and 'role' in request.session:
        print("====")
        Email =  request.session['email']
        print(Email)
        all_user=Foreman.objects.get(Foreman_email=Email)

        print(all_user)
        
        return render(request,"fprofile.html",{'all_user':all_user})
    else:    
        return render(request,"login.html")

    return render(request,"fprofile.html")

def Editfor(request):
    if 'email' in request.session and 'role' in request.session:
        if request.method=="POST":
            print("Edit Foreman Profile")
            Name = request.POST['name']
            # Mail = request.POST['email']
            Phone = int(request.POST['phone'])
            Address = request.POST['address']
            Gender = request.POST['gender']
            print("Name",Name)
            # print(Mail)
            print(Phone)
            print(Address)
            print(Gender)
            id = request.session['id']
            user = Foreman.objects.get(Category_id_id=id)
            print(user)
            user.Foreman_name= Name
            # user.usermail = Mail
            user.Foreman_contact = Phone
            user.Foreman_address = Address
            user.Foreman_gender = Gender
            user.save()

            return HttpResponseRedirect(reverse('fprofile'))
        else:
            id = request.session['id']
            user = Foreman.objects.get(Category_id_id=id)
            print(user)
            return render(request, "editfor.html",{'user':user})

    else:    
        return render(request,"login.html")
   
#def Pickdrop(request):

def Forapproval(request):
    foreman = Foreman.objects.all()
    category = Category.objects.filter(is_active=False)
    return render(request, "forapproval.html",{'foreman':foreman,'category':category})

def Forapprove(request,pk):
    category1 = Category.objects.get(pk=pk)
    category1.is_active = True  
    category1.save()
    email = category1.email
    html_message='''
    <html>
    <body>
    <p> Welcome %s</p>
    <p> Your profile is verified and you can login and access the system</p>
    <br>
    <p>Thank you. All the Best <br>Regards from MotorWork Expert</p>
    </body>
    </html>

    '''%(email)

    plain_message=strip_tags(html_message)

    send_mail("Confirmation from MotorWork Expert",plain_message,'motorworkexpert@gmail.com',[email],
        html_message=html_message)
    return HttpResponseRedirect(reverse('forapproval'))

def Rejectpage(request):
    if 'email' in request.session and 'role' in request.session:
        email=request.session['email']
        rej=appointment.objects.get(vehicle_useremail=email)
        print("---------------------------")
        x=rej.vehicle_status
        print(x)
        return render(request,"appointment.html")
    else:
        return render(request,"login.html")

def statuspage(request):
    if 'email' in request.session and 'role' in request.session:

        user = User.objects.get(Category_id=request.session['id']) 
        allcase = appointment.objects.filter( 
        userid=user) 
        print(allcase) 
    # for i in allcase:
    #     print(i.userid)
    #     print(i.vehicle_number)
    #     print(i.vehicle_status)
        
    #     if(i.vehicle_status=="accept"):
    #         print("hii")
    #     else:
    #         print("Bye")
    #     print("\n")
    # all_service=appointment.objects.get(useremail=email)
    # return render(request,"statuspage.html",{'all_service':all_service})
        return render(request, "statustable.html", {'allcase':allcase})
    else:
        return render(request,"login.html")

    # return render(request, "statustable.html")

def Acceptance(request,pk):
    if 'email' in request.session and 'role' in request.session:
        accept=appointment.objects.get(pk=pk)
        print("------------------------------")
        accept.vehicle_status=request.POST['status']
        accept.save()   
        x = accept.vehicle_mode 
        y = 0
        newservice = serviceaccept.objects.create(veh_status=accept.vehicle_status,veh_number=accept.vehicle_number,veh_year=accept.vehicle_year,veh_type=accept.vehicle_type,veh_mileage=accept.vehicle_mileage,veh_appdate=accept.vehicle_appdate,veh_apptime=accept.vehicle_apptime,veh_need=accept.vehicle_need,veh_username=accept.vehicle_username,veh_useremail=accept.vehicle_useremail,veh_address=accept.vehicle_address,veh_mode=accept.vehicle_mode,veh_contact=accept.vehicle_contact,veh_info=accept.vehicle_info,userid=accept.userid)
        y = "Pick & Dro"
        if (x==y):
            st = "pending"
            # newpick = pickup.objects.create(vehid=newservice,status=st) 
            newservice.veh_pdstatus = st
        accept.delete()
        return HttpResponseRedirect(reverse("forstatus"))
    else:
        return render(request, "login.html")


def Reject(request,pk):
    if 'email' in request.session and 'role' in request.session:
        reject=appointment.objects.get(pk=pk)
        reject.vehicle_status=request.POST['status']
        reject.save()
        newservice = servicereject.objects.create(rej_number=reject.vehicle_number,rej_year=reject.vehicle_year,rej_type=reject.vehicle_type,rej_mileage=reject.vehicle_mileage,rej_appdate=reject.vehicle_appdate,rej_apptime=reject.vehicle_apptime,rej_need=reject.vehicle_need,rej_username=reject.vehicle_username,rej_useremail=reject.vehicle_useremail,rej_address=reject.vehicle_address,rej_mode=reject.vehicle_mode,rej_contact=reject.vehicle_contact,rej_info=reject.vehicle_info,userid=reject.userid)
        reject.delete()
        return HttpResponseRedirect(reverse("forstatus"))
    else:
        return render(request,"login.html")

def pickdrop(request):
    if 'email' in request.session and 'role' in request.session:
        id="Pick & Drop"
        s = "pending" 
        x = ""
        # id="gj02sf8627"
        print("===----===---=-=-====-----==--==")
        all_vehicle = serviceaccept.objects.filter(veh_mode=id,veh_pdstatus=x)
        print("==--00--99--==") 
        sa = "pending"
        for t in all_vehicle:

            print((t.veh_useremail))
            # all_user = User.objects.get()

        # print(all_vehicle.userid_id)
        # all_user = User.objects.filter(id=all_vehicle.userid_id)
        # all_vehicle = appointment.objects.get(vehicle_number=id)
        # print(all_vehicle.vehicle_mode)
        print("------------")
        print(all_vehicle)

        return render(request,"pick.html",{'all_vehicle':all_vehicle})
    else:
        return render(request,"login.html")

def pickdetails(request,pk):
    veh = serviceaccept.objects.get(pk=pk)

def Uservehicle(request,pk):
    if 'email' in request.session and 'role' in request.session:
        veh = serviceaccept.objects.get(pk=pk)
        print(veh)
        print(veh.userid)
        idx = veh.userid
        x = veh.veh_useremail
        print(x)
        all_user = User.objects.get(usermail=x)
        if all_user:
        
            return render(request, "pickdetails.html",{'all_user':all_user,'veh':veh})
        else:
            return render(request, "login.html")

def Vehicleverify(request):
    if 'email' in request.session and 'role' in request.session:

        used = Usedvehicle.objects.filter(Usedvehicle_verify=False)
        return render(request, "vehicleused.html",{'used':used})
    else:
        return render(request,"login.html")

def Vehapproval(request,pk):
    if 'email' in request.session and 'role' in request.session:
        apr = Usedvehicle.objects.get(pk=pk)
        apr.Usedvehicle_verify = True
        apr.save()


        email= apr.Usedvehicle_email
        html_message='''
        <html>
        <body>
        <p> Welcome your vehicle %s is successfully registered on our site...</p>
        </body>
        </html>

        '''%(apr.Usedvehicle_regno)

        plain_message=strip_tags(html_message)

        send_mail("my subject",plain_message,'motorworkexpert@gmail.com',[email],
        html_message=html_message)
    

        print("-=-==-=-=-=--=-=-==-=")
        return HttpResponseRedirect(reverse("vehicleverify"))
    else:
        return render(request,"login.html")

def Vehreject(request,pk):
    if 'email' in request.session and 'role' in request.session:
        apr = Usedvehicle.objects.get(pk=pk)
        email= apr.Usedvehicle_email
        html_message='''
        <html>
        <body>
        <p> Welcome your vehicle %s is not registered on our site...</p>
        </body>
        </html>

        '''%(apr.Usedvehicle_regno)

        plain_message=strip_tags(html_message)

        send_mail("my subject",plain_message,'motorworkexpert@gmail.com',[email],
            html_message=html_message)

        apr.delete()

        print("-=-==-=-=-=--=-=-==-=")
        return HttpResponseRedirect(reverse("vehicleverify"))
    else:
        return render(request,"login.html")


def Pdstatus(request,pk):
    if 'email' in request.session and 'role' in request.session:
        st = "accept"
        x = "Done"
        veh = serviceaccept.objects.get(pk=pk)
        id = request.session['id']
        cat = Category.objects.get(id=id)
        veh.veh_pdstatus = x
        veh.save()
        newpick = pickup.objects.create(vehid=veh,status=veh.veh_status,forid=cat) 
        return HttpResponseRedirect(reverse("pick"))
    else:
        return render(request,"login.html")

def Servicedon(request,pk):
    if 'email' in request.session and 'role' in request.session:
        if request.method=="POST":
            print("--------1----------------")
            det = request.POST['info']
            print("--------2----------------")
            accept = serviceaccept.objects.get(pk=pk)
            print(accept) 
            print("--------3----------------")
            id = request.session['id']
            print("--------4----------------")
            print(accept.veh_number)
            cat = Category.objects.get(id=id)
            print("--------5----------------")
            newservice = Servicedone.objects.create(ser_details=det,forid=cat,
            ser_status=accept.veh_status,ser_number=accept.veh_number,ser_year=accept.veh_year,
            ser_type=accept.veh_type,ser_mileage=accept.veh_mileage,ser_appdate=accept.veh_appdate,
            ser_apptime=accept.veh_apptime,ser_need=accept.veh_need,ser_username=accept.veh_username,
            ser_useremail=accept.veh_useremail,ser_address=accept.veh_address,ser_mode=accept.veh_mode,
            ser_contact=accept.veh_contact,ser_info=accept.veh_info,userid=accept.userid,
            ser_pdstatus=accept.veh_pdstatus)
            print("--------6----------------")
            accept.delete()
            print("--------7----------------")
            return HttpResponseRedirect(reverse("findex"))
        else:
            return HttpResponseRedirect(reverse("forstatus"))
    else:
        return render(request,"login.html")

def Invoice(request):
    if 'email' in request.session and 'role' in request.session:
        all_vehicle = Servicedone.objects.all()
        return render(request,"invoice.html",{'all_vehicle':all_vehicle})	
    else:
        return render(request,"login.html")

def Generateinvoice(request,pk):
    if 'email' in request.session and 'role' in request.session:
        done = Servicedone.objects.get(pk=pk)
    
        print(done)
        print(done.userid)
        idx = done.userid
        x = done.ser_useremail
        print(x)
        all_user = User.objects.get(usermail=x)
        print("==-=-=-=-=-=-=-=-=")
        x = done.ser_need 
        val = done.ser_details
        print(val)
        # x= list(filter(None, x))
        # print(x)
        y = x.split(", ")
        print(y)
        # y = list(filter(None, y))
        print('**************')
        print("==========") 
        # print(y)
        print("-------------------------")
        a = x.replace('None',"")
        c = 0   
        print(a)
        print("[][][[{}}}{}{}{}{}{}")
        str1 = ""
        for y in a:
            if(y==','):
                if(c==0):
                    if(y!=','):
                        str1 = str1  + y
                        c = c + 1
                else:
                    c = 0
            else:
                str1 = str1  + y
        str1 = str1[1:-1]
        print(str1)
        print("[[============================]]")
        # o = []
        w = list(a.split(","))
        print(w)
        l = []
        # for j in w:
    #     for lp in j:
    #         # if(lp=="'")
    #         if(lp>='a' and lp<='z' or lp>'A' and lp<'Z'):
    #             l +=j

    # print("L :: s",l)
    # print(w[0])
    # print(w[1])
    # print(w[2])
    # l = []
    # for i in w:
    #     if(i==)
        d = {}
        d[0] = "service"
        c = 1
        for i in w:
            ln = len(i)
            if(i!=" " and ln>2):
            # if(i.isspace()==False):
            # print(i.isspace())
                d[c] = i
                c+=1

        # for a,b in d.items():
        #     print(b)
        #     if(b==" "):
        #         d.pop(a)
        mem = all_user.userremservice
        discount=0
        if(mem>=1):
            discount = 200
            mem = mem - 1 
            all_user.userremservice = mem
            all_user.save()


        print("\n\n\n==>dict : ",d)
        le = len(d)
        print(le)
        total = le * 200
        if(discount!=0):
            total = total - 200

        print(discount)
        print(total)
    # for i in d:

    #     if(j=="' '"):
    #         print("----")
    #     else:
    #         o.append(j)
    #         print(j)
        print("===++++++++====")
    # for val in w: 
    #     if val != None : 
    #         o.append(val) 
        # l=[]
    # st=""
    # for i in x:
    #     if(i==','):
    #         l.append(st)
    #         st=""
    #     else:
    #         st +=i
    # print("=-=--=list,",l)
    # l1=[]
    # for i in l:
    #     if(i!="None"):
    #         l1.append(i)

    # print(l1)
    # print(o)
    # print("898989898989898989898989898")
        request.session['bill'] = total

        print(request.session['bill'])
        return render(request,"bill.html",{'d':d,'total':total,'all_user':all_user,'val':val,'done':done,'discount':discount})
    # return HttpResponseRedirect(reverse("forstatus"))
    else:
        return render(request,"login.html")

def Bill(request):
    return render(request,"bill.html")

def Paybill(request,pk):
    if 'email' in request.session and 'role' in request.session:
        print("=-=-=--=-")
        done = Servicedone.objects.get(pk=pk)
        request.session['vid'] = done.id
        print(request.session['vid'])
        total = request.session['bill']
        print(total)
        return render(request, "cartpay.html",{'total':total})
    else:
        return render(request,"login.html")


def Track(request):
    if 'email' in request.session and 'role' in request.session:
        idx=request.session['id']
        user = User.objects.get(Category_id_id=idx)
        all_app = appointment.objects.filter(userid_id=user)
        all_done = Servicedone.objects.filter(userid_id=user,ser_payment="pending")
        all_acc = serviceaccept.objects.filter(userid_id=user)
        all_rej = servicereject.objects.filter(userid_id=user)
        all_com = Servicedone.objects.filter(userid_id=user,ser_payment="done")    

        print(user)
        print(all_app)
        print(all_done)
        print(all_acc)
        print(all_rej)
        return render(request,"track.html",{'all_app':all_app,'all_done':all_done,'all_acc':all_acc,'all_rej':all_rej,'all_com':all_com})

    else:
        return render(request,"login.html")

def Trackacc(request):
    if 'email' in request.session and 'role' in request.session:
        idx=request.session['id']
        user = User.objects.get(Category_id_id=idx)
        order = OrderDetails.objects.filter(userid_id=user.id)
        return render(request, "trackacc.html", {'order':order})
    else:
        return render(request,"login.html")

def Trackveh(request):
    if 'email' in request.session and 'role' in request.session:
        idx=request.session['id']
        user = User.objects.get(Category_id_id=idx)
        used = Usedvehicle.objects.filter(userid_id=user.id)
        return render(request, "trackveh.html", {'used':used})
    else:
        return render(request,"login.html")


def Forstatus(request):
    if 'email' in request.session and 'role' in request.session:
        id="reject"
        id1=" "
    #  or vehicle_status=id1
    #  vehicle_status=id
        all_vehicle = appointment.objects.all()
        return render(request, "forstatus.html", {'all_vehicle':all_vehicle})
    else:
        return render(request,"login.html")

def Accept(request):
    if 'email' in request.session and 'role' in request.session:
        # id="accept"
        all_vehicle = serviceaccept.objects.all()
        return render(request,"accept.html",{'all_vehicle':all_vehicle})	
    else:
        return render(request,"login.html")

def Rejectpg(request):
    if 'email' in request.session and 'role' in request.session:
    # id="reject"
        all_vehicle = servicereject.objects.all()
        return render(request,"reject.html",{'all_vehicle':all_vehicle})
    else:
        return render(request,"login.html")
#ADMIN

def Adminpanel(request):
    if 'email' in request.session and 'role' in request.session:
        x = User.objects.all()
        le = len(x)
        order = OrderDetails.objects.all().count()
        print(order)
        amt = Transaction.objects.all()
        total=0
        for i in amt:
            total += i.amount

        print(total)
        feedback = Feedback.objects.all().count()

        used = Usedvehicle.objects.all().count()
        done = Servicedone.objects.all().count()
        acc = serviceaccept.objects.all().count()
        rej= servicereject.objects.all().count()
        app = appointment.objects.all().count()
        x = done + acc + rej + app

        acc = Accesories.objects.all().count()
        auser = OrderMasterTbl.objects.all().count()
        order1 = OrderDetails.objects.all()
        sold = 0
        for j in order1:
            sold += j.Qty 

        return render(request,"adminpanel.html",{'le':le,'order':order,'total':total,'feedback':feedback,'used':used,'done':done,'x':x,'acc':acc,'auser':auser,'sold':sold})
        # return render(request, "adminpanel.html")
    else:
        return render(request,"login.html")

def Database(request):
    return render(request, "admin")

def Orderacc(request):
    if 'email' in request.session and 'role' in request.session:
        order = OrderDetails.objects.all()
        return render(request, "ordersacc.html", {'order':order})
    else:
        return render(request,"login.html")

def Orderdel(request,pk):
    if 'email' in request.session and 'role' in request.session:
        orders = OrderDetails.objects.get(pk=pk)
        orders.order_status = "Delivered"
        orders.save()
        return HttpResponseRedirect(reverse("orderacc"))
    else:
        return render(request,"login.html")

def Userorder(request,pk):
    if 'email' in request.session and 'role' in request.session:
        user = User.objects.get(pk=pk)

        return render(request , "userorder.html", {'user':user})
    else:
        return render(request,"login.html")

def Accpayment(request):
    if 'email' in request.session and 'role' in request.session:
        all_acc = OrderMasterTbl.objects.all()
        return render(request, "accpayment.html", {'all_acc':all_acc})
    else:
        return render(request,"login.html")

def Adminupdates(request):
    if 'email' in request.session and 'role' in request.session:
        if request.method == "POST":
            info = request.POST['msg']
            newupdate = updates.objects.create(message = info)
            return render(request ,"adminupdate.html")
        else:
            return render(request ,"adminupdate.html")
    else:
        return render(request,"login.html")

def Foremanupdates(request):
    if 'email' in request.session and 'role' in request.session:
        message = updates.objects.all()
        return render(request ,"foremanupdate.html",{'message':message})
    else:
        return render(request,"login.html")

def vehtrue(request,pk):
    used=Usedvehicle.objects.filter(Usedvehicle_verify=False)

def vehdetails(request):
    used=Usedvehicle.objects.filter(Usedvehicle_verify=False)
    return render(request,"vehverify.html")

#Payment
def Payment(request):
    if 'email' in request.session and 'role' in request.session:
        return render(request, "pay.html",{'total':total})
    else:
        return render(request,"login.html")

def initiate_payment(request):
    print("Inside View")
    if request.method == "GET":
        return render(request, 'pay.html')
    try:
        print("0000")
        email = request.session['email']
        # request.POST['email']
        print("Email------------->",email)
        password = request.POST['password']
        amount = int(request.POST['amount'])

        request.session['paid'] = amount
        
        user = Category.objects.get(email=email)
        print("User------------>",user)
        if user:
            transaction = Transaction.objects.create(made_by=user, amount=amount)   #amount can be changed as per requirement
            transaction.save()
            merchant_key = settings.PAYTM_SECRET_KEY

            params = (
            ('MID', settings.PAYTM_MERCHANT_ID),
            ('ORDER_ID', str(transaction.order_id)),
            ('CUST_ID', str(transaction.made_by.email)),
            ('TXN_AMOUNT', str(transaction.amount)),
            ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
            ('WEBSITE', settings.PAYTM_WEBSITE),
            # ('EMAIL', request.user.email),
            # ('MOBILE_N0', '9911223388'),
            ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
            ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
            # ('PAYMENT_MODE_ONLY', 'NO'),
            )

            paytm_params = dict(params)
            checksum = generate_checksum(paytm_params, merchant_key)

            transaction.checksum = checksum
            transaction.save()

            paytm_params['CHECKSUMHASH'] = checksum
            print('SENT: ', checksum)
            return render(request, 'redirect.html', context=paytm_params)
        else:
            return render(request, 'pay.html', context={'error': 'Wrong Account Details or amount'})

    except Exception as e1:
        print("Exception Caught -------------->",e1)
        return render(request, 'pay.html', context={'error': 'Wrong Account Details or amount'})


    #     user = User(request, email=email, password=password)
    #     print("User------------------>",user)
    #     if user is None:
    #         raise ValueError
    #     auth_login(request=request, user=user)
    
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
            print("--------match")
            email = request.session['email']
            # x=received_data['TXN_AMOUNT']
            x=request.session['paid']
            print(x)
            user = Category.objects.get(email=email)
            print(user.id)
            mainuser = User.objects.get(usermail=email)
            bill = request.session['bill']
            print(bill)
            mem = request.session['membership']
            print(mem)
            vid = request.session['vid']
            print(vid)
            print("======1111")
            if(bill!=0):
                done = Servicedone.objects.get(id=vid)
                print("done",done)
                done.ser_payment = "done"
                done.ser_bill = bill
                done.save()
                print("=-==-=-")


            if(mem!="1"):
                mem=request.session['membership']
                print(mem)
                if(mem=="silver"):
                    mainuser.userremservice+=2
                    print("-----ser")
                    mainuser.save()
                    request.session['membership']="1"
                elif(mem=="gold"):
                    mainuser.userremservice+=3
                    print("-----ser")
                    mainuser.save()
                    request.session['membership']="1"
                elif(mem=="platinum"):
                    mainuser.userremservice+=5
                    print("-----ser")
                    mainuser.save()
                    request.session['membership']="1"
            

            # mem = 0
            if user:
                
                newpayment = Paymentstatus.objects.create(userid_id=user.id,Payment_price=x,Card_number=x,Payment_type=mem)

                return HttpResponseRedirect(reverse("comingsoon"))        
        else:
            received_data['message'] = "Checksum Mismatched"
            print("--------mismatch")
            return render(request, 'callback.html', context=received_data)

        # return HttpResponseRedirect(reverse("comingsoon"))


def Chat(request):
    if request.method == "POST":
        x = request.POST['info']
        print(x)
        a1 = ""
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8 = 0
        c9 =0 
        c10 =0 
        c11 = 0
        
        user = User.objects.get(id=1)
        # newchat = chat.objects.create(message = info,userid_id =user.id)
        ques = x.split(" ")
        # li = x.split(" ")

        q1 = "how are you what's up how's you everything fine"
        ans1 = "fine, What about you?"
        l1 = q1.split(" ")
        print(ques)
        # print(li)
        
        q2 = "service vehicle time when will get ready"
        l2 = q2.split(" ")
        ans2 = "Apply for service from homepage and you will have your vehicle service done in minimum time"

        q3 = " hi hii hiii hiiii hello good morning afternoon evening night hi "
        l3 = q3.split(" ")
        ans3 = "Hello!! Greetings... How may i help you ?"
        
        q4 = "payment credit debit card money charge charges pay paytm phonepe googlepe cash bill invoice upi method methods cash pay "
        l4 = q4.split(" ")
        ans4 = "You can pay your bill with many options available like paytm, credit card, debit card with charges of 200 Rs per services...Thank You.."

        q5 = "one time plan plans contract contracts apply types work works problem problems ready when time service services monthly yearly repair repairs vehicle vehicles two wheeler wheel activa bike gear gearless "
        l5 = q5.split(" ")
        ans5 = "You can apply for the service for any problem or any type of repairing works and you can check our best plans from the web site...."

        q6 = "facility charges extra pick drop and & pick&drop time timeslot when upto self mode available home delivery door steps step"
        l6 = q6.split(" ")
        ans6 = "You can have two mode of options for your service 1. Self 2. Pick and Drop. In Self mode you have to pick your vehicle from workshop and In pick and drop mode we will deliver your vehicle to your door steps in minimum time wit no extra charges"

        q7 = "accesories accesory product item items products cash on delivery charges checkout "
        l7 = q7.split(" ")
        ans7 = " You can buy any type of accesories available on our site with many payment methods and with minimum delivery time.."

        q8 = " buy sell buying selling vehicle old used register process deal dealer "
        l8 = q8.split(" ")
        ans8 = "You can register your old vehicle on our and once our admin will confirm it will be listed on our site and you can buy vehicle from our site with direct seller contact..."

        q8 = "status track done  service order"
        l8 = q8.split(" ")
        ans8 = "  You can track order or service from the track function option available on your site"

        q9 = "user profile update password change email mail id pic"
        l9 = q9.split(" ")
        ans9 = " You can update your profile from my profile "

        q10 = "type types membership memberships gold silver platinum package packages plan plans "
        l10 = q10.split(" ")
        ans10 = "There are three type of membership provided Gold, Silver, Platinum and more details are provided on the site with all type of payment methods and auto deduction of membership while applying service"

        q11 = " complain feedback contact "
        l11 = q11.split(" ")
        ans11 = "You can complain or give feedback from the contact us page"

        q12 = "emergency "
        l12 = q12.split(" ")
        ans12 = "You  can access emergency from our website with all nearby contacts"


        for i in ques:
            if i in l1:
               
                c1 +=1
                # a1 = ans1
                # print(c1)
                print("Q - 1 : present")
            if i in l2:
                c2 +=1
                # a1 = a2
                print('Q - 2 Present')

            if i in l3:
                c3 +=1
                print('Q - 3 Present')  

            if i in l4:
                c4 +=1
                print('Q - 4 Present')  

            if i in l5:
                c5 +=1
                print('Q - 5 Present sir')

            if i in l6:
                c6 +=1
                print('Q - 6 Present sir')

            if i in l7:
                c7 +=1
                print('Q - 7 Present sir') 

            if i in l8:
                c8 +=1
                print('Q - 8 Present sir')

            if i in l9:
                c9 +=1
                print('Q - 9 Present sir')


            if i in l10:
                c10 +=1
                print('Q - 10 Present sir')

            if i in l11:
                c11 +=1
                print('Q - 11 Present sir')

            else:
                print("NOt")
        

        if(c1 > max(c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)):
            a1 = ans1
        elif(c2 > max(c1,c3,c4,c5,c6,c7,c8,c9,c10,c11)):
            a1 = ans2
        elif(c3 > max(c1,c2,c4,c5,c6,c7,c8,c9,c10,c11)):
            a1 = ans3
        elif(c4 > max(c1,c2,c3,c5,c6,c7,c8,c9,c10,c11)):
            a1 = ans4
        elif(c5 > max(c1,c2,c3,c4,c6,c7,c8,c9,c10,c11)):
            a1 = ans5
        elif(c6 > max(c1,c2,c3,c4,c5,c7,c8,c9,c10,c11)):
            a1 = ans6
        elif(c7 > max(c1,c2,c3,c4,c5,c6,c8,c9,c10,c11)):
            a1 = ans7
        elif(c8 > max(c1,c2,c3,c4,c5,c7,c6,c9,c10,c11)):
            a1 = ans8
        elif(c9 > max(c1,c2,c3,c4,c5,c7,c8,c6,c10,c11)):
            a1 = ans9
        elif(c10 > max(c1,c2,c3,c4,c5,c7,c8,c9,c6,c11)):
            a1 = ans10
        elif(c11 > max(c1,c2,c3,c4,c5,c7,c8,c9,c10,c6)):
            a1 = ans11
        
        else:
            a1 = "can you please rephrase your question"

        t1 = "emergency"
        if t1 in ques:
            print("==T1==")
            a1 = ans12 

        t2 = "membership"
        if t2 in ques:
            print("==T2==")
            a1 = ans10

        t3 = "track"
        if t3 in ques:
            a1 = ""
            print("==T3==")
            a1 = ans8

        if(c2==c5 and c2!=0):
            a1 = ans5
            print("-=-=-C2&C5=-=-=-")

        # if(c1 > max(c2,c3,c4)):
        #     print("C1")
        print('-=-==-=')
        print(a1)

        user = User.objects.get(id=1)
        newchat = chat.objects.create(message = x,answer=a1,userid_id =user.id)
        msg = chat.objects.all().order_by("id")
        # return render(request, "chat.html", {'a1' : a1,'x':x})
        return render(request, "chat.html", {'msg' : msg})
    else:
        msg = chat.objects.all()
        for i in msg:
            i.delete()
            
        return render(request, "chat.html", {'msg' : msg})


def Pdfgenerate(request,pk):
    done = Servicedone.objects.get(pk=pk)

    print(done)
    print(done.userid)
    idx = done.userid
    x = done.ser_useremail
    print(x)
    all_user = User.objects.get(usermail=x)
    print("==-=-=-=-=-=-=-=-=")
    x = done.ser_need 
    val = done.ser_details
    print(val)
    # x= list(filter(None, x))
    # print(x)
    y = x.split(", ")
    print(y)
    # y = list(filter(None, y))
    print('**************')
    print("==========") 
    # print(y)
    print("-------------------------")
    a = x.replace('None',"")
    c = 0   
    print(a)
    print("[][][[{}}}{}{}{}{}{}")
    str1 = ""
    for y in a:
        if(y==','):
            if(c==0):
                if(y!=','):
                    str1 = str1  + y
                    c = c + 1
            else:
                c = 0
        else:
            str1 = str1  + y
    str1 = str1[1:-1]
    print(str1)
    print("[[============================]]")
    # o = []
    w = list(a.split(","))
    print(w)
    l = []
    # for j in w:
    #     for lp in j:
    #         # if(lp=="'")
    #         if(lp>='a' and lp<='z' or lp>'A' and lp<'Z'):
    #             l +=j

    # print("L :: s",l)
    # print(w[0])
    # print(w[1])
    # print(w[2])
    # l = []
    # for i in w:
    #     if(i==)
    d = {}
    d[0] = "service"
    c = 1
    for i in w:
        ln = len(i)
        if(i!=" " and ln>2):
        # if(i.isspace()==False):
            # print(i.isspace())
            d[c] = i
            c+=1

        # for a,b in d.items():
        #     print(b)
        #     if(b==" "):
        #         d.pop(a)
    mem = all_user.userremservice
    discount = 0
    if(mem>=1):
        discount = 200


    print("\n\n\n==>dict : ",d)
    le = len(d)
    print(le)
    total = le * 200
    if(discount!=0):
        total = total - 200

    print(discount)
    print(total)

    print("===++++++++====")


    # print(request.session['bill'])
    # return render(request,"bill.html",{'d':d,'total':total,'all_user':all_user,'val':val,'done':done,'discount':discount})

    data = {'d':d,'total':total,'all_user':all_user,'val':val,'done':done,'discount':discount}
    # template = get_template("pdf_template.html")
    template = get_template("bill.html")
    data_p=template.render(data) 
    response=BytesIO() 

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)

    if not pdfPage.err:

        return HttpResponse(response.getvalue(),content_type="application/pdf") 
    else:

        return HttpResponse("Error Generating PDF") 

# if request.session.has_key('id'):
# {% if request.session.id %} html