from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib import messages


def login_user(request):
    if request.user.is_authenticated:
        messages.error(
            request,
            "Hey you're already loggedin.",
            extra_tags="alert alert-warning alert-dismissible fade show",
        )
        return redirect("notes:home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("notes:home")
        else:
            messages.error(
                request,
                "Username Or Password is incorrect!",
                extra_tags="alert alert-warning alert-dismissible fade show",
            )
    return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    return redirect("notes:home")


def create_user(request):
    if request.user.is_authenticated:
        messages.error(
            request,
            "Hey you're already loggedin.",
            extra_tags="alert alert-warning alert-dismissible fade show",
        )
        return redirect("notes:home")
    if request.method == "POST":
        check1 = False
        check2 = False
        check3 = False
        # print(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            email = form.cleaned_data["email"]

            if password1 != password2:
                check1 = True
                messages.error(
                    request,
                    "Password did not match!",
                    extra_tags="alert alert-warning alert-dismissible fade show",
                )
            if User.objects.filter(username=username).exists():
                check2 = True
                messages.error(
                    request,
                    "Username already exists!",
                    extra_tags="alert alert-warning alert-dismissible fade show",
                )
            if User.objects.filter(email=email).exists():
                check3 = True
                messages.error(
                    request,
                    "Email already registered!",
                    extra_tags="alert alert-warning alert-dismissible fade show",
                )

            if check1 or check2 or check3:
                messages.error(
                    request,
                    "Registration Failed!",
                    extra_tags="alert alert-warning alert-dismissible fade show",
                )
                return redirect("accounts:signup")
            else:
                User.objects.create_user(
                    username=username, password=password1, email=email
                )
                messages.success(
                    request,
                    "Hurrah, registration completed successfully!!",
                    extra_tags="alert alert-success alert-dismissible fade show",
                )
                return redirect("accounts:login")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})
