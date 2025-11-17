from django.urls import path
from .views import hello_view, user_status_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('status/', user_status_view, name='user_status'),
]