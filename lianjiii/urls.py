"""lianjiii URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from lianjia import views as lianjia_views

urlpatterns = [
	url(r'^$', 'lianjia.views.index'),
	url(r'^show', 'lianjia.views.showlist'),
	url(r'^loginpage', 'lianjia.views.page1'),
	url(r'^login$', 'lianjia.views.login'),
	url(r'^register$', 'lianjia.views.register'),
	url(r'^template/(\d+)/(\d+)', lianjia_views.template, name='template'),
	url(r'^add', lianjia_views.add, name='add'),
    url(r'^admin/', include(admin.site.urls)),
]
