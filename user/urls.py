from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Register,profile_view
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #path('login',name='login')
    path('register',Register.as_view(),name='register'),
    path('profile/<str:pk>',profile_view,name='profile')

]
