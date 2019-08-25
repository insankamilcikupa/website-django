from django.shortcuts import render

# Create your views here.

from.models import Galeri

def galeri(request):
	galeri = Galeri.objects.all();
	context = {
		'judul' : 'GALERI TK INSAN KAMIL',
		'gambar' : galeri,
	}
	return render(request, 'galeri/galeri.html', context)