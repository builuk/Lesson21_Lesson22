from django.urls import path
from .views import hello_view, user_status_view, about_view, age_view, SimpleTemplateView, filter_view, StaticTemplateView, CourseInfoView,simple_contact_view, simple_contact_list_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('status/', user_status_view, name='user_status'),
    path('about/', about_view, name='about'),
    path('filter/<str:name>/<str:color>/<str:numbers>', filter_view, name='filter'),
    path('age/<int:age>', age_view, name='age'),
    path('age/', age_view, name='age'),
    path('simple/', SimpleTemplateView.as_view(), name='simple'),
path('static_page/', StaticTemplateView.as_view(), name='static'),
    path("course-info/", CourseInfoView.as_view(), name="course-info"),
    path("simple_contact/", simple_contact_view, name="simple_contact"),
path("simple_contact_list/", simple_contact_list_view, name="simple_contact_list"),
]
