from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name="login-page"),
    path("register", views.register_user_page, name="register-user"),
    path("logout", views.logout_view, name="logout-user"),
    path("delete-task", views.delete_data),
    path("todo/<uuid>", views.todo_page)
]
