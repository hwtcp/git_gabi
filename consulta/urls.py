from django.contrib import admin  # ← ESTA LINHA É ESSENCIAL
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # exemplo de view
]
