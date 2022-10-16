from django.urls import path, include
from .views import Register,profile_view
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register',Register.as_view(),name='register'),
    path('profile/<int:pk>',profile_view,name='profile')

]
