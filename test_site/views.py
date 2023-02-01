from django.shortcuts import render,get_object_or_404
#from django.http import HttpResponse
from .models import MedicalEquipment, Brand, ProductInstance, Category
from django.views import generic


# Create your views here.
def index(request):
    num_devices = MedicalEquipment.objects.all().count()
    num_instances_available = ProductInstance.objects.filter(status='i').count()
    context = {'num_devices' : num_devices, 'num_instances_available' : num_instances_available,}
    
    return render(request, "index.html",
     context =  {'num_devices' : num_devices, 'num_instances_available' : num_instances_available,})
    

class MedicalEquipmentListView(generic.ListView):
    model = MedicalEquipment 
   

class MedicalEquipmentDetailView(generic.DetailView):
    model = MedicalEquipment   
    
    
