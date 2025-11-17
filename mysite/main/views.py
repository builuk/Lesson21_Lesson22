from django.shortcuts import render

def hello_view(request):
    context = {'name': 'Andrii'}
    return render(request, "main/hello.html", context)

def user_status_view(request):
    is_logged_in = True
    return render(request, "main/user_status.html", {'is_logged_in': is_logged_in})

def about_view(request):
    return render(request, "main/about.html")

def age_view(request, age=16):
    return render(request, "main/age.html", {'age': age})