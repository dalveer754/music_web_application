from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def bio(request):
    return render(request, 'bio.html')

def contact(request):
    print("hii this is contact page ")
    return render(request, 'contact.html')

def concert(request):
    print("hii this is concert page ")
    return render(request, 'concert.html')