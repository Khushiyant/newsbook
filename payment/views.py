from django.shortcuts import render

# Create your views here.
def pricing(request):
    context = {
        'plan_status_basic': 'Start Now',
        'plan_status_pro': 'Buy Now',
        'plan_status_enterprise': 'Buy Now',
    }
    return render(request, 'landing/pricing.html',context)

def checkout(request):
    pass