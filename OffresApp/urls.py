from django.urls import path
from .views import (
    OffreListView,
    OffreCreateView,
    OffreUpdateView,
    OffreDeleteView,
)

app_name='offre'

urlpatterns=[
    path('list/',OffreListView.as_view(),name='List_offre'),
    path('create/',OffreCreateView.as_view(),name='Create_Offre'),  
    path('update/<int:pk>/',OffreUpdateView.as_view(),name='Update_Offre'),
    path('delete/<int:pk>/',OffreDeleteView.as_view(),name='Delete_Offre'),
]