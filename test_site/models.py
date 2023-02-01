from django.db import models
from django.urls import reverse
import uuid


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,help_text='Device Category (e.g. Radiology)')
    def __str__(self):
        return self.name

class MedicalEquipment(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey("Brand",on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    price_in_euros = models.IntegerField()
    category = models.ManyToManyField(Category,help_text='Select category for this device')

    class Meta:
        ordering = ['name','brand']

    def display_category(self):
        return ', '.join([category.name for category in self.category.all()[:3]])
    
    display_category.short_description = 'Category'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('medicalequipment_detail',args=[str(self.id)])     
   

class ProductInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular Device')
    medicalequipment = models.ForeignKey('MedicalEquipment', on_delete=models.RESTRICT, null=True)
    date_of_upload = models.DateField()
    #created_at = models.DateTimeField(auto_now_add=True)
    status_type = (
        ('i', 'In stock'),
        ('o', 'Out of stock')
    )

    status = models.CharField(
        max_length=1,
        choices=status_type,
        blank=True,
        help_text='Device availability',
    )

    class Meta:
        ordering = ['status']

    def __str__(self):
        return f'{self.id} ({self.medicalequipment.name})'
        #return '{0} ({1})'.format(self.id, self.book.title)


class Brand(models.Model):
    manufacturer = models.CharField(max_length=200) 
    
    class Meta:
        ordering = ["manufacturer"]  

    def get_absolute_url(self):
        return reverse('brand-details', args=[str(self.id)])

    def __str__(self):
        return f"{self.manufacturer}"       





