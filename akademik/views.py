from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

from.models import Guru, Siswa, Penilaian_Siswa, Kalender, SPP_Siswa

def index(request):
    return render(request, 'akademik/index.html')

def guru(request):
	guru = Guru.objects.all();
	context = {
		'judul': 'Guru TK INSAN KAMIL',
		'gambar': guru,
	}

	return render(request, 'akademik/pengajar.html', context)

def kalender(request):
	kalender = Kalender.objects.all()

	context = {
		'judul':'Kalender Akademik TK Insan Kamil',
		'kalender':kalender,
	}

	return render(request, 'akademik/kal.html', context)

def siswa(request):
	siswa = Siswa.objects.all();

	context = {
		'data' : siswa,
	}

	return render(request, 'akademik/siswa.html', context)

def kelasSiswa(request, kelasInput):
	siswa = Siswa.objects.filter(Kelas=kelasInput);
	kelas_data = Siswa.objects.values('Kelas').distinct();

	context = {
		'kelas_data' : kelas_data,
		'data' : siswa,
	}
	return render(request, 'akademik/forkelas.html', context)

def list(request):
	semua_field = Penilaian_Siswa.objects.all()

	context = {
		'page_title' : 'Penilaian_Siswa Siswa',
		'semua_field': semua_field,
	}

	return render(request, 'akademik/list.html', context)

def data(request):
	data = Siswa.objects.filter(Siswa= request.user)
	context = {
		'tampil_data': data,
	}

	return render(request, 'akademik/data.html', context)

def nilai(request):
	nilai = Penilaian_Siswa.objects.filter(Siswa = request.user)
	context = {
		'tampil_nilai': nilai,
	}

	return render(request, 'akademik/nilai.html', context)

def spp(request):
	spp = SPP_Siswa.objects.filter(Siswa = request.user)
	context = {
		'tampil_spp':spp,
	}

	return render(request, 'akademik/spp.html', context)

def ortu(request):
	context = {
		'judul': 'LOGIN ORANG TUA SISWA',
	}

	user = None

	if request.method == "GET":
		if request.user.is_authenticated():
			return redirect('data')
		else:
			return render(request, 'akademik/orangtua.html', context)

	if request.method == "POST":
		username_login = request.POST['username']
		password_login = request.POST['password']

		user = authenticate(request, username=username_login, password=password_login)

		if user is not None:
			login(request, user)
			return redirect('data')
		else:
			return redirect('ortu')

	return render(request, 'akademik/orangtua.html', context)

@login_required
def logoutView(request):
	context = {
		'judul':'LOGOUT',
	}

	if request.method == "POST":
		if request.POST["logout"] == "Submit":
			logout(request)

		return redirect('ortu')

	return render(request, 'akademik/logout.html', context)