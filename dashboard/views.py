from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages




def welcome(request):
    return render(request, 'dashboard/welcome.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Autenticar al usuario (puedes ajustar esto según tu modelo de usuario)
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('welcome')  # Redirige a la página de inicio después del login
        else:
            messages.error(request, 'Email or password is incorrect.')

    return render(request, 'dashboard/login.html')