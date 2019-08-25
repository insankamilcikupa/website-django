from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

#MODEL TABEL GURU
class Guru(models.Model):
	user = models.OneToOneField(User)
	NIK = models.CharField(max_length=12, blank=False, primary_key=True)
	Nama_Lengkap = models.CharField(max_length=50, blank=False)
	Nama_Panggilan = models.CharField(max_length=20, blank=False)
	jk = (
		('P','Pria'),
		('W','Wanita'),
		)
	Jenis_Kelamin = models.CharField(max_length=10, choices=jk, default='P')
	Tempat_Lahir = models.CharField(max_length=25, blank=False)
	Tanggal_Lahir = models.DateField(max_length=50, blank=False)
	Tahun_Masuk = models.CharField(max_length=4, blank=False, default='1999')
	Alamat = models.CharField(max_length=60, blank=False)
	Jabatan = models.CharField(max_length=15, blank=False)
	Status = models.CharField(max_length=15)
	No_Telp = models.CharField(max_length=13)
	Motto = models.CharField(max_length=255)
	Foto = models.ImageField(blank=True, upload_to='media')

	class Meta:
		verbose_name = 'Tabel Guru'
		verbose_name_plural = 'Tabel Guru'

	def __str__(self):
		return "{}".format(self.Nama_Lengkap)

#MODEL TABEL KELAS SISWA
class Kelas_Siswa(models.Model):
	Kode_Kelas = models.CharField(max_length=3, blank=False, primary_key=True)
	Nama_Kelas = models.CharField(max_length=5)
	Keterangan = models.CharField(max_length=50, null=True)
	Guru = models.ForeignKey(Guru, to_field='NIK')

	class Meta:
		verbose_name = 'Tabel Siswa (Kelas Siswa)'
		verbose_name_plural = 'Tabel Siswa (Kelas Siswa)'

	def __str__(self):
		return "{}".format(self.Nama_Kelas)

#MODEL TABEL SISWA
class Siswa(models.Model):
	Siswa = models.OneToOneField(User, null=True)
	NIS = models.CharField(max_length=15, blank=False, primary_key=True)
	Nama_Lengkap = models.CharField(max_length=50, blank=False, null=False)
	Nama_Panggilan = models.CharField(max_length=20, blank=False, null=False)

	jk = (
		('P','Pria'),
		('W','Wanita'),
		)
	Jenis_Kelamin = models.CharField(max_length=10, choices=jk, default='P')
	Tempat_Lahir = models.CharField(max_length=25, blank=False, null=True)
	Tanggal_Lahir = models.DateField(blank=False)
	Alamat = models.CharField(max_length=60, null=True)
	Agama = models.CharField(max_length=10, null=True)
	Anak_Ke = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(50)])
	Tinggi_Badan = models.IntegerField(null=True, validators=[MinValueValidator(80), MaxValueValidator(150)])
	Berat_Badan = models.IntegerField(null=True, validators=[MinValueValidator(10), MaxValueValidator(50)])
	Nama_Orang_Tua = models.CharField(max_length=50, null=True)
	Alamat_Orang_Tua = models.CharField(max_length=60, null=True)
	Pekerjaan_Orang_Tua = models.CharField(max_length=40, null=True)
	No_Telp_Orang_Tua = models.CharField(max_length=13, null=True)
	Kelas = models.ForeignKey(Kelas_Siswa, to_field='Kode_Kelas', null=True)

	angkatan = (
		('Ganjil 18/19', 'Ganjil 18/19'),
		('Genap 18/19', 'Genap 18/19'),
		)
	Angkatan = models.CharField(max_length=15, choices=angkatan, null=True)

	status = (
		('Aktif','Aktif'),
		('TA', 'Tidak Aktif'),
		)
	Status = models.CharField(max_length=10, choices=status, default='Aktif')

	class Meta:
		verbose_name = 'Tabel Siswa'
		verbose_name_plural = 'Tabel Siswa'

	def __str__(self):
		return "{}.".format(self.Nama_Lengkap)

