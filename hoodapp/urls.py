from . import views
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
   url('^$', views.landing,name='landing'),
   url('^home/$', views.home, name='home'),  
]