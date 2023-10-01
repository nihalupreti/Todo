from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page),
    path("todo/<uuid>", views.todo_page)
]
