from django.conf.urls import patterns, include, url

from findmycarproject.findmycarapp import views_controller

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'findmycarproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views_controller.index, name='index'),

)