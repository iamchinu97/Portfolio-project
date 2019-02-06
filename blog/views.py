from django.shortcuts import render
from .models import blog

def blogpage(request):
    blogs=blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})