from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    return render(request, 'accounts/register.html')

@login_required
def profile(request):
    return render(request, 'accounts/register.html')