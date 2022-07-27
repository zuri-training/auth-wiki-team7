from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', views.libraries, name='libraries'),
    path('library_detail/<slug:slug>/', views.library_detail, name='library_detail'),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)