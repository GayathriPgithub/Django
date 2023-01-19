from django.shortcuts import render
from django.http import HttpResponse
from .models import MedicalEquipment, Brand, ProductInstance, Category

# Create your views here.
def index(request):
    num_devices = MedicalEquipment.objects.all().count()
    num_instances_available = ProductInstance.objects.filter(status='i').count()
    context = {'num_devices' : num_devices, 'num_instances_available' : num_instances_available,}
    
    return render(request, "index.html",
     context =  {'num_devices' : num_devices, 'num_instances_available' : num_instances_available,})
    #return HttpResponse("<h1> <strong> Olmest.com </strong> </h1> <h2>Interested in buying/selling with us?</h2>")

 

   