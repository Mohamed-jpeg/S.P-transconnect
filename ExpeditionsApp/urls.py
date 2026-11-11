from django.urls import path
from .views import (
    ExpeditionCreateView,
    ExpeditionDeleteView,
    ExpeditionListView,
    ExeditionDetailsView,
    ExpeditionUpdateView,
)

app_name='expedition'

urlpatterns = [
    path('list/', ExpeditionListView.as_view(), name='list_Expeditions'),
    path('detail/<int:pk>/',ExeditionDetailsView.as_view(),name='detail_Expedition'),
    path('listView/',ExpeditionListView.as_view(),name='listcbv'),
    path('deleteView/<int:pk>/',ExpeditionDeleteView.as_view(),name='deleteview'),
    path('create/', ExpeditionCreateView.as_view(), name='createview'),
    path('update/<int:pk>/', ExpeditionUpdateView.as_view(), name='updateview'),
]
