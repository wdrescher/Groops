from django.shortcuts import render
from django.contrib.auth import authenticate

def myview(request):
    ...
    return HttpResponseRedirect("/path/")


# Create your views here.
def home(request, pk):
    template = 'communication/userhome.html'
    context = {
        'key': 'value'
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
            return home(request, user.pk)
        else:
            template = 'communication/failedLogin.html'
    return render(request, template, context)
