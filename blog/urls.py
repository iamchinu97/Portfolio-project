from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogpage, name='blogpage'),
    path('<int:blog_id>/',views.detailspage,name='details')
]