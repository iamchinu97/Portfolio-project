from django.shortcuts import render,get_object_or_404
from .models import blog

def blogpage(request):
    blogs=blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})

def detailspage(request,blog_id):
    detailblog= get_object_or_404(blog,pk=blog_id)
    return render(request,'blog/details.html',{'blog':detailblog})