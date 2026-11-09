from django.urls import path 
from .views import home ,afficher , listExpeditions ,detail_Expedition , ExpeditionListView ,Delete_Expedition , ExpeditionDeleteView , ExeditionDetailsView


app_name='expedition'

urlpatterns = [
    path('home/', home , name='home'),
    path('afficher/<str:name>/',afficher,name='afficher'),
    path('list/',listExpeditions,name='list_Expeditions'),
    path('detail/<str:pk>/',ExeditionDetailsView.as_view(),name='detail_Expedition'),
    path('listView/',ExpeditionListView.as_view(),name='listcbv'),
    path('deleteView/',ExpeditionDeleteView.as_view(),name='deleteview')
]
