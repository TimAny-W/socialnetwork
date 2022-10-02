from django.forms import ModelForm

from .models import News


class CreateNewsForm(ModelForm):
    class Meta:
        model = News
        fiels = ['title', 'announce', 'text', 'img', ]
        exclude = ['author', 'date', ]
