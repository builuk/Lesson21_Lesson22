from django.shortcuts import render

def hello_view(request):
    context = {'name': 'Andrii'}
    return render(request, "main/hello.html", context)
