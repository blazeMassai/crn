
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

urlpatterns = [
	url(r'^select2/', include('django_select2.urls')),
    path('' , include('pages.urls')),
    url(r'', include('monitor.urls')),
    url(r'^accounts/login/$' ,views.login, name='login'),
    url(r'^accounts/logout/$' ,views.logout,name='logout' ,kwargs={'next_page':'/'}),

    path('admin/', admin.site.urls),
]
