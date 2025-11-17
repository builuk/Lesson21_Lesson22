from django.urls import path
from .views import hello_view, user_status_view, about_view, age_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('status/', user_status_view, name='user_status'),
    path('about/', about_view, name='about'),
    path('age/<int:age>', age_view, name='age'),
    path('age/', age_view, name='age'),
]
