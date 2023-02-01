from django.contrib import admin
from .models import Category, MedicalEquipment, ProductInstance, Brand

# Register your models here.
admin.site.register(Category) 
#admin.site.register(MedicalEquipment)
#admin.site.register(ProductInstance)
admin.site.register(Brand)

class ProductsInstanceInline(admin.TabularInline):
    model = ProductInstance

class MedicalEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name','brand','display_category')

    inlines = [ProductsInstanceInline]

admin.site.register(MedicalEquipment, MedicalEquipmentAdmin)
    
@admin.register(ProductInstance)    
class ProductInstanceAdmin(admin.ModelAdmin):
    list_display = ('medicalequipment', 'status', 'date_of_upload', 'id')
    list_filter = ('status','date_of_upload')

    fieldsets = (
        (None, {
            'fields' : ('medicalequipment','id')
        }),
        ('Availability',{
            'fields' : ('status','date_of_upload')
        }),
    )

 

