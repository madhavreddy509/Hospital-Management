from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),
   
]