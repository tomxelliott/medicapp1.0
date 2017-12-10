from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^quiz/', include('quiz.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),

]
