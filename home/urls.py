from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="home/reset-password-form.html"),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="home/reset-requested-page.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="home/change-password-form.html"),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="home/reset-success-page.html"),
         name='password_reset_complete'),
    path("", views.login_page, name="login-page"),
    path("register", views.register_user_page, name="register-user"),
    path("logout", views.logout_view, name="logout-user"),
    path("delete-task", views.delete_data),
    path("save-task", views.save_task),
    path("todo/<uuid>", views.todo_page)
]
