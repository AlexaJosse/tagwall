from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from posts import views


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password1'] and request.POST['password2']:

            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html',
                              {'error': "Nom d'utilisateur déjà pris"})

            except User.DoesNotExist:
                if request.POST['password1'] == request.POST['password2']:
                    user = User.objects.create_user(request.POST['username'])
                    user.set_password(request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'accounts/signup.html',
                                  {'error': "Les mots de passes ne correspondent pas"})
    else:
        redirect('signup/')

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])

        if user is not None:
            login(request, user)
            if 'next' in request.POST.keys():
                print("BITTTTTTTE")
                return redirect(request.POST['next'][:-1])
            else:
                return redirect(views.home)

        else:
            return render(request, 'accounts/login.html',
                          {'error': 'Identifiants incorrects'})
    else :
        return render(request, 'accounts/login.html')


def logout_view(request):
    if request.method == "POST":
        logout(request)

    return redirect('home')
