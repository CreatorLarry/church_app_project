from django.shortcuts import render

# Create your views here.
# home page
def home(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')