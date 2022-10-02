from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls'), name='user'),
    
    path('',home,name='home'),
    path('news/',include('news.urls'),name='news')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
