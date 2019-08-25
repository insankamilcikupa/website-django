from django.contrib import admin

from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from imagekit.cachefiles import ImageCacheFile

# Register your models here.

from.models import Galeri

class AdminThumbnailSpec(ImageSpec):
    processors = [ResizeToFill(150, 150)]
    format = 'JPEG'
    options = {'quality': 100 }

def cached_admin_thumb(instance):
    # `image` is the name of the image field on the model
    cached = ImageCacheFile(AdminThumbnailSpec(instance.image))
    # only generates the first time, subsequent calls use cache
    cached.generate()
    return cached

class GaleriAdmin(admin.ModelAdmin):
    list_display = ('keterangan', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field=cached_admin_thumb)
    list_per_page = 4

admin.site.register(Galeri, GaleriAdmin)