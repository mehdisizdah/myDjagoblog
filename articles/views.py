from django.shortcuts import render
from . import models
# from django.shortcuts import render

# Create your views here.

def articles_list(request):
    articles=models.Article.objects.all().order_by('date')
    return render(request,'articles/articleslist.html',{'articless':articles})#.html farmush nshavad
