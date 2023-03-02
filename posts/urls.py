from django.urls import path
from . import views
from posts.views import get_create, get_detail, get_update, get_admin

urlpatterns = [
    path("", get_admin, name="get_admin"),
    path("create/", get_create, name="get_create"),
    path("detail/", get_detail, name="get_datail"),
    path("update/", get_update, name="get_update"),
]

