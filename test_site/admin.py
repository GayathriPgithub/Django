from django.contrib import admin
from .models import Category, MedicalEquipment, ProductInstance, Brand

# Register your models here.
admin.site.register(Category) 
#admin.site.register(MedicalEquipment)
#admin.site.register(ProductInstance)
admin.site.register(Brand)

class ProductInstanceInline(admin.TabularInline):
    model = ProductInstance

class MedicalEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name','brand','display_category')

    inlines = [ProductInstanceInline]

admin.site.register(MedicalEquipment, MedicalEquipmentAdmin)
    
@admin.register(ProductInstance)    
class ProductInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status','date_of_upload')

    fieldsets = (
        (None, {
            'fields' : ('device','id')
        }),
        ('Availability',{
            'fields' : ('status','date_of_upload')
        }),
    )

 

