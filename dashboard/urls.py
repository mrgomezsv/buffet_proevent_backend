from django.urls import path
from .views import home, login_view

urlpatterns = [
    path('', home, name='home'),  # Ruta para la página de inicio
    path('login/', login_view, name='login'),  # Ruta para el login
]