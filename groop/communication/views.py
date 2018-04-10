from django.shortcuts import render
from django.contrib.auth import authenticate

from .forms import SignUpForm, AddComment

# Create your views here.
def home(request, user):
    template = 'communication/userhome.html'
    context = {
        'key': user
    }
    return render(request, template, context)

def index(request):
    template = 'communication/userland.html'
    context = {
        'key': 'value',
    }
    if request.method == 'POST':
        in_username = request.POST.get('username')
        in_password = request.POST.get('password')
        user = authenticate(username=in_username, password=in_password)
        if user is not None:
            return home(request, user)
        else:
            template = 'communication/failedLogin.html'
    return render(request, template, context)

def signup(request):
    template = 'communication/signup.html'
    user_form = SignUpForm()
    context = {
        'form': user_form
    }
    return render(request, template, context)

def create(request):
    template ="communication/signup.html"
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db() #loads profile
            user.profile.f_name = user_form.cleaned_data.get('f_name')
            user.profile.l_name = user_form.cleaned_data.get('l_name')
            user.save()
            user.profile.save()
            raw_password = user_form.cleaned_data.get('password')
            user = authenticate(username=user.username, password=raw_password)
            return home(request, user)
        else:
            user_form = SignUpForm()
    context= {
        'form': user_form
    }
    return render(request, template, context)

def newComment(request, user, ride):
    template = ''
    form = AddComment()
    context = {
        'commentForm': form
    }
    return render(request, template, context)
