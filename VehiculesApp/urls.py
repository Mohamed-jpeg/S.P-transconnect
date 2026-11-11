from django.urls import path
from .views import (
    VehiculeListView,
    VehiculeCreateView,
    VehiculeUpdateView,
    VehiculeDeleteView,
)
app_name='vehicule'

urlpatterns = [
    path('list/',VehiculeListView.as_view(),name='List_Vehicules'),
    path('create/',VehiculeCreateView.as_view(),name='Create_Vehicules'),
    path('update/<int:pk>',VehiculeUpdateView.as_view(),name='Update_Vehicule'),
    path('delete/<int:pk>',VehiculeDeleteView.as_view(),name='Delete_Vehicule'),
]
