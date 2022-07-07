import os
from django.shortcuts import redirect, render
from datetime import datetime
from home.models import Contact
from newsscrap.scrap import scrap
import yaml

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')

    # api_key = yaml.full_load('config.yaml')['newsdata']['api_key']
    # context = scrap('pub_86308d85a19dd4b6ec10c5f34bcdd4fa9704').get_data()
    # context = {
    #     'status': True,
    #     'feature_title': "Title of a longer featured blog post",
    #     'feature_img': 'https://64.media.tumblr.com/fa5e27c33743758eb802dc79c799a041/1c21a381185e7c09-f9/s1280x1920/7b114d3320760bebea6af5c49068734242fe261a.jpg',
    #     'feature_link': "#",
    #     'feature_desc': "Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.",

    #     'post_data': [('World', 'Title1', 'This is a wider card with supporting text below as a natural lead-in to additional content.', '#'),
    #                   ('India', 'Title2', 'This is a wider card with supporting text below as a natural lead-in to additional content.', '#'),
    #                   ('Science', 'Title3', 'This is a wider card with supporting text below as a natural lead-in to additional content.', '#'),
    #                   ('Development', 'Title4',
    #                    'This is a wider card with supporting text below as a natural lead-in to additional content.', '#'),
    #                   ('Education', 'Title5', 'This is a wider card with supporting text below as a natural lead-in to additional content.', '#')],
    #     'post_date': datetime.now().strftime("%d %b %Y")

    # }
    scrapobj = scrap("pub_86308d85a19dd4b6ec10c5f34bcdd4fa9704")
    newsdata = scrapobj.get_data_newsdataapi()
    hindueditorials = scrapobj.get_hindu_editorials()
    return render(request, 'main/index.html', {**newsdata, **hindueditorials})


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
   
    return render(request, '404.html')