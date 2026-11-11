from django.shortcuts import render
from .models import Vehicule
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .form import VehiculeForm


# Create your views here.
class VehiculeListView( ListView ):
    model=Vehicule
    template_name='vehicule/list.html'
    context_object_name='vehicules'

class VehiculeCreateView( CreateView ):
    model = Vehicule
    form_class = VehiculeForm
    template_name = 'vehicule/form.html'
    success_url = reverse_lazy('vehicule:List_Vehicules')

class VehiculeUpdateView( UpdateView ):
    model = Vehicule
    template_name = 'vehicule/form.html'
    success_url = reverse_lazy('vehicule:List_Vehicules')
    form_class = VehiculeForm # this is the form that will be used to update the expedition

class VehiculeDeleteView( DeleteView ):
    model=Vehicule
    template_name = 'vehicule/delete.html'
    context_object_name='vehicule'
    success_url = reverse_lazy('vehicule:List_Vehicules')
