from django.urls import path
from . import views

urlpatterns = [
    path('first_app/', views.card)  # Link URL: http://127.0.0.1:8000/first_app/first_app/
]

