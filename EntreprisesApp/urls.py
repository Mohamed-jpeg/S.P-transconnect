from django.urls import path
from .views import (
    EntrepriseListView,
    EntrepriseCreateView,
    EntrepriseUpdateView,
    EntrepriseDeleteView,
)
app_name='entreprise'

urlpatterns = [
    path('list/',EntrepriseListView.as_view(),name='List_Entreprises'),
    path('create/',EntrepriseCreateView.as_view(),name='Create_Entreprises'),
    path('update/<int:pk>',EntrepriseUpdateView.as_view(),name='Update_Entreprise'),
    path('delete/<int:pk>',EntrepriseDeleteView.as_view(),name='Delete_Entreprise'),
]
