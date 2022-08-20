from multiprocessing import context
import os
from django.shortcuts import redirect, render
from datetime import datetime
from home.models import Contact
from newsscrap.scrap import scrap
import yaml

# Create your views here.

def index(request, topic="trending"):
    if request.user.is_anonymous:
        return redirect('/login')

    scrapobj = scrap("pub_86308d85a19dd4b6ec10c5f34bcdd4fa9704", topic)
    newsdata = scrapobj.get_data_newsdataapi()
    hindueditorials = scrapobj.get_hindu_editorials()
    # exams = scrapobj.get_upcoming_exams()

    context = {**newsdata, **hindueditorials}
    return render(request, 'main/index.html', context)


def profile(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'main/profile.html')


def about(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'main/about.html')


def contact(request):
    context = {
        'status_code': 404
    }
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        data = request.POST.get('data')

        contact = Contact(name=name, email=email, number=number,
                          data=data, date=datetime.today())
        contact.save()
        context['status'] = 200
    return render(request, 'main/contact.html', context)


def services(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'main/services.html')

def error_404_view(request, exception):
   
    return render(request, 'error/404.html')