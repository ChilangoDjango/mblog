from django.conf.urls import url
from blog import views as bviews

urlpatterns = [
    url(r'^$', bviews.BlogIndex.as_view(), name='index'),
    url(r'^article/(?P<slug>\w{1,})/$', bviews.PostDetail.as_view(), name='post'),
]
