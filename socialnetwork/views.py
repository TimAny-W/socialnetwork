
from django.db.models import Q
from django.shortcuts import render

from news.models import News

from user.models import CustomUser


def home(request):
    """
        View of home page
    """
    search_query = request.GET.get('search','')
    print(search_query)
    if search_query:
        news = CustomUser.objects.filter(Q(first_name__iregex=search_query) | Q(last_name__iregex=search_query)) #search users
        print(CustomUser.objects.all())
        print(CustomUser.objects.filter(username__iregex=search_query))
    else:
        news = 'Не найдено пользователей по таким параметрам'
    context = {'news': news}
    return render(request,'home.html',context)