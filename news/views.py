from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from .forms import CreateNewsForm


class NewsCreate(View):
    template_name = 'news/news_create.html'

    def get(self, request):
        return render(request, self.template_name, {'form': CreateNewsForm})

    def post(self,request):
        form = CreateNewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'error': form.errors,
                'form': form

            }
            return render(request,self.template_name,context)
