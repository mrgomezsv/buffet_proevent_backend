from django.urls import path
from .views import welcome, login_view
from . import views

urlpatterns = [
    path('', welcome, name='welcome'),  # Ruta para la página de inicio
    path('login/', login_view, name='login'),  # Ruta para el login
    path('register/', views.register_view, name='register'),
]