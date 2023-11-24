""" App urls """
from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.Student_List, name= "student_list"),
    path('', views.Student_Form,name= "student_register"),
    path('<str:curp>/', views.Student_Form,name= "student_update"),
    path('delete/<str:curp>', views.Student_Delete, name="student_delete"),
]