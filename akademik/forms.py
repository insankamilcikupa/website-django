from django import forms

from .models import Penilaian_Siswa

class Penilaian_SiswaForm(forms.ModelForm):
	class Meta:
		model = Penilaian_Siswa
		fields = [
			'Nama_Siswa',
			'Kode_Pengembangan',
			'Bulan',
			'Penilaian',
		]

		Pilihan_Bulan = (
	        ('Jan', 'Januari'),
	        ('Feb', 'Februari'),
	        ('Mar', 'Maret'),
	        ('Apr', 'April'),
	        ('Mei', 'Mei'),
	        ('Jun', 'Juni'),
	        ('Jul', 'Juli'),
	        ('Agus', 'Agustus'),
	        ('Sept', 'September'),
	        ('Okt', 'Oktober'),
	        ('Nov', 'November'),
	        ('Des', 'Desember'),
	    )

	    Bulan = forms.ChoiceField(
	        widget=forms.Select(choices=Pilihan_Bulan)
	    )
