from django.urls import path
from . import views


urlpatterns=[
     path("", views.index, name="index"),
     path('medicalequipments/', views.MedicalEquipmentListView.as_view(), name='medicalequipments'),
     path('medicalequipment/<int:pk>/', views.MedicalEquipmentDetailView.as_view(), name='medicalequipment_detail'),
    
]