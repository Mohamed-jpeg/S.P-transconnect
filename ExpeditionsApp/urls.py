from django.urls import path 
from .views import home ,afficher , listExpeditions ,detail_Expedition , ExpeditionListView , ExpeditionDeleteView , ExeditionDetailsView


app_name='expedition'

urlpatterns = [
    path('home/', home , name='home'),
    path('afficher/<str:name>/',afficher,name='afficher'),
    path('list/',listExpeditions,name='list_Expeditions'),
    path('detail/<int:pk>/',ExeditionDetailsView.as_view(),name='detail_Expedition'),
    path('listView/',ExpeditionListView.as_view(),name='listcbv'),
    path('deleteView/<int:pk>/',ExpeditionDeleteView.as_view(),name='deleteview')
]
