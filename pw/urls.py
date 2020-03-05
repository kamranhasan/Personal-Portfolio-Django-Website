from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home  , name='index'),
    url(r'^about$', views.about , name='about'),
    url(r'^services$', views.services, name='services'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^contacted$', views.message_sent, name='message'),
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^skills$', views.skills, name='skills'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)