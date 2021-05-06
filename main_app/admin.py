from django.contrib import admin
from . import models        
from import_export.admin import ImportExportModelAdmin 
# Register your models here.



# class appointmentAdmin(admin.ModelAdmin):

#     list_display = ('vehicle_number','vehicle_appdate','vehicle_apptime','vehicle_mode',)
#     list_filter = ('vehicle_appdate',)
    
class appointmentAdmin(ImportExportModelAdmin):
    list_display = ('vehicle_number','vehicle_appdate','vehicle_apptime','vehicle_mode',)
    list_filter = ('vehicle_appdate',)
    pass   

# class AppAdmin(ImportExportModelAdmin):
#     pass

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','role','email',)
    list_filter = ('role',)

class foremanadmin(admin.ModelAdmin):
    list_display = ('id','Foreman_name','Foreman_email',)
    list_filter = ('Foreman_jdate',)

class Useradmin(admin.ModelAdmin):
    list_display = ('id','username','usermail',)
    list_filter = ('id',)

class Usedvehicleadmin(admin.ModelAdmin):
    list_display = ('id','Usedvehicle_regno','Usedvehicle_company','Usedvehicle_email',)
    list_filter = ('Usedvehicle_regdate',)

class Accesoriesadmin(admin.ModelAdmin):
    list_display = ('id','Accesories_name','Accesories_type','Accesories_price',)
    list_filter = ('Accesories_type',)



admin.site.register(models.appointment,appointmentAdmin)
admin.site.register(models.Category, categoryAdmin)
admin.site.register(models.Foreman, foremanadmin)
admin.site.register(models.User, Useradmin)
admin.site.register(models.Servicevehicle)
admin.site.register(models.Service)
admin.site.register(models.Usedvehicle, Usedvehicleadmin)
admin.site.register(models.Vehiclebuyer)
admin.site.register(models.VehicleSeller)
admin.site.register(models.Accesories, Accesoriesadmin)
admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.Paymentstatus)
admin.site.register(models.Chatbox)
admin.site.register(models.Feedback)
admin.site.register(models.CartTbl)
admin.site.register(models.OrderMasterTbl)
admin.site.register(models.OrderDetails)
admin.site.register(models.pickup)
admin.site.register(models.Servicedone)
admin.site.register(models.serviceaccept)
admin.site.register(models.servicereject)


admin.site.site_header=('Vehicle Maintenance System')
admin.site.site_title=('VMS')
admin.site.site_url = 'http://127.0.0.1:8000/adminpanel/'
# site.favicon=staticfiles=('C:\Users\PREMAL PAREKH\Desktop\django\main_project\main_app\img\accesories\p1.png')

    
    

# ₹₹₹₹

# class Appoint(appointment.Model)