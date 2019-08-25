from django.shortcuts import render, redirect

# Create your views here.

from .forms import FormKritikSaran
from .models import KritikSaran


def index(request):
	Form_ks = FormKritikSaran(request.POST or None)
	if request.method == 'POST':
		if Form_ks.is_valid():
			Form_ks.save()

			return redirect('/')

	context = {
		'data_form':Form_ks,
	}

	return render(request, 'kritiksaran/beranda.html', context)


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
