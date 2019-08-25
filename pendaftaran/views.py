from django.shortcuts import render

# Create your views here.

#from .forms import DaftarForm
#from .models import DaftarSiswa

def index(request):
    return render(request, 'pendaftaran/index.html')

# def daftar_siswa(request):
#     daftar_form = DaftarForm(request.POST or None)
#     if request.method == 'POST':
#         if daftar_form.is_valid():
#             daftar_form.save()


#     context = {
#         'heading':'Pendaftaran Siswa Baru',
#         'data_form':daftar_form,
#     }
#     return render(request, 'pendaftaran/daftar.html', context)

def menu(request):
	return render(request, 'pendaftaran/menu.html')