from django.urls import path ,reverse_lazy
from django.contrib.auth import views as auth_views

from .views import (
    EntrepriseListView,
    EntrepriseCreateView,
    EntrepriseUpdateView,
    EntrepriseDeleteView,
    HomeView,
    Inscription,
    AccountDeleteView,
    ProfileUpdateView,
)
app_name='entreprise'

urlpatterns = [
    path('list/',EntrepriseListView.as_view(),name='List_Entreprises'),
    path('create/',EntrepriseCreateView.as_view(),name='Create_Entreprises'),
    path('update/<int:pk>',EntrepriseUpdateView.as_view(),name='Update_Entreprise'),
    path('delete/<int:pk>',EntrepriseDeleteView.as_view(),name='Delete_Entreprise'),
    path('login/',auth_views.LoginView.as_view(template_name='entreprise/login.html'),name='Login_Entreprise'),
    path('logout/',auth_views.LogoutView.as_view(template_name='entreprise/logout.html'),name='Logout_Entreprise'),
    path('home/',HomeView.as_view(),name='home'),
    path('userregister/',Inscription.as_view() ,name='User_Register'),
    path('userupdate/',auth_views.PasswordChangeView.as_view(template_name='entreprise/update.html',
    success_url=reverse_lazy('entreprise:home'),  # must match the name= of your home route
        ),name='User_Update',),
        path(
    'passwordchanged/',
    auth_views.PasswordChangeDoneView.as_view(template_name='entreprise/password_changed.html'),
    name='password_change_done',),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/delete/', AccountDeleteView.as_view(), name='account_delete'),
]
