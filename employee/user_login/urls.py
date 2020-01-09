from django.urls import path, include
from . import views


urlpatterns = [
    path('user_list/', views.user_list),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login")


]
