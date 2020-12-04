from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    return render(request, 'accounts/register.html')

@login_required
def profile(request):
    return render(request, 'accounts/register.html')


def verify_username(request):
    username = request.GET.get('username','')

    response = {
        'exists' : User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)