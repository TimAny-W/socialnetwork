from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from .forms import UserCreationForm
from .models import CustomUser


class Register(View):
    """View of registration"""
    template_name = 'registration/registration.html'

    def get(self, request):
        return render(request, self.template_name, {'form': UserCreationForm})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
        else:
            context = {
                'form': form,
                'errors': form.errors
            }
            return render(request, self.template_name, context)


def profile_view(request, pk):
    """Def to view somebody profile"""
    user = CustomUser.objects.get(username=pk)
    info = {
        'user_': user,
    }

    return render(request, 'user/profile.html', info)

