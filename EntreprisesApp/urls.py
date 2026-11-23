from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    EntrepriseListView,
    EntrepriseCreateView,
    EntrepriseUpdateView,
    EntrepriseDeleteView,
    HomeView,
    Inscription,
    UtilisateurUpdateView,
    UtilisateurDetailView,
    UtilisateurDeleteView,
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
    path('register/', ,name='User_Register'),
    path('userupdate/<int:pk>', ,name='User_Update'),
    path('userdetail/<int:pk>', ,name="User_Detail"),
    path('userdelete/<int:pk>', ,name='User_Delete'),
]
