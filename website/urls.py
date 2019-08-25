from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

from. import views

urlpatterns = [
	url(r'^jet/', include('jet.urls', 'jet')),
	url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
    url(r'^akademik/', include('akademik.urls')),
    url(r'^galeri/', include('galeri.urls')),
    url(r'^profil/', include('profil.urls')),
    url(r'^pendaftaran/', include('pendaftaran.urls')),
    url(r'^kritiksaran/', include('kritiksaran.urls')),
    url(r'^$', views.home),
]

if settings.DEBUG:
	urlpatterns += [
		url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT,}),
	]