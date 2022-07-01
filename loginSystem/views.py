from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def loginUser(request):
    context = {
        'status_code': 200
    }
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('/home/')
        else:
            context['status_code'] = 404
            return render(request, 'login.html', context)
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def signupUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                return redirect('/login/')
            except Exception as e:
                return render(request, 'signup.html', {'status_code': 409})
        else:
            return render(request, 'signup.html', {'status_code': 401})
            
    return render(request, 'signup.html')
    