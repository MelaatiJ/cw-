from django.urls import path
from . import views


#endpoints made to create , add  display strings
urlpatterns = [
    path('', views.index),
    path("hello/<str:name>", views.name, name="name"),
    path("times2/<int:answer>", views.times2, name="times2"),
    path("total/<int:numbers>", views.total, name="total"),
    path('newcup/', views.new, name="newcup"),
    path('newcup2/', views.new2, name="newcup2"),


]

