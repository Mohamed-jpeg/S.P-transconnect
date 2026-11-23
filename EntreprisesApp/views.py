from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Entreprise , Utilisateur
from .forms import EntrepriseForm , UtulisateurForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model, logout



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

class HomeView( ListView ):
    model=Entreprise
    template_name='entreprise/home.html'
    context_object_name = "entreprises"







class Inscription(CreateView):
    model = Utilisateur
    form_class = UtulisateurForm
    template_name = 'entreprise/inscription.html'
    success_url = reverse_lazy('entreprise:login')  

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ['first_name', 'last_name', 'email']
    template_name = 'entreprise/profile.html'
    success_url = reverse_lazy('entreprise:profile')

    def get_object(self, queryset=None):
        return self.request.user

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = 'entreprise/confirm_delete.html'
    success_url = reverse_lazy('entreprise:home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = self.object
        logout(self.request)  # log out first so the session doesn't point to a deleted user
        user.delete()
        return HttpResponseRedirect(self.get_success_url())