#MODEL TABEL PENGEMBANGAN SISWA	
class Pengembangan_Siswa(models.Model):
	Kode_Pengembangan = models.CharField(max_length=5, blank=False, primary_key=True)
	Judul_Pengembangan = models.CharField(max_length=50)
	Deskripsi = models.TextField(null=True)

	class Meta:
		verbose_name = 'Tabel Siswa (Pengembangan Siswa)'
		verbose_name_plural = 'Tabel Siswa (Pengembangan Siswa)'

	def __str__(self):
		return "{}".format(self.Judul_Pengembangan)


#MODEL TABEL PENILAIAN SISWA
class Penilaian_Siswa(models.Model):
	Siswa = models.ForeignKey(User, null=True)
	Judul_Pengembangan = models.ForeignKey(Pengembangan_Siswa, to_field='Kode_Pengembangan')

	Pilihan_Bulan = (
        ('Januari Minggu 1', 'Januari M1'),
        ('Januari Minggu 2', 'Januari M2'),
        ('Januari Minggu 3', 'Januari M3'),
        ('Januari Minggu 4', 'Januari M4'),
        ('Februari Minggu 1', 'Februari M1'),
        ('Februari Minggu 2', 'Februari M2'),
        ('Februari Minggu 3', 'Februari M3'),
        ('Februari Minggu 4', 'Februari M4'),
        ('Maret Minggu 1', 'Maret M1'),
        ('Maret Minggu 2', 'Maret M2'),
        ('Maret Minggu 3', 'Maret M3'),
        ('Maret Minggu 4', 'Maret M4'),
        ('April Minggu 1', 'April M1'),
        ('April Minggu 2', 'April M2'),
        ('April Minggu 3', 'April M3'),
        ('April Minggu 4', 'April M4'),
        ('Mei Minggu 1', 'Mei M1'),
        ('Mei Minggu 2', 'Mei M2'),
        ('Mei Minggu 3', 'Mei M3'),
        ('Mei Minggu 4', 'Mei M4'),
        ('Juni Minggu 1', 'Juni M1'),
        ('Juni Minggu 2', 'Juni M2'),
        ('Juni Minggu 3', 'Juni M3'),
        ('Juni Minggu 4', 'Juni M4'),
        ('Juli Minggu 1', 'Juli M1'),
        ('Juli Minggu 2', 'Juli M2'),
        ('Juli Minggu 3', 'Juli M3'),
        ('Juli Minggu 4', 'Juli M4'),
        ('Agustus Minggu 1', 'Agustus M1'),
        ('Agustus Minggu 2', 'Agustus M2'),
        ('Agustus Minggu 3', 'Agustus M3'),
        ('Agustus Minggu 4', 'Agustus M4'),
        ('September Minggu 1', 'September M1'),
        ('September Minggu 2', 'September M2'),
        ('September Minggu 3', 'September M3'),
        ('September Minggu 4', 'September M4'),
        ('Oktober Minggu 1', 'Oktober M1'),
        ('Oktober Minggu 2', 'Oktober M2'),
        ('Oktober Minggu 3', 'Oktober M3'),
        ('Oktober Minggu 4', 'Oktober M4'),
        ('November Minggu 1', 'November M1'),
        ('November Minggu 2', 'November M2'),
        ('November Minggu 3', 'November M3'),
        ('November Minggu 4', 'November M4'),
        ('Desember Minggu 1', 'Desember M1'),
        ('Desember Minggu 2', 'Desember M2'),
        ('Desember Minggu 3', 'Desember M3'),
        ('Desember Minggu 4', 'Desember M4'),
    )

	Bulan = models.CharField(max_length=15, choices=Pilihan_Bulan, null=True)

	Pilihan_Nilai = (
		('SB', 'Sangat Bisa'),
		('B', 'Bisa'),
		('CB', 'Cukup Bisa'),
		('BB', 'Belum Bisa'),
	)

	Penilaian = models.CharField(max_length=20, choices=Pilihan_Nilai, null=False, blank=False)
	Deskripsi = models.TextField(null=True)

	class Meta:
		verbose_name = 'Tabel Siswa (Penilaian Siswa)'
		verbose_name_plural = 'Tabel Siswa (Penilaian Siswa)'

	def __str__(self):
		return "{}".format(self.Siswa)

