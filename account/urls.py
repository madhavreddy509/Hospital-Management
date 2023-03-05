from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('patient/', views.patient, name='patient'),
    path('doctors/', views.doctors, name='doctor'),
    path('doctors/<int:pk>', views.doctor, name='doctor-single'),
    path('postblogs/', views.postBlog, name='postblogs'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<str:pk>/',views.blog,name='blog'),
    path('updateblog/<str:pk>/',views.updateblog,name='updateblog'),
    path('deleteblog/<str:pk>/',views.deleteblog,name='deleteblog'),
    path('drafts',views.drafts,name='drafts'),
    path('appointments',views.appointments,name='appointments'),
]