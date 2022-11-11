from django.contrib.auth import login, get_user_model, logout
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from staff.models import Patient

User = get_user_model()


def user_list(request):
    user = request.user.level
    L = User.objects.all().filter(level=user)
    M = User.objects.all()
    print(user)
    context = {
        'L': L,
        'M': M,
    }

    return render(request, 'userlist.html', context)


def updateUser(request, pk):
    user = User.objects.get(id=pk)

    form = RegisterForm(instance=user)

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect('users')

    context = {
        "form": form
    }

    return render(request, 'updateUser.html', context)


def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('users')


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
        password = form.cleaned_data.get("password")
        newUser = User.objects.create_user(username, password)
    context = {
        "form": form,
        "registerForm": registerForm,
    }
    return render(request, "auth/login.html", context)


def home_page(request):
    if request.user.is_authenticated:
        user = request.user.level
        user2 = request.user.ward

    user_count = User.objects.filter(level=user, personel=True, active=True).count()
    user2_count = User.objects.filter(level=user, patient=True, active=True).count()
    patient_count = Patient.objects.filter(Admitted=True).count()
    Npatient_count = Patient.objects.filter(Admitted=False).count()
    wardpatient_count = Patient.objects.filter(ward=user2).count()

    print(user)
    context = {
        'Npatient_count': Npatient_count,
        'user_count': user_count,
        'patient_count': patient_count,
        'user2_count': user2_count,
        'wardpatient_count': wardpatient_count,
    }
    return render(request, 'home_page.html', context)


def logout(request):
    return render(request, 'auth/login.html')


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
    return render(request, "auth/register.html", context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = 'users'
