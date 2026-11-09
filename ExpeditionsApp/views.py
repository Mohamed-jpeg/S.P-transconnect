from django.shortcuts import render
from .models import Expedition
from django.http import HttpResponse
from django.views.generic import ListView ,DetailView , DeleteView
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Expedition App!")

def afficher(request, name ):
    expeditions_list=[Expedition.obj.all()]
    return render(request,'expedition/afficher.html',{'name':name})

def listExpeditions(request):
    expeditions=Expedition.objects.all()
    return render(request , 'expedition/list.html',
    {'expeditions':expeditions})

def detail_Expedition(request,pk):  
    expeditions = Expedition.objects.get(pk=pk)
    return render(request, 'expedition/details.html',{'expeditions':expeditions})

class ExeditionDetailsView(DetailView):
    model=Expedition
    template_name="expedition/detail.html"
    context_object_name = 'expedition'

def list_expeditions(request):
    expedition = Expedition.objects.filter(statut='pubile')
    return render(request, "expedition/list.html",{'expeditions':expedition})

class ExpeditionListView( ListView ):
    model=Expedition #hata lhouni amali "select * from Expedition "
    template_name="expedition/list.html"
    context_object_name = 'expeditions'


class ExpeditionDeleteView(DeleteView):
    model=Expedition
    template_name='expedition/delete.html'
    contexte_object_name='expedition'
    success_url = reverse_lazy('expedition:list_Expeditions')