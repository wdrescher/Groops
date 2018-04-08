from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'communication/userhome.html'
    context = {
        'key': 'value',
    }
    return render(request, template, context)
