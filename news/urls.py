from django.urls import path

from .views import NewsCreate

urlpatterns = [
    path('create',NewsCreate.as_view(),name='news_create'),
]
