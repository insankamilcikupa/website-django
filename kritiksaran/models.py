from django.db import models

# Create your models here.

class KritikSaran(models.Model):
	isi = models.TextField(blank=False, null=False)
	tanggal = models.DateTimeField(auto_now_add=True, blank=False)

	class Meta:
		verbose_name = 'Tabel Kritik dan Saran'
		verbose_name_plural = 'Tabel Kritik dan Saran'

	def __str__(self):
		return "{}".format(self.tanggal)
