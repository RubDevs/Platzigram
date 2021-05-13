from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile

from django.db.utils import IntegrityError

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("feed")
        else:
            return render(request, "users/login.html", {"error": "Invalid username or password"})
    return render(request, "users/login.html")


def signup_view(request):
    '''Signup view'''

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirmation']
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        # PASSWORD VALIDATION
        if password != password_confirm:
            error = 'The passwords do not match.'
            return render(request, 'users/signup.html', {'error': error})

        # EMAIL VALIDATION
        u = User.objects.filter(email=email)
        if u:
            error = f'There is another account using {email}'
            return render(request, 'users/signup.html', {'error': error})

        # USERNAME VALIDATION
        try:
            user = User.objects.create_user(
                username=username, password=password)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name

            user.save()

            profile = Profile(user=user)
            profile.save()

            login(request, user)
            # CAMBIAR >> Redireccionar a completar perfil
            return redirect('profile')
        except IntegrityError as ie:
            error = f'There is another account using {usermame}'
            return render(request, 'users/signup.html', {'error': error})

    return render(request, 'users/signup.html')


def update_profile(request):
    return render(request, "users/update_profile.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
