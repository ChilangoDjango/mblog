from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bloggy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls', namespace='blog'))
]
