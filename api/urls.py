from django.urls import path,include
from api import views

urlpatterns = [
    path('',views.allPerson,name = 'allPerson'),
    path('onePerson/<str:id>/',views.onePerson, name = 'onePerson'),
    path('createPerson/',views.createPerson,name = 'createPerson'),
    path('updatePerson/<str:id>', views.updatePerson,name ='updatePerson'),
    path('deletePerson/<str:id>', views.deletePerson,name = 'deletePerson')
]