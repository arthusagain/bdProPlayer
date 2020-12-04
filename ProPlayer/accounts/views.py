from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.http import JsonResponse

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'accounts/register.html',context)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def verify_username(request):
    username = request.GET.get('username','')

    response = {
        'exists' : User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)