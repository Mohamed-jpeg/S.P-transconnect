from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Entreprise
from .forms import EntrepriseForm
# Create your views here.
class EntrepriseListView( ListView ):
    model=Entreprise
    template_name='entreprise/list.html'
    context_object_name='entreprises'

class EntrepriseCreateView( CreateView ):
    model = Entreprise
    form_class = EntrepriseForm
    template_name = 'entreprise/form.html'
    success_url = reverse_lazy('entreprise:List_Entreprises')

class EntrepriseUpdateView( UpdateView ):
    model = Entreprise
    template_name = 'entreprise/form.html'
    success_url = reverse_lazy('entreprise:List_Entreprises')
    form_class = EntrepriseForm # this is the form that will be used to update the expedition

class EntrepriseDeleteView( DeleteView ):
    model=Entreprise
    template_name = 'entreprise/delete.html'
    context_object_name='entreprise'
    success_url = reverse_lazy('entreprise:List_Entreprises')