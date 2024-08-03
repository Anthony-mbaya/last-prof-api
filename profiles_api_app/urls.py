from django.urls import path
from . import views


urlpatterns = [
    path('hello', views.Hello.as_view())
]