from django.urls import path

from users.views import UserRegister,UserListAPIView

urlpatterns = [
    path("users/register/", UserRegister, name="register"),
    path("api/users/list", UserListAPIView.as_view(), name= "api_users")
]