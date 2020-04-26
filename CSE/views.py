from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'CSE/index.html')

def aboutus(request):
    return render(request, 'CSE/aboutus.html')

def contactus(request):
    return render(request, 'CSE/contactus.html')   

    