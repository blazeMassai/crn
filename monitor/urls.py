from django.conf.urls import url
from monitor import views

from django.urls import path

urlpatterns = [

    #url(r'^$' , views.HomeView.as_view(),name='home'),
    
    url(r'^crn/(?P<pk>\d+)$', views.CrnDetailView.as_view(),name='crn_detail'),
    url(r'^crn/new/$', views.CreateCrnView.as_view(),name='crn_new'),
    url(r'^crn/(?P<pk>\d+)/edit/$', views.CrnUpdateView.as_view(),name='crn_edit'),
    url(r'^crn/(?P<pk>\d+)/remove/$', views.CrnDeleteView.as_view(),name='crn_remove'),
    url(r'^crn/$' ,views.CrnListView.as_view(),name='crn_list'),
    #path('search' ,views.search, name='search'),
    path('all_crn' ,views.allcrn, name='allcrn'),
]
