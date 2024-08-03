from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, base_name='helloviewset') #use base name when not using queryset
router.register('profiles', views.UserProfileViewset)


urlpatterns = [
    path('hello', views.Hello.as_view()),
    path('studs', views.StudentMarks.as_view()), 
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)) #empty url to pass all the urls not speciying name
]