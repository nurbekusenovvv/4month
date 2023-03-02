from django.shortcuts import render
from django.http import HttpResponse


def get_create(request):
   
    return render(request, "posts/post_create.html", context=None)


def get_detail(request):
    
    return render(request, "posts/post_detail.html", context=None)


def get_update(request):
    
    return render(request, "posts/post_update.html", context=None)


def get_admin(request):
    
    return render(request, "posts/admin.html", context=None)