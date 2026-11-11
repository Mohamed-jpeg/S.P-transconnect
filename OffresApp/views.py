from django.shortcuts import render
from .models import Offre
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .form import OffreForm

# Create your views here.
class OffreListView( ListView ):
    model=Offre
    template_name='offre/list.html'
    context_object_name='offres'

class OffreCreateView( CreateView ):
    model=Offre
    template_name='offre/form.html'
    success_url = reverse_lazy('offre:List_offre')
    form_class=OffreForm

class OffreUpdateView( UpdateView ):
    model=Offre
    template_name='offre/form.html'
    success_url = reverse_lazy('offre:List_offre')
    form_class=OffreForm

class OffreDeleteView( DeleteView ):
    model=Offre
    template_name='offre/delete.html'
    context_object_name='offre'
    success_url = reverse_lazy('offre:List_offre')
    