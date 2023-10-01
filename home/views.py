from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import Data
#


def login_page(request):
    url_const = ""
    my_user = request.user
    # If you want to know if the user is logged in
    if (my_user.is_authenticated):
        print("succes")
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


def todo_page(request, uuid):
    user_data = Data.objects.all().get(id=uuid)
    todo_lists = user_data.todos["unfinished"]
    return render(request, "home/todo-page.html", {
        "tasks": todo_lists
    })
