from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .models import Data
#


def register_user_page(request):
    if (request.method) == "POST":
        user_username = request.POST["username"]
        user_email = request.POST["email"]
        user_password = request.POST["password"]
        user = User.objects.create_user(
            user_username, user_email, user_password)
        user.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "home/register.html")


def login_page(request):
    my_user = request.user
    # If you want to know if the user is logged in
    if (my_user.is_authenticated):
        return HttpResponseRedirect(f"/todo/{Data.objects.get(email=my_user.email).id}")
    else:
        if (request.method) == "POST":
            username_input = request.POST["username"]
            password_input = request.POST["password"]
            user = authenticate(request, username=username_input,
                                password=password_input)
            if user is not None:
                login(request, user)
                request.session["is_logged_in"] = True
                appropriate_user = Data.objects.get(email=user.email).id
                url_const = f"/todo/{appropriate_user}"
                return HttpResponseRedirect(url_const)
            else:
                return None
        return render(request, "home/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required
def todo_page(request, uuid):
    user_data = Data.objects.get(id=uuid)
    # print(f"{user_data.email} data database")
    # print(f"{request.user.username} user database")
    if request.user.email == user_data.email:
        todo_lists = user_data.todos["unfinished"]
        return render(request, "home/todo-page.html", {
            "tasks": todo_lists
        })
    else:
        return HttpResponseForbidden("Access Denied")
