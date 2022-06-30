from django.shortcuts import render, redirect

# Create your views here.
def landingPage(request):
    if request.user.is_anonymous:
        return render(request, "landing.html")
    return redirect('/home/')
    