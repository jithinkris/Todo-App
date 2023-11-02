from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),

    ##################### USER MODULE ###########################
    path('UserHome/',views.UserHome,name="UserHome"),
    path('ADDTODO/',views.ADDTODO,name="ADDTODO"),
    path('delete/',views.delete,name="delete"),
    path('Done/',views.Done,name="Done"),
    path('editing/',views.editing,name="editing"),
    
]
