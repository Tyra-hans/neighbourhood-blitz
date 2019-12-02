from . import views
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
   url('^$', views.landing,name='landing'),
   url('^home/$', views.home, name='home'),
   url(r'^profile/(?P<username>\w{0,50})/', views.profile, name='profile'),
   url(r'update-profile/',views.update_profile,name='update_profile'),
   url(r'^sites/(\d+)$', views.post, name='post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)