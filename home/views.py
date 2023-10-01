from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import Data
#


def login_page(request):
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


def todo_page(request, uuid):
    user_data = Data.objects.all().get(id=uuid)
    todo_lists = user_data.todos["unfinished"]
    return render(request, "home/todo-page.html", {
        "tasks": todo_lists
    })
