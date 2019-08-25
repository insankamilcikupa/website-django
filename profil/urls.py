from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

from. import views

urlpatterns = [
    url(r'^sejarah/', views.sejarah),
    url(r'^visimisi/', views.visimisi),
    url(r'^$', views.index),
]

if settings.DEBUG:
	urlpatterns += [
		url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT,}),
	]
