from django.conf.urls import include, url
from django.contrib import admin
from engplatform import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'siteLogin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.login),
    url(r'^auth/', views.auth),
    url(r'^main/$', views.mainpage),
    url(r'^main/(.+)', views.selectpage),
]
