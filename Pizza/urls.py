from django.urls import path

from .views import *

urlpatterns=[
    path("",home,name="home"),
    path("Pizza/<str:id>",single_pizza_view,name="single"),
    path("Create",createPizza,name="create"),
    path("Update/<str:id>",EditPizza,name="update"),
    path("Delete/<str:id>",DeletePizza,name="delete")
]