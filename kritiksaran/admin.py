from django.contrib import admin

# Register your models here.

from.models import KritikSaran

class KritikSaranAdmin(admin.ModelAdmin):
    list_display = ('tanggal', 'isi')
    search_field = ('tanggal')

admin.site.register(KritikSaran, KritikSaranAdmin)