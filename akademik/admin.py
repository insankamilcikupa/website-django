import csv
from django.contrib import admin
from django.http import HttpResponse

from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from imagekit.cachefiles import ImageCacheFile

from.models import Guru, Siswa, Pengembangan_Siswa, Kelas_Siswa, Penilaian_Siswa, NilaiGuru, PenilaianGuru, SPP_Siswa, Kalender

admin.site.site_header = 'TK Insan Kamil'
admin.site.site_title  = 'TK Insan Kamil'
admin.site.index_title = 'TK Insan Kamil'

#Untuk Tabel Guru
def export_Guru(modeladmin, request, queryset):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment; filename="Guru.csv"'
	writer = csv.writer(response)
	writer.writerow(['NIK', 'Nama_Lengkap', 'Jenis_Kelamin', 'Tempat_Lahir', 'Tanggal_Lahir',
		'Tahun_Masuk', 'Alamat','Jabatan', 'Status', 'No_Telp'])
	Guru = queryset.values_list('NIK', 'Nama_Lengkap', 'Jenis_Kelamin', 'Tempat_Lahir', 'Tanggal_Lahir',
		'Tahun_Masuk', 'Alamat', 'Jabatan', 'Status', 'No_Telp')
	for Guru in Guru:
		writer.writerow(Guru)
	return response
export_Guru.short_description = 'Export to Csv File'

class AdminThumbnailSpec(ImageSpec):
    processors = [ResizeToFill(150, 150)]
    format = 'JPEG'
    options = {'quality': 100 }

def cached_admin_thumb(instance):
    # `image` is the name of the image field on the model
    cached = ImageCacheFile(AdminThumbnailSpec(instance.Foto))
    # only generates the first time, subsequent calls use cache
    cached.generate()
    return cached

# class GaleriAdmin(admin.ModelAdmin):
#     list_display = ('__str__', 'admin_thumbnail')
#     admin_thumbnail = AdminThumbnail(image_field=cached_admin_thumb)

class GuruAdmin(admin.ModelAdmin):

	search_fields = ('NIK', 'Nama_Lengkap')
	list_display = ('NIK', 'Nama_Lengkap', 'Alamat', 'Jabatan', 'Status','No_Telp', 'admin_thumbnail')
	admin_thumbnail = AdminThumbnail(image_field=cached_admin_thumb)
	list_per_page = 3
	actions = [export_Guru,]
	
admin.site.register(Guru, GuruAdmin)

#Untuk Tabel Siswa
def export_Siswa(modeladmin, request, queryset):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment; filename="Siswa.csv"'
	writer = csv.writer(response)
	writer.writerow(['NIS', 'Nama_Lengkap', 'Jenis_Kelamin', 'Tempat_Lahir', 'Tanggal_Lahir', 'Alamat', 'Agama', 'Anak_Ke', 'Tinggi_Badan', 'Berat_Badan', 'Nama_Orang_Tua', 
		'Alamat_Orang_Tua', 'Pekerjaan_Orang_Tua', 'No_Telp_Orang_Tua', 'Kelas', 'Status'])
	Siswa = queryset.values_list('NIS', 'Nama_Lengkap', 'Jenis_Kelamin', 'Tempat_Lahir', 'Tanggal_Lahir', 'Alamat','Agama', 'Anak_Ke', 'Tinggi_Badan', 'Berat_Badan', 'Nama_Orang_Tua', 
		'Alamat_Orang_Tua', 'Pekerjaan_Orang_Tua', 'No_Telp_Orang_Tua', 'Kelas', 'Status')
	for Siswa in Siswa:
		writer.writerow(Siswa)
	return response
export_Siswa.short_description = 'Export to Csv File'

class SiswaAdmin(admin.ModelAdmin):
	list_display = ('NIS', 'Nama_Lengkap', 'Nama_Orang_Tua', 'No_Telp_Orang_Tua', 'Kelas', 'Angkatan', 'Status')
	search_fields = ('NIS', 'Nama_Lengkap', 'Kelas__Nama_Kelas')
	actions = [export_Siswa,]

admin.site.register(Siswa, SiswaAdmin)
#class SiswaAdmin(ImportExportModelAdmin):
	#pass

#Untuk Tabel Penilaian Siswa
class Penilaian_SiswaAdmin(admin.ModelAdmin):
	list_display = ('Siswa', 'Judul_Pengembangan', 'Bulan', 'Penilaian')
	search_fields = ('Siswa__username', 'Judul_Pengembangan__Kode_Pengembangan', 'Bulan')

admin.site.register(Penilaian_Siswa, Penilaian_SiswaAdmin)


#Untuk Tabel Pengembangan Siswa
class Pengembangan_SiswaAdmin(admin.ModelAdmin):
	list_display = ('Kode_Pengembangan', 'Judul_Pengembangan', 'Deskripsi')

admin.site.register(Pengembangan_Siswa, Pengembangan_SiswaAdmin)

#Untuk Tabel Kelas Siswa
class Kelas_SiswaAdmin(admin.ModelAdmin):
	list_display = ('Kode_Kelas', 'Nama_Kelas', 'Keterangan', 'Guru')

admin.site.register(Kelas_Siswa, Kelas_SiswaAdmin)

class NilaiGuruAdmin(admin.ModelAdmin):
	list_display = ('Kode_Nilai', 'Judul_Penilaian', 'Deskripsi')

admin.site.register(NilaiGuru, NilaiGuruAdmin)

class PenilaianGuruAdmin(admin.ModelAdmin):
	list_display = ('Nama_Guru','Indikator','Bulan', 'Penilaian')
	search_fields = ('Nama_Guru__Nama_Lengkap', 'Indikator__Judul_Penilaian', 'Bulan')

admin.site.register(PenilaianGuru, PenilaianGuruAdmin)

class SPP_SiswaAdmin(admin.ModelAdmin):
	list_display = ('Siswa', 'Bulan', 'Keterangan', 'Tanggal')
	search_fields = ('Siswa__username', 'Bulan', 'Keterangan', 'Tanggal')

admin.site.register(SPP_Siswa, SPP_SiswaAdmin)

class KalenderAdmin(admin.ModelAdmin):
	list_display = ('Tanggal', 'Kegiatan')
	search_fields = ('Tanggal', 'Kegiatan')

admin.site.register(Kalender, KalenderAdmin)