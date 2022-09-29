from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm
User = get_user_model()

def home_page(request):
    if request.user.is_authenticated:
        return render(request,"home_page.html")
    else:
        return redirect('login')

def user_list(request):
    model = User.objects.all().values()
    context = {
        'model': model,
    }

    return render(request, 'auth/user.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    registerForm = RegisterForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.login(request)
        print(user)
        if user:
            print(user)
            login(request, user)
            return redirect('home')
    if request.POST and registerForm.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        newUser = User.objects.create_user(username, email, password)
    context = {
        "form": form,
        "registerForm": registerForm
    }
    return render(request, "auth/login.html", context)

# def register_form(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         'form': form
#     }
#
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")
#         newUser = User.objects.create_user(username, email, password)
#
#     return render(request, "auth/register.html", context)

