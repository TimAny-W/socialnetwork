from django.conf import settings
from django.db import models

# Create your models here.

class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False)
    title = models.CharField('title',max_length=75,null=False)
    announce = models.CharField('announce',max_length=255,null=False)
    text = models.TextField('text',null=False)
    img = models.ImageField('image',null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

