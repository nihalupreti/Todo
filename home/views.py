from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden, JsonResponse, HttpResponse
from .models import Data
from .forms import UserRegisterForm


def register_user_page(request):
    if (request.method) == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            register_user = User.objects.create_user(
                first_name=user_data["first_name"], last_name=user_data["last_name"], username=user_data["username"], email=user_data["email"], password=user_data["password"])
            create_user_field = Data(
                user=user_data["username"], email=user_data["email"])
            register_user.save()
            create_user_field.save()
            return HttpResponseRedirect("/")
    else:
        form = UserRegisterForm()
    return render(request, "home/register.html", {
        "forms": form
    })


def login_page(request):
    my_user = request.user
    # If you want to know if the user is logged in
    if (my_user.is_authenticated):
        return HttpResponseRedirect(f"/todo/{Data.objects.get(email=my_user.email).id}")
    else:
        if (request.method) == "POST":
            email_input = request.POST["username"]
            password_input = request.POST["password"]
            print(email_input)
            user = authenticate(request, email=email_input,
                                password=password_input)
            if user is not None:
                login(request, user)
                appropriate_user = Data.objects.get(email=user.email).id
                request.session["id"] = str(appropriate_user)
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
    if request.user.email == user_data.email:
        todo_lists = user_data.todos["unfinished"]
        return render(request, "home/todo-page.html", {
            "tasks": todo_lists,
            "user_id": uuid
        })
    else:
        return HttpResponseForbidden("Access Denied")


def delete_data(request):
    if (request.method) == "POST":
        table_data = Data.objects.get(id=request.session.get("id"))
        todos = table_data.todos
        clicked_task = request.POST.get('user_todo')
        todos["finished"].append(clicked_task)
        todos["unfinished"].remove(clicked_task)
        # update the database
        table_data.todos = todos
        table_data.save()
        table_data.save()
        response_data = {
            "status": True,
        }
        return JsonResponse(response_data)
    else:
        return HttpResponse("Method not allowed", status=405)


def save_task(request):
    if (request.method) == "POST":
        table_data = Data.objects.get(id=request.session.get("id"))
        table_data.todos["unfinished"].append(request.POST.get('added_todo'))
        table_data.save()
        response_data = {
            "status": True,
        }
        return JsonResponse(response_data)
    else:
        return HttpResponse("Method not allowed", status=405)
