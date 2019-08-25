from django.db import models

# Create your models here.

class Galeri(models.Model):
	image = models.ImageField(blank=True, upload_to='media')
	keterangan = models.CharField(max_length=40, blank=True)

	class Meta:
		verbose_name = 'Tabel Galeri'
		verbose_name_plural = 'Tabel Galeri'

	def __str__(self):
		return "{}".format(self.keterangan)
 
