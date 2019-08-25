from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

from. import views

urlpatterns = [
    #url(r'^guru/', views.guru),
    url(r'^logout/', views.logoutView, name='logout'),
    url(r'^ortu/', views.ortu, name='ortu'),
    url(r'^data/', views.data, name='data'),
    url(r'^nilai/', views.nilai, name='nilai'),
    url(r'^spp/', views.spp, name='spp'),
    url(r'^list/', views.list, name='list'),
    url(r'^kalender/', views.kalender),
    url(r'^guru/', views.guru),
    url(r'^siswa/', views.siswa),
    url(r'^kelas/(?P<kelasInput>[\w-]+)/$', views.kelasSiswa),
    url(r'^$', views.index),
]

if settings.DEBUG:
	urlpatterns += [
		url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT,}),
	]
