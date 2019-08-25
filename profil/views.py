from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def visimisi(request):
	return render(request, 'profil/profil.html')

def sejarah(request):
	return render(request, 'profil/profil.html')

