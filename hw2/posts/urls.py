from django.urls import path

from posts.views import hello, get_index,get_contact,get_about

urlpatterns = [
    path("hello/", hello, name="hello-view"),
    path("", get_index, name="index-page"),
    path('contact/', get_contact, name="get_contact"),
    path('about/', get_about, name='get_about'),
]