#MODEL TABEL NILAI GURU
class NilaiGuru(models.Model):
	Kode_Nilai = models.CharField(max_length=5, blank=False, primary_key=True)
	Judul_Penilaian = models.CharField(max_length=50)
	Deskripsi = models.TextField(null=True)

	class Meta:
		verbose_name = 'Tabel Guru (Nilai Guru)'
		verbose_name_plural = 'Tabel Guru (Nilai Guru)'

	def __str__(self):
		return "{}".format(self.Judul_Penilaian)	

#MODEL TABEL PENILAIAN GURU
class PenilaianGuru(models.Model):
	Nama_Guru = models.ForeignKey(Guru)
	Indikator = models.ForeignKey(NilaiGuru)

	Pilihan_Bulan = (
        ('Januari', 'Januari'),
        ('Februari', 'Februari'),
        ('Maret', 'Maret'),
        ('April', 'April'),
        ('Mei', 'Mei'),
        ('Juni', 'Juni'),
        ('Juli', 'Juli'),
        ('Agustus', 'Agustus'),
        ('September', 'September'),
        ('Oktober', 'Oktober'),
        ('November', 'November'),
        ('Desember', 'Desember'),
    )

	Bulan = models.CharField(max_length=15, choices=Pilihan_Bulan, null=True)
	Penilaian = models.IntegerField(null=False, validators=[MinValueValidator(0), MaxValueValidator(10)])

	class Meta:
		verbose_name = 'Tabel Guru (Penilaian Guru)'
		verbose_name_plural = 'Tabel Guru (Penilaian Guru)'

	def __str__(self):
		return "{}".format(self.Nama_Guru)

#MODEL TABEL SPP SISWA
class SPP_Siswa(models.Model):
	Siswa = models.ForeignKey(User, null=True)
	SPP_Bulan = (
        ('Januari', 'Januari'),
        ('Februari', 'Februari'),
        ('Maret', 'Maret'),
        ('April', 'April'),
        ('Mei', 'Mei'),
        ('Juni', 'Juni'),
        ('Juli', 'Juli'),
        ('Agustus', 'Agustus'),
        ('September', 'September'),
        ('Oktober', 'Oktober'),
        ('November', 'November'),
        ('Desember', 'Desember'),
    )

	Bulan = models.CharField(max_length=15, choices=SPP_Bulan, null=False)

	Ket_SPP = (
		('Lunas', 'Lunas'),
		('Belum Lunas', 'Belum Lunas'),
	)

	Keterangan = models.CharField(max_length=15, choices=Ket_SPP, null=True, blank=True)
	Tanggal = models.DateField(auto_now_add=True, blank=False)

	class Meta:
		verbose_name = 'Tabel Siswa (Pembayaran SPP Siswa)'
		verbose_name_plural = 'Tabel Siswa (Pembayaran SPP Siswa)'

	def __str__(self):
		return "{}".format(self.Siswa)

#MODEL KALENDER AKADEMIK
class Kalender(models.Model):
	Tanggal = models.DateField(blank=False, null=False)
	Kegiatan = models.CharField(max_length=100, blank=True, null=True)

	class Meta:
		verbose_name = 'Tabel Kalender Akademik'
		verbose_name_plural = 'Tabel Kalender Akademik'

	def __str__(self):
		return "{}".format(self.Tanggal)