from django.shortcuts import render
from django.views.generic import TemplateView
import datetime
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def simple_contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        message = request.POST.get("message", "")
        return render(request, "main/simple_contact.html",
                      {'sent': True, 'name': name, 'message': message})
    return render(request, "main/simple_contact.html", {'sent': False})


@csrf_protect
def simple_contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        message = request.POST.get("message", "")
        return render(request, "main/simple_contact.html",
                      {'sent': True, 'name': name, 'message': message})
    return render(request, "main/simple_contact.html", {'sent': False})


@csrf_protect
def simple_contact_list_view(request):
    if request.method == "POST":
        start = request.POST.get("start", "")
        finish = request.POST.get("finish", "")
        mod = request.POST.get("mod")
        simple_list = []

        def simple_number(number):
            for n in range(2, int(number)):
                if number % n == 0:
                    return False
            return True

        for i in range(int(start), int(finish) + 1):
            if simple_number(i):
                simple_list.append(i)

        return render(request, "main/simple_contact_list.html",
                      {'sent': True, 'simple_list': simple_list,"mod": mod})
    return render(request, "main/simple_contact_list.html", {'sent': False})

@csrf_protect
def water_view(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        surname = request.POST.get("surname", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "")
        month = request.POST.get("month")
        value = request.POST.get("value")
        water_form = {
        'name': name,
        'surname': surname,
        'email': email,
        'phone': phone,
        'address': address,
        'month': month,
        'value': value
        }

        return render(request, "main/water.html",
                      {'sent': True, 'water_form': water_form})
    return render(request, "main/water.html", {'sent': False})

def hello_view(request):
    context = {'name': 'Andrii'}
    return render(request, "main/hello.html", context)


def user_status_view(request):
    is_logged_in = True
    return render(request, "main/user_status.html", {'is_logged_in': is_logged_in})


def about_view(request):
    return render(request, "main/about.html")


def age_view(request, age=16):
    context = {'age': age}
    return render(request, "main/age.html", context)


def filter_view(request, name, color, numbers):
    today = datetime.date.today()
    numbers = numbers.split(',')
    context = {'name': name, 'color': color, 'numbers': numbers, 'today': today}
    return render(request, "main/filter.html", context)


class SimpleTemplateView(TemplateView):
    template_name = "main/simple.html"


class StaticTemplateView(TemplateView):
    template_name = "main/static.html"


class CourseInfoView(TemplateView):
    template_name = "main/course_info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course_name"] = "Django Web Development"
        context["duration_hours"] = 24
        return